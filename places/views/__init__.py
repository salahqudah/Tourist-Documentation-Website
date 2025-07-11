from .tourist_place_view import TouristPlaceListCreateView, TouristPlaceDetailView
from .tag_view import TagListView, TagDetailView
from .review_view import AddRatingView
from .tour_package_view import TourPackageListCreateView, TourPackageDetailView
from .booking_view import BookingListCreateView, BookingDetailView

__all__ = [
    "TouristPlaceListCreateView", "TouristPlaceDetailView",
    "TagListView", "TagDetailView",
    "AddRatingView",
    "TourPackageListCreateView", "TourPackageDetailView",
    "BookingListCreateView", "BookingDetailView",
]
