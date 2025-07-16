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
    location = models.CharField(max_length=100, default='Not specified')
    
    # New field to track visits
    visit_count = models.PositiveIntegerField(default=0)

    # M2M with Tag
    tags = models.ManyToManyField(Tag, related_name='places', blank=True)

    def __str__(self):
        return self.name
