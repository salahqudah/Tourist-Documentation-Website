from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from ..serializers.login_serializer import CustomTokenObtainPairSerializer
from drf_yasg.utils import swagger_auto_schema 
from drf_yasg import openapi

class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(request_body=CustomTokenObtainPairSerializer)
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)