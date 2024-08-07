from django.contrib import admin
from .models import Events, passes

admin.site.register(Events)

admin.site.register(passes)
class PassesAdmin(admin.ModelAdmin):
    list_display = ('event', 'secure_id', 'is_booked', 'is_scanned', 'last_scanned')
    list_filter = ('event', 'is_booked', 'is_scanned')
    search_fields = ('event__name', 'secure_id__username')  