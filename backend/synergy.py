from studentvue import StudentVue
from backend.classes import Account, Subject


def login(username: str, password: str, domain: str) -> None:
    account = check_account_success(username, password, domain)
    courses = account["Courses"]["Course"]
    for idx, course in enumerate(courses):
        courses[idx] = parse_subjects(course)
    account = Account(
        username,
        courses
    )


def check_account_success(username: str, password: str, domain: str) -> StudentVue:
    # TODO: Add error checking
    return StudentVue(username, password, domain)


def parse_subjects(subjects: dict[str, list[dict]]) -> Subject:
    marks = subjects["Marks"]
    grading_scheme = marks["Mark"]["GradeCalculationSummary"]
    for weight in grading_scheme["AssignmentGradeCalc"]:
        if weight["@Type"] == "TOTAL":
            points = weight["@Points"]
            total_points = weight["@PointsPossible"]
            return Subject(points, total_points)
    raise ValueError("Something went wrong?")
