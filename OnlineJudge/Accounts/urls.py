from django.contrib import admin
from django.urls import path,include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from .views import AuthAPIView, RegisterAPIView

urlpatterns = [
    path('', AuthAPIView.as_view()),
    path('register/', RegisterAPIView.as_view()),
    path('refresh/', refresh_jwt_token),
]
