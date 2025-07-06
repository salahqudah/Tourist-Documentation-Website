from django.db import models
from django.contrib.auth import get_user_model
from .tour_package_model import TourPackage

User = get_user_model()
class BookingStatus(models.IntegerChoices):
    CONFIRMED=1,'confirmed'
    CANCELED=2,'canceled'


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tour_package = models.ForeignKey(TourPackage, on_delete=models.CASCADE)
    status = models.IntegerField(choices=BookingStatus.choices, default=BookingStatus.CONFIRMED)
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.tour_package.name} ({self.get_status_display()})"
