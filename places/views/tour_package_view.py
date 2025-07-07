from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404
from ..models import TourPackage
from ..serializers import TourPackageSerializer

class TourPackageListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        packages = TourPackage.objects.all()
        serializer = TourPackageSerializer(packages, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TourPackageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(guide=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TourPackageDetailView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, pk):
        package = get_object_or_404(TourPackage, pk=pk)
        serializer = TourPackageSerializer(package)
        return Response(serializer.data)

    def put(self, request, pk):
        package = get_object_or_404(TourPackage, pk=pk)
        if package.guide != request.user:
            return Response({'detail': 'Not authorized'}, status=status.HTTP_403_FORBIDDEN)

        serializer = TourPackageSerializer(package, data=request.data)
        if serializer.is_valid():
            serializer.save(guide=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        package = get_object_or_404(TourPackage, pk=pk)
        if package.guide != request.user:
            return Response({'detail': 'Not authorized'}, status=status.HTTP_403_FORBIDDEN)
        package.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
