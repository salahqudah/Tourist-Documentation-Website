from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..models import TouristPlace
from ..serializers import TouristPlaceSerializer

class TouristPlaceListCreateView(APIView):
    def get(self, request):
        places = TouristPlace.objects.all()
        serializer = TouristPlaceSerializer(places, many=True)
        return Response(serializer.data)

    def post(self, request):
        # You should add permission checks here for admin/guide only
        serializer = TouristPlaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TouristPlaceDetailView(APIView):
    def get(self, request, pk):
        place = get_object_or_404(TouristPlace, pk=pk)
        serializer = TouristPlaceSerializer(place)
        return Response(serializer.data)

    def put(self, request, pk):
        # Add permission checks here
        place = get_object_or_404(TouristPlace, pk=pk)
        serializer = TouristPlaceSerializer(place, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Add permission checks here
        place = get_object_or_404(TouristPlace, pk=pk)
        place.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
