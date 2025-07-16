from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers.register_serializer import RegisterSerializer
from ..serializers.user_profile_serializer import UserProfileSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg.utils import swagger_auto_schema 

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class RegisterView(APIView):
    @swagger_auto_schema(request_body=RegisterSerializer) 
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'user': UserProfileSerializer(user).data,
                'tokens': get_tokens_for_user(user)
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)