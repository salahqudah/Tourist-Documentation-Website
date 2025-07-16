from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from ..models import PlaceTag
from ..serializers import PlaceTagSerializer
from django.shortcuts import get_object_or_404

class PlaceTagListCreateView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        tags = PlaceTag.objects.all()
        serializer = PlaceTagSerializer(tags, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PlaceTagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PlaceTagDetailView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def delete(self, request, pk):
        place_tag = get_object_or_404(PlaceTag, pk=pk)
        place_tag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
