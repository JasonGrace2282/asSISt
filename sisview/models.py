from __future__ import annotations

from django.conf import settings
from django.db import models

__all__ = ["Subject", "Weight"]


class Weight(models.Model):
    """A dataclass storing info about a category of a grade

    i.e. if the gradebook was split into Formative/Sumative,
    then Formative/Sumative would be instances of this class.

    Parameters
    ----------
        points
            How many points the student got in the category
        points_possible
            How many points were possible to be earned in the category
        percent
            Weighting of final grade on a scale of 0-1
        name
            Name of the category, i.e. Formative
    """

    points = models.FloatField()
    points_possible = models.FloatField()
    percent = models.FloatField()
    name = models.TextField(default="Cumulative")
    subject = models.ForeignKey("Subject", on_delete=models.CASCADE, related_name="weights")

    def __str__(self) -> str:
        return str(self.name)

    def get_status(self) -> str:
        points = (
            int(self.points)  # type: ignore
            if float(self.points).is_integer()  # type: ignore
            else float(self.points)  # type: ignore
        )
        points_possible = (
            int(self.points_possible)  # type: ignore
            if float(self.points_possible).is_integer()  # type: ignore
            else float(self.points_possible)  # type: ignore
        )
        return f"{points} / {points_possible}"


class Subject(models.Model):
    """A Subject (i.e. English or Math)

    Parameters
    ----------
        name
            Name of the subject
        weights
            The different categories of weights in the subject.
            For example, Red Points, Blue Points and Green Points
            or Formative and Summative

    Properties
    ----------
        final_grade
            Calculate the final grade based off of the weights
    """

    name = models.TextField()
    account = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="subjects",
    )

    def __str__(self) -> str:
        return str(self.name)

    def get_final_grade(
        self,
        category_sims: dict[str, list[tuple[float, float]]],
    ) -> float:
        # populate with simulated assignments
        divisor = 0
        grade = 0
        for weight in self.weights.all():  # type: ignore
            divisor += weight.percent

            new_points = weight.points
            new_points_possible = weight.points_possible

            inputs = category_sims[weight.name] if weight.name in category_sims else ()

            for points, possible in inputs:
                new_points += points
                new_points_possible += possible

            grade += (new_points / new_points_possible) * weight.percent
        return round(grade * 100, 2) if not grade.is_integer() else grade * 100
