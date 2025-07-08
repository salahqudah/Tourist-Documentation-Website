from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.utils.timezone import now

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom fields to JWT
        token['email'] = user.email
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['role'] = user.role
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        # Update last login time
        self.user.last_login = now()
        self.user.save(update_fields=['last_login'])

        # Add user info to response
        data['user'] = {
            'id': str(self.user.id),
            'email': self.user.email,
            'first_name': self.user.first_name,
            'last_name': self.user.last_name,
            'role': self.user.role,
        }
        return data
