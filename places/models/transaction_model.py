from django.db import models
from django.contrib.auth import get_user_model
from .tour_package_model import TourPackage
from .tourist_place_model import TouristPlace

User = get_user_model()

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tour_package = models.ForeignKey(TourPackage, on_delete=models.CASCADE)
    tourist_places = models.ManyToManyField(TouristPlace, blank=True)
    amount_paid = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Transaction #{self.id} by {self.user.username} for {self.tour_package.name}"