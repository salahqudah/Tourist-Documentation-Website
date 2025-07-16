from django.core.management.base import BaseCommand
from django.core.serializers import serialize
import os

# Import your models
from places.models.tourist_place_model import TouristPlace
from places.models.tag_model import Tag
from places.models.place_tag_model import PlaceTag
from places.models.tour_package_model import TourPackage
from places.models.booking_model import Booking
from places.models.transaction_model import Transaction
from places.models.review_model import Review
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Export model data to fixtures/data/*.json'

    def export_model(self, model, filename):
        data = serialize('json', model.objects.all())
        path = os.path.join('fixtures', 'data', filename)
        with open(path, 'w') as f:
            f.write(data)
        self.stdout.write(self.style.SUCCESS(f"✅ Exported {model.__name__} to {filename}"))

    def handle(self, *args, **kwargs):
        self.export_model(User, 'users_fixture.json')
        self.export_model(TouristPlace, 'tourist_place_fixture.json')
        self.export_model(Tag, 'tag_fixture.json')
        self.export_model(PlaceTag, 'place_tag_fixture.json')
        self.export_model(TourPackage, 'tour_package_fixture.json')
        self.export_model(Booking, 'booking_fixture.json')
        self.export_model(Transaction, 'transaction_fixture.json')
        self.export_model(Review, 'review_fixture.json')
