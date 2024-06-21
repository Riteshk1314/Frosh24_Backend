from django.db import models

# Create your models here.

class Eventlist(models.Model):
    event_id = models.CharField(max_length=50, unique=True, primary_key=True)
    name = models.CharField(max_length=256)
    description = models.TextField()
    venue = models.CharField(max_length=256)
    date = models.DateField()
    time = models.CharField(max_length=256)
    max_capacity = models.IntegerField()
    passes_generated = models.IntegerField()
    image = models.URLField(default='https://darkroomphotos.com/wp-content/uploads/2021/10/image-file-formats-header-1-1-678x381@2x.png')
    calendar_url = models.URLField(default='#')
    booking_required = models.BooleanField(default=True)
    is_booking = models.BooleanField(default=False)
    is_display = models.BooleanField(default=False)
    slots_required = models.BooleanField(default=False)
    booking_complete = models.BooleanField(default=False)
    slot_id = models.CharField(max_length=16, default='lmao')


    def __str__(self):
        return self.name

