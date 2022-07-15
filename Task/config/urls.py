"""Task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from user.views import Home
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
                  path("", Home.as_view(), name="home"),
                  path('admin/', admin.site.urls),
                  path('users/', include('user.urls')),
                  path("accounts/", include("allauth.urls")),
                  # rest_framework
                  path('api-auth/', include('rest_framework.urls')),
                  # dj_rest_auth with using simple_jwt
                  path('dj-rest-auth/', include('dj_rest_auth.urls')),
                  path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
                  # login with google and github
                  path('', include('social_django.urls', namespace='social')),
                  # captcha
                  path('captcha/', include("captcha.urls")),
                  # django-admin-charts
                  path('admin_tools_stats/', include('admin_tools_stats.urls')),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
