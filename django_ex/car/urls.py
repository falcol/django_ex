from django.urls import path
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'cars', views.ListCreateCarView, basename='car')
router.register(r'cars', views.UpdateDeleteCarView, basename='car')

urlpatterns = [
    path('cars', views.ListCreateCarView.as_view()),
    path('cars/<int:pk>', views.UpdateDeleteCarView.as_view()),
]
