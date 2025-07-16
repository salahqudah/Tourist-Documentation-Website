from django.db import models
from django.contrib.auth import get_user_model
from .tourist_place_model import TouristPlace
User = get_user_model()

class TourPackage(models.Model):
    guide = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'is_staff': True},
        related_name='tour_packages'
    )
    place = models.ForeignKey(TouristPlace, on_delete=models.CASCADE, related_name='tour_packages')  # ✅ Add this
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField(null=True, blank=True)

    # 🔄 Changed from PositiveIntegerField to CharField
    duration_days = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} by {self.guide.username}"
