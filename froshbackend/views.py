from events.models import Events
from rest_framework import serializers
from events.models import passes
from users.models import User

from django.db.models import Count, Sum, F, ExpressionWrapper, FloatField, IntegerField, Case, When, Subquery, OuterRef
from django.db.models.functions import Cast
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt
def testing(request):
    if request.method == 'GET':
      
        result = Events.objects.annotate(
            total_passes=Count('passes'),
            booked_passes=Sum(Case(
                When(passes__is_booked=True, then=1),
                default=0,
                output_field=IntegerField()
            )),
            scanned_passes=Sum(Case(
                When(passes__is_scanned=True, then=1),
                default=0,
                output_field=IntegerField()
            )),
            booking_rate=ExpressionWrapper(
                Cast(F('booked_passes'), FloatField()) / Cast(F('passes_generated'), FloatField()) * 100,
                output_field=FloatField()
            ),
            scan_rate=ExpressionWrapper(
                Cast(F('scanned_passes'), FloatField()) / Cast(F('booked_passes'), FloatField()) * 100,
                output_field=FloatField()
            )
        ).annotate(
            user_engagement=Subquery(
                passes.objects.filter(event_id=OuterRef('pk'))
                .values('registration_id')
                .annotate(engagement_score=Sum(
                    Case(
                        When(is_booked=True, then=1),
                        When(is_scanned=True, then=2),
                        default=0,
                        output_field=IntegerField()
                    )
                ))
                .order_by('-engagement_score')
                .values('engagement_score')[:1]
            )
        ).filter(
            date__gte=timezone.now().date(),
            is_live=True,
            is_display=True,
            total_passes__gt=0,
            booking_rate__gt=50,
            scan_rate__gt=25
        ).order_by('-date', '-user_engagement', '-booking_rate')[:50]

        result_list = list(result.values('id', 'name', 'date', 'total_passes', 'booked_passes', 'scanned_passes', 'booking_rate', 'scan_rate', 'user_engagement'))

        return JsonResponse({'results': result_list})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)