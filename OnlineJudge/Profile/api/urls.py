from django.contrib import admin
from django.urls import path, include
from .views import (
    ProfileListSearchAPIView,
    ProfileCreateAPIView,
    ProfileDetailAPIView,
    ProfileUpdateAPIView,
    ProfileDeleteAPIView,
) 


urlpatterns = [
    path('',ProfileListSearchAPIView.as_view()),
    path('create/',ProfileCreateAPIView.as_view()),
    path('<id>/',ProfileDetailAPIView.as_view()),
    path('<id>/update/',ProfileUpdateAPIView.as_view()),
    path('<id>/delete/',ProfileDeleteAPIView.as_view()),
]

