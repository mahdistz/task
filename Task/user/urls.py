from django.urls import path
from user.views import RegisterView, UserDetailView, Login, Register

urlpatterns = [

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('new-register/', Register.as_view(), name='new-register'),
    path('detail/<int:pk>/', UserDetailView.as_view(), name='user-detail'),

]
