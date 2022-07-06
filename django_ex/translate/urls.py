from django.urls import path
from translate import views

app_name = 'translate'
urlpatterns = [
    path('', views.index, name='index'),
    path('trans/', views.TranslateAPIView.as_view(), name='translate'),
]
