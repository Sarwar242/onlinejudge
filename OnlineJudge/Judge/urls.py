
from django.urls import path

from Judge import views

urlpatterns = [
    path('', views.index, name='index'),
]
