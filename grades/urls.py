from __future__ import annotations

from django.urls import path

from .views import CalcGrades

urlpatterns = [path("<int:course_id>/grades/", CalcGrades.as_view(), name="grades")]
