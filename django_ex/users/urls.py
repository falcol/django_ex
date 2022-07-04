from django.urls import path

from users import views

urlpatterns = [
    path('', views.ListUsers.as_view()),
    path('token', views.CustomAuthToken.as_view())
]
