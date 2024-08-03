from django.db import models
from django.conf import settings

class Events(models.Model):
    event_id = models.AutoField( primary_key=True, blank=False)
    name = models.CharField(max_length=256)
    description = models.TextField()
    venue = models.CharField(max_length=256)
    date = models.DateField()
    time = models.CharField(max_length=256)
    available_tickets = models.IntegerField(blank=True, default=350) 
    passes_generated = models.IntegerField()
    image = models.URLField(default='https://darkroomphotos.com/wp-content/uploads/2021/10/image-file-formats-header-1-1-678x381@2x.png')
    calendar_url = models.URLField(default='#')
    booking_required = models.BooleanField(default=True)
    is_booking = models.BooleanField(default=False)
    is_live = models.BooleanField(default=False)
    is_display = models.BooleanField(default=False)
    slots_required = models.BooleanField(default=False)
    booking_complete = models.BooleanField(default=False)
    slot_id = models.CharField(max_length=16, default='lmao')

    def __str__(self):
        return self.name

class passes(models.Model):
    event_id= models.ForeignKey(Events, on_delete=models.CASCADE, related_name='passes')
    # registration_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='registered_passes')
    secure_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='secured_passes')
    is_booked = models.BooleanField("is_booked", default=False)
    is_scanned = models.BooleanField("is_scanned", default=False)
    last_scanned = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return f"Pass for {self.event.name} - User: {self.secure_id}"