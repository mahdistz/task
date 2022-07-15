from django.urls import path
from user.views import UserRegistrationView, UserDetailView, Login
from django.contrib.auth import views as auth


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', auth.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('detail/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]
