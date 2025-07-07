from django.urls import path
from .views.tourist_place_view import TouristPlaceListCreateView, TouristPlaceDetailView
from .views.tag_view import TagListView, TagDetailView
from .views.review_view import ReviewListCreateView, ReviewDetailView
from .views.tour_package_view import TourPackageListCreateView, TourPackageDetailView
from .views.booking_view import BookingListCreateView, BookingDetailView

urlpatterns = [
    # Tourist Places
    path('api/places/', TouristPlaceListCreateView.as_view(), name='place-list'),
    path('api/places/<int:pk>/', TouristPlaceDetailView.as_view(), name='place-detail'),

    # Tags
    path('api/tags/', TagListView.as_view(), name='tag-list'),
    path('api/tags/<int:pk>/', TagDetailView.as_view(), name='tag-detail'),

    # Reviews
    path('api/reviews/', ReviewListCreateView.as_view(), name='review-list'),
    path('api/reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),

    # Tour Packages
    path('api/tour-packages/', TourPackageListCreateView.as_view(), name='tourpackage-list'),
    path('api/tour-packages/<int:pk>/', TourPackageDetailView.as_view(), name='tourpackage-detail'),

    # Bookings
    path('api/bookings/', BookingListCreateView.as_view(), name='booking-list'),
    path('api/bookings/<int:pk>/', BookingDetailView.as_view(), name='booking-detail'),
]
