from dataclasses import dataclass
from customtkinter import CTkEntry


__all__ = [
    "Subject",
    "Account",
    "SimulatedAssignment",
    "Weight"
]


def pcall(f, *args, **kwargs):
    try:
        return f(*args, **kwargs)
    except Exception:
        pass


@dataclass
class Weight:
    points: float
    points_possible: float
    percent: float
    name: str = "Unweighted"


@dataclass
class SimulatedAssignment:
    expr: CTkEntry
    name: str

    @property
    def points(self):
        return pcall(float, self.expr.get().split("/")[0])

    @property
    def points_possible(self):
        return pcall(float, self.expr.get().split("/")[1])


@dataclass
class Subject:
    name: str
    weights: list[Weight]

    @property
    def final_grade(self) -> float:
        return sum(
            (weight.points / weight.points_possible) * weight.percent
            for weight in self.weights
        )


@dataclass
class Account:
    name: str
    subjects: list[Subject]
