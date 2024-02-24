from studentvue import StudentVue
from backend.classes import Account, Assignment, Subject


def login(username: str, password: str, domain: str) -> None:
    account = check_account_success(username, password, domain)
    courses = account["Courses"]["Course"]
    for course in courses:

    account = Account(
        username,
        courses
    )


def check_account_success(username: str, password: str, domain: str) -> StudentVue:
    # TODO: Add error checking
    return StudentVue(username, password, domain)


def parse_subjects(subjects: dict[str, list[dict]]) -> Subject:
    marks = subjects["Marks"]
    for weight in marks["Mark"]["GradeCalculationSummary"]["AssignmentGradeCalc"]:
        if weight["@TYPE"] == "TOTAL":
            total_points = weight["@POINTS"]
