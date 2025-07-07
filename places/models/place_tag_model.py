from django.db import models
from .tourist_place_model import TouristPlace
from .tag_model import Tag

class PlaceTag(models.Model):
    place = models.ForeignKey(TouristPlace, on_delete=models.CASCADE, related_name='place_tags')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='tag_places')
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('place', 'tag')  # prevent duplicates

    def __str__(self):
        return f"{self.place.name} - {self.tag.name}"
