from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import UserSerializer


class LoginView(ObtainAuthToken):
    serializer_class = UserSerializer
    