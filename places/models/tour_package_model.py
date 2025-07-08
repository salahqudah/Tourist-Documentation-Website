from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class TourPackage(models.Model):
    guide = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_staff': True})
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    duration_days = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} by {self.guide.username}"
