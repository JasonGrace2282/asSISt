from dataclasses import dataclass


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
