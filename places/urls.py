from django.urls import path
from .views.tourist_place_view import TouristPlaceListCreateView, TouristPlaceDetailView
from .views.tag_view import TagListView, TagDetailView
from .views.add_review_view import AddRatingView
from .views.tour_package_view import TourPackageListCreateView, TourPackageDetailView
from .views.place_listReview_view import PlaceReviewListView
from .views.most_places_visited_view import MostVisitedPlacesView
from .views.booking_add_view import BookingAddView
from .views.bookinglist_view import BookingListView
from .views.booking_delete_view import BookingDeleteView
urlpatterns = [
    # Tourist Places
    path('api/places/', TouristPlaceListCreateView.as_view(), name='place-list'),
    path('api/places/<int:pk>/', TouristPlaceDetailView.as_view(), name='place-detail'),

    # Tags
    path('api/tags/', TagListView.as_view(), name='tag-list'),
    path('api/tags/<int:pk>/', TagDetailView.as_view(), name='tag-detail'),

    # Reviews
    path('Reviews/addreviews/', AddRatingView.as_view(), name='add_review'),
    path('Reviews/places/<uuid:place_id>/allreviews/', PlaceReviewListView.as_view(), name='place_reviews'),

    #most visited
    path('most visited/places/most-visited/', MostVisitedPlacesView.as_view(), name='most_visited_places'),

    # Tour Packages
    path('Tour Packages/tour-packages/', TourPackageListCreateView.as_view(), name='tourpackage-list'),
    path('Tour Packages/tour-packages/<int:pk>/', TourPackageDetailView.as_view(), name='tourpackage-detail'),

    # Bookings
    path('Bookings/allbookings/', BookingListView.as_view(), name='booking-list'),
    path('Bookings/bookings/add/', BookingAddView.as_view(), name='booking-add'),
    path('Bookings/bookings/<uuid:pk>/delete/', BookingDeleteView.as_view(), name='booking-delete'),
]
