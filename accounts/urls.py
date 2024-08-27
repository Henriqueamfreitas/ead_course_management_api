from django.urls import path

from accounts.views import CreateAccountView
from rest_framework_simplejwt import views

urlpatterns = [
    path("accounts/", CreateAccountView.as_view()),
    path("login/", views.TokenObtainPairView.as_view()),
]
