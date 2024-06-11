from __future__ import annotations

from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy

from .views import AssistLoginView

urlpatterns = [
    path("login/", AssistLoginView.as_view(), name="login-page"),
    path(
        "logout/",
        LogoutView.as_view(next_page=reverse_lazy("login-page")),
        name="logout",
    ),
]
