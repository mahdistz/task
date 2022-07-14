from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import Users
from user.serializers import RegisterSerializer
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from django.views.generic import TemplateView


# class GoogleLogin(SocialLoginView):
#     adapter_class = GoogleOAuth2Adapter
#
#     def post(self, request, *args, **kwargs):
#         response = super(GoogleLogin, self).post(request, *args, **kwargs)
#         token = Token.objects.get(key=response.data['key'])
#         return Response({'token': token.key, 'id': token.user_id})

class Home(TemplateView):
    template_name = "home.html"


class Login(TemplateView):
    template_name = "login.html"


class Register(TemplateView):
    template_name = "register.html"


class GoogleLogin(SocialLoginView):  # if you want to use Authorization Code Grant, use this
    adapter_class = GoogleOAuth2Adapter
    callback_url = 'http://127.0.0.1:8000/accounts/google/login/callback/'
    client_class = OAuth2Client


class GitHubLogin(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter
    callback_url = 'http://127.0.0.1:8000/accounts/github/login/callback'
    client_class = OAuth2Client


# Create your views here.
class RegisterView(CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class UserDetailView(RetrieveUpdateAPIView):
    queryset = Users.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [IsAuthenticated]
