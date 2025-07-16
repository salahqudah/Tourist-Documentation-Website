import re
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models.tourist_place_model import TouristPlace
from ..serializers.tourist_place_serializer import TouristPlaceSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rapidfuzz import fuzz


def normalize(text):
    return re.sub(r'\s+', ' ', re.sub(r'[^a-z0-9]+', ' ', text.lower())).strip()


class TouristPlaceSearchView(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'search': openapi.Schema(type=openapi.TYPE_STRING, description='Search term'),
            },
            required=[],
        ),
        responses={200: TouristPlaceSerializer(many=True)}
    )
    def post(self, request, *args, **kwargs):
        search_query_raw = request.data.get('search', '')
        search_query = normalize(search_query_raw)

        all_places = TouristPlace.objects.all()
        results = []

        if search_query:
            query_length = len(search_query)

            # Set threshold and scorer dynamically based on query length
            if query_length == 1:
                threshold = 30
                scorer = fuzz.partial_ratio
            elif query_length == 2:
                threshold = 40
                scorer = fuzz.partial_ratio
            elif query_length == 3:
                threshold = 45
                scorer = fuzz.partial_ratio
            else:
                threshold = 60
                scorer = fuzz.token_set_ratio

            for place in all_places:
                name = normalize(place.name or '')
                description = normalize(place.description or '')

                name_score = scorer(search_query, name)
                desc_score = scorer(search_query, description)

                combined_score = 0.7 * name_score + 0.3 * desc_score

                if combined_score >= threshold:
                    results.append((place, combined_score))

            results.sort(key=lambda x: x[1], reverse=True)
            places = [item[0] for item in results]
        else:
            places = all_places

        if not places:
            return Response({'message': 'No matching places found.'}, status=status.HTTP_200_OK)

        serializer = TouristPlaceSerializer(places, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
