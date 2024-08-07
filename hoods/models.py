from django.db import models


class Hoods(models.Model):
    hood_id = models.AutoField(primary_key=True, blank=True)
    hood_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.URLField(blank=True)
    member_count = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    # is_booking = models.BooleanField(default=True)

    def __str__(self):
        return self.hood_name
