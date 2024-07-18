from django.db import models


class Events(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    venue = models.CharField(max_length=256)
    date = models.DateField()
    time = models.CharField(max_length=256)
    available_tickets=models.IntegerField(blank=True, default=350) 
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

