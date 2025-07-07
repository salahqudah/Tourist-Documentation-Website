from django.urls import path
from .views.tourist_place_view import TouristPlaceListCreateView, TouristPlaceDetailView
from .views.tag_view import TagListCreateView, TagDetailView
from .views.review_view import ReviewListCreateView, ReviewDetailView
from .views.tour_package_view import TourPackageListCreateView, TourPackageDetailView
from .views.booking_view import BookingListCreateView, BookingDetailView

urlpatterns = [
    # Tourist Places
    path('places/', TouristPlaceListCreateView.as_view(), name='place-list'),
    path('places/<int:pk>/', TouristPlaceDetailView.as_view(), name='place-detail'),

    # Tags
    path('tags/', TagListCreateView.as_view(), name='tag-list'),
    path('tags/<int:pk>/', TagDetailView.as_view(), name='tag-detail'),

    # Reviews
    path('reviews/', ReviewListCreateView.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),

    # Tour Packages
    path('tour-packages/', TourPackageListCreateView.as_view(), name='tourpackage-list'),
    path('tour-packages/<int:pk>/', TourPackageDetailView.as_view(), name='tourpackage-detail'),

    # Bookings
    path('bookings/', BookingListCreateView.as_view(), name='booking-list'),
    path('bookings/<int:pk>/', BookingDetailView.as_view(), name='booking-detail'),
]
