"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from accounts.views import *
from main.views import *
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView, TokenVerifyView, TokenBlacklistView
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('admin/', admin.site.urls),

    path("v1/user/register/", RegisterAPIView.as_view()),  # post - 회원가입
    path("sv1/user/auth/", UserLoginAPI.as_view()),
    # post - 로그인, delete - 로그아웃, get - 유저정보
    path("v1/", include("api.urls")),

    # JWT Token auth
    path('v1/auth/', TokenObtainPairView.as_view()),
    path('v1/auth/refresh/', TokenRefreshView.as_view()),
    path('v1/auth/verify/', TokenVerifyView.as_view()),
    path('v1/auth/logout/', TokenBlacklistView.as_view()),

    # path('main', main_page, name="main"),
    # path('main/team', team_page, name="team"),

    # path('api/v1/token/', obtain_jwt_token),
    # path('api/v1/token/refresh/', refresh_jwt_token),
    # path('api/v1/token/verify/', verify_jwt_token),∑
    ]
