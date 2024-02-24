from dataclasses import dataclass, field


__all__ = [
    "Subject",
    "Account"
]


@dataclass
class Weighting:
    is_weighted: bool
    weighting: dict = field(default_factory=dict)


@dataclass
class SimulatedAssignment:
    points: float
    percent: float
    weighting: Weighting


@dataclass
class Subject:
    points: float
    points_possible: float
    weighting: Weighting


@dataclass
class Account:
    name: str
    subjects: list[Subject]
