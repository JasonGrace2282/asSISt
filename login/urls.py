from django.urls import path
from django.urls import reverse_lazy
from .views import AssistLoginView, LogoutView


urlpatterns = [
    path('login/', AssistLoginView.as_view(), name='login-page'),
    path("logout/", LogoutView.as_view(next_page=reverse_lazy("login-page")), name="logout")
]
