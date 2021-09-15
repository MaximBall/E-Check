from django.urls import path

from .views import UserDetailView

urlpatterns = [
    path("users/", UserDetailView.as_view(), name="homepage"),
]