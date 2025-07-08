from django.db import models
from .tag_model import Tag

class TouristPlace(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    image = models.ImageField(upload_to='places/')
    opening_hours = models.CharField(max_length=255)
    entry_fee = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    # M2M with Tag
    tags = models.ManyToManyField(Tag, related_name='places', blank=True)

    def __str__(self):
        return self.name
