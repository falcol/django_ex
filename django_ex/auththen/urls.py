from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from auththen import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('login/', views.MyObtainTokenPairView.as_view(), name='authen'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('profile/', views.ExampleView.as_view(), name='auth_example'),
]

urlpatterns = format_suffix_patterns(urlpatterns)