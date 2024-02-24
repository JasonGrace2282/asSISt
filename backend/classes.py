from dataclasses import dataclass


__all__ = [
    "Assignment",
    "Subject",
    "Account"
]


@dataclass
class Assignment:
    points: int
    possible_points: int
    graded: bool


@dataclass
class Subject:
    grades: list[Assignment]


@dataclass
class Account:
    name: str
    subjects: list[Subject]
