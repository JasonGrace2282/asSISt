from dataclasses import dataclass
from customtkinter import CTkEntry  # TODO: Change to django object


__all__ = [
    "Subject",
    "Account",
    "SimulatedAssignment",
    "Weight"
]


def pcall(f, *args, **kwargs):
    """Protected call: on failure returns ``None``"""
    try:
        return f(*args, **kwargs)
    except Exception:
        pass


@dataclass(slots=True)
class Weight:
    """A dataclass storing info about
    a category of a grade

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
    points: float
    points_possible: float
    percent: float
    name: str = "Cumulative"


@dataclass(slots=True)
class SimulatedAssignment:
    """An assignment that hasn't actually happened yet.
    This is an assignment the end user inputs into the application
    """
    expr: CTkEntry
    name: str

    @property
    def points(self):
        return pcall(float, self.expr.get().split("/")[0])

    @property
    def points_possible(self):
        return pcall(float, self.expr.get().split("/")[1])


@dataclass(slots=True)
class Subject:
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
    name: str
    weights: list[Weight]

    @property
    def final_grade(self) -> float:
        return sum(
            (weight.points / weight.points_possible) * weight.percent
            for weight in self.weights
        ) / sum(
            weight.percent
            for weight in self.weights
        )


@dataclass(slots=True)
class Account:
    """A user account.
    """
    name: str
    subjects: list[Subject]

    def json_serialize(self):
        return self.__dict__
