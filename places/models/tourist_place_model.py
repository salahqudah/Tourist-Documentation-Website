from django.db import models
import uuid
from django.core.validators import MaxValueValidator, MinValueValidator
from .tag_model import Tag

class TouristPlace(models.Model):
    # UUID primary key
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    image = models.ImageField(upload_to='places/')
    opening_hours = models.CharField(max_length=255)
    entry_fee = models.FloatField(validators=[MinValueValidator(0)], default=0)
    location = models.CharField(max_length=255, default='Not specified')
    
    # Track how many people visited the place
    visit_count = models.PositiveIntegerField(default=0)

    # Rating info (if needed)
    total_rating = models.FloatField(validators=[MaxValueValidator(5)], default=0)
    sum_of_ratings = models.IntegerField(validators=[MaxValueValidator(1000000)], default=0)
    number_of_ratings = models.IntegerField(validators=[MaxValueValidator(1000000)], default=0)

    # Many-to-many with tags
    tags = models.ManyToManyField(Tag, related_name='places', blank=True)

    def __str__(self):
        return self.name
