from __future__ import annotations

from collections import OrderedDict

from studentvue import StudentVue

from .models import Subject


class LoginError(Exception):
    pass


class ApiError(Exception):
    pass


def login(username: str, password: str, domain: str, user):
    gradebook = check_account_success(username, password, domain)
    if isinstance(gradebook, str):
        raise LoginError(gradebook)

    if user.subjects.exists():
        user.subjects.all().delete()

    for course in gradebook["Courses"]["Course"]:
        parse_subject(course, user)


def check_account_success(username: str, password: str, domain: str) -> OrderedDict:
    try:
        gradebook = StudentVue(username, password, domain).get_gradebook()
        if gradebook.get("RT_ERROR"):
            return gradebook["RT_ERROR"]["@ERROR_MESSAGE"]
        return gradebook["Gradebook"]
    except KeyError as e:
        raise LoginError("Oops, an error occurred with logging in. Incorrect Credentials?") from e


def parse_class(
    weight: dict,
    subject: Subject,
) -> int:
    if weight["@Type"] == "TOTAL":
        return 0

    category = subject.weights.create(
        name=weight["@Type"],
        points=weight["@Points"],
        points_possible=weight["@PointsPossible"],
        percent=int(weight["@Weight"][:-1]) / 100,  # PERCENT weightage
    )
    category.save()
    return -1  # continue adding weights


def parse_unweighted(assignments: list[dict]) -> tuple[float, float]:
    if not isinstance(assignments, list):
        # this happens if there is only one assignment
        # in the gradebook
        assignments = [assignments]

    points_earned = points_possible = 0
    for assign in assignments:
        if (
            "points possible" in assign["@Points"].lower()
            or "not for grading" in assign["@Notes"].lower()
        ):
            continue

        points, possible_points = map(
            float,
            # parse stuff of form "3 / 4"
            assign["@Points"].replace(" ", "").split("/"),
        )
        # Since it's unweighted it can be represented as a weight
        # with percent=1
        # So there is only one weight
        points_earned += points
        points_possible += possible_points

    return points_earned, points_possible


def parse_subject(
    courses,  # trying to typehint this is hell
    account,
) -> None:
    marks = courses["Marks"]["Mark"][0]
    grading_scheme = marks["GradeCalculationSummary"]

    subject = account.subjects.create(name=courses["@Title"])
    subject.save()

    if grading_scheme:
        for weight in grading_scheme["AssignmentGradeCalc"]:
            # modify weights, if the total is reached it returns a Subject
            tmp = parse_class(weight, subject)
            if tmp != -1:
                # found total
                return
        raise ApiError("Invalid Output from API")

    # otherwise it isn't weighted
    points, points_possible = parse_unweighted(
        marks["Assignments"]["Assignment"],  # type: ignore
    )
    weight = subject.weights.create(points=points, points_possible=points_possible, percent=1)
    weight.save()
