from django.urls import path

from accounts.views import CreateUserView

urlpatterns = [path("accounts/", CreateUserView.as_view())]
