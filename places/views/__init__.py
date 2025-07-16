from .tourist_place_view import TouristPlaceListCreateView, TouristPlaceDetailView
from .tag_view import TagListView, TagDetailView
from .add_review_view import AddRatingView
from .tour_package_view import TourPackageListCreateView, TourPackageDetailView
from .bookinglist_view import BookingListView
from .booking_add_view import BookingAddView
from .booking_delete_view import BookingDeleteView

__all__ = [
    "TouristPlaceListCreateView", "TouristPlaceDetailView",
    "TagListView", "TagDetailView",
    "AddRatingView",
    "TourPackageListCreateView", "TourPackageDetailView",
    "BookingListView", "BookingAddView","BookingDeleteView"
    
    
    ]
