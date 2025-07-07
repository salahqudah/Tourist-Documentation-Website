from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..models import TouristPlace
from ..serializers import TouristPlaceSerializer
from rest_framework.permissions import IsAuthenticated


class TouristPlaceListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        places = TouristPlace.objects.all()
        serializer = TouristPlaceSerializer(places, many=True)
        return Response(serializer.data)

    def post(self, request):
        if not request.user.is_staff:
            return Response(
                {"detail": "Only staff can add tourist places."},
                status=status.HTTP_403_FORBIDDEN
            )
        serializer = TouristPlaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TouristPlaceDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        place = get_object_or_404(TouristPlace, pk=pk)
        serializer = TouristPlaceSerializer(place)
        return Response(serializer.data)

    def put(self, request, pk):
        place = get_object_or_404(TouristPlace, pk=pk)
        if not request.user.is_staff:
            return Response(
                {"detail": "Only staff can update tourist places."},
                status=status.HTTP_403_FORBIDDEN
            )
        serializer = TouristPlaceSerializer(place, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        place = get_object_or_404(TouristPlace, pk=pk)
        if not request.user.is_staff:
            return Response(
                {"detail": "Only staff can delete tourist places."},
                status=status.HTTP_403_FORBIDDEN
            )
        place.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
