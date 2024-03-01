from studentvue import StudentVue
from backend.classes import Account, Subject, Weight
from collections import OrderedDict


def login(username: str, password: str, domain: str) -> Account:
    account = check_account_success(username, password, domain)
    # convert courses to list of Subjects
    courses = account["Courses"]["Course"]
    for idx, _ in enumerate(courses):
        courses[idx] = parse_subjects(account, idx)
    account = Account(
        username,
        courses
    )
    return account


def check_account_success(
        username: str,
        password: str,
        domain: str
        ) -> OrderedDict:
    try:
        return StudentVue(
            username,
            password,
            domain
        ).get_gradebook()["Gradebook"]
    except Exception as e:
        raise RuntimeError("Oops, an error occurred with logging in") from e


def parse_class(
    weight: dict,
    weights: list[Weight],
    name: str
) -> Subject | None:
    if weight["@Type"] == "TOTAL":
        return Subject(name, weights)

    points = weight["@Points"]
    total_points = weight["@PointsPossible"]
    weights.append(
        Weight(
            percent=int(weight["@Weight"][:-1])/100,  # PERCENT weightage
            points=points,
            points_possible=total_points,
            name=weight["@Type"]
        )
    )


def parse_unweighted(assignments: list[dict], subject: Subject) -> None:
    if not isinstance(assignments, list):
        assignments = [assignments]
    for assign in assignments:
        if (
            "Points Possible" in assign["@Points"]
            or "Not For Grading" in assign["@NOTES"]
        ):
            continue
        points, possible_points = map(
            float,
            # parse stuff of form "3 / 4"
            assign["@Points"].replace(" ", "").split("/")
        )
        # Since it's unweighted it can be represented as a weight
        # with percent=1
        # So there is only one weight, hence weights[0]
        subject.weights[0].points += points
        subject.weights[0].points_possible += possible_points


def parse_subjects(
    subjects: dict[str, dict[str, dict]],
    course_idx: int
) -> Subject:
    courses = subjects["Courses"]["Course"][course_idx]
    marks = courses["Marks"]["Mark"]
    grading_scheme = marks["GradeCalculationSummary"]

    if grading_scheme:
        weights = []
        for weight in grading_scheme["AssignmentGradeCalc"]:
            # modify weights, if the total is reached return a Subject
            tmp = parse_class(weight, weights, courses["@Title"])
            if isinstance(tmp, Subject):
                return tmp
        raise RuntimeError("Invalid Output from API")

    # otherwise it isn't weighted
    subject = Subject(courses["@Title"], [Weight(0, 0, 1)])
    # exit(1)
    parse_unweighted(
        marks["Assignments"]["Assignment"],  # type: ignore
        subject
    )
    return subject
