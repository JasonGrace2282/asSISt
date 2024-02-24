from dataclasses import dataclass, default_factory


__all__ = [
    "Subject",
    "Account"
]


@dataclass
class Weighting:
    is_weighted: bool
    weighting: dict = default_factory(dict)


@dataclass
class Subject:
    points: float
    points_possible: float
    weighting: Weighting


@dataclass
class Account:
    name: str
    subjects: list[Subject]
