from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from ..serializers.login_serializer import CustomTokenObtainPairSerializer

class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    permission_classes = [AllowAny]
