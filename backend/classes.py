from dataclasses import dataclass


__all__ = [
    "Subject",
    "Account",
    "SimulatedAssignment"
]


@dataclass
class Weight:
    points: float
    points_possible: float
    percent: float
    name: str = "Unweighted"


@dataclass
class SimulatedAssignment:
    points: float
    points_possible: float
    name: str


@dataclass
class Subject:
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
