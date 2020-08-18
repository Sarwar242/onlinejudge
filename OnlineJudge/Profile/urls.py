from django.urls import path
from .views import(
    ProfileAPIView,
    ProfileAPIDetailView,
)

urlpatterns = [
    path('', ProfileAPIView.as_view()),
    path('<user>/', ProfileAPIDetailView().as_view()),
]