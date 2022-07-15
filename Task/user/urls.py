from django.urls import path
from user.views import UserRegistrationView, UserDetailView, Login
from django.contrib.auth import views as auth
from .views import line_chart, line_chart_json

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', auth.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('detail/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('chart/', line_chart, name='line_chart'),
    path('chartJSON/', line_chart_json, name='line_chart_json'),
]
