from django.urls import path

from .views import HomePageView

urlpatterns = [
    path("users/", HomePageView.as_view(), name="homepage"),
]