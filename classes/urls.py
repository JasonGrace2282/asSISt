from __future__ import annotations

from django.urls import path

from .views import ChooseClasses, LoadingScreen

urlpatterns = [
    path("", ChooseClasses.as_view(), name="choose-classes"),
    path("loading", LoadingScreen.as_view(), name="loading"),
]
