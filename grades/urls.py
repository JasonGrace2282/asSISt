from django.urls import path
from .views import CalcGrades

urlpatterns = [
    path("grades/", CalcGrades.as_view(), name='grades')
]
