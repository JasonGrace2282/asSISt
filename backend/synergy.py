from studentvue import StudentVue
from backend.classes import Account, Subject, Weighting, Weight


def login(username: str, password: str, domain: str) -> None:
    account = check_account_success(username, password, domain)
    courses = account["Courses"]["Course"]
    for idx, course in enumerate(courses):
        courses[idx] = parse_subjects(course)
    account = Account(
        username,
        courses
    )


def check_account_success(
        username: str,
        password: str,
        domain: str
        ) -> StudentVue:
    # TODO: Add error checking
    return StudentVue(username, password, domain)


def parse_class(weight, weights: Weighting) -> Subject | None:
    points = weight["@Points"]
    total_points = weight["@PointsPossible"]
    if weight["@Type"] == "TOTAL":
        return Subject(points, total_points, weighting=weights)

    weights.weighting[weight["@Type"]] = Weight(
        weight["@Weight"],
        points,
        total_points
    )
    return None


def parse_subjects(subjects: dict[str, list[dict]]) -> Subject:
    marks = subjects["Marks"]
    grading_scheme = marks["Mark"]["GradeCalculationSummary"]
    # if it's weighted
    if grading_scheme:
        weights = Weighting(is_weighted=True)
        for weight in grading_scheme["AssignmentGradeCalc"]:
            # modify weights, if the total is reached return a Subject
            tmp = parse_class(weight, weights)
            if isinstance(tmp, Subject):
                return tmp
    else:
        # not weighted, todo
        pass
    raise ValueError("Something went wrong?")

def parse_
