from studentvue import StudentVue
from backend.classes import Account, Subject, Weighting, Weight
from collections import OrderedDict


def login(username: str, password: str, domain: str) -> Account:
    account = check_account_success(username, password, domain)
    # convert courses to list of Subjects
    courses = account["Courses"]["Course"]
    for idx, course in enumerate(courses):
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


def parse_class(weight, weights: Weighting) -> Subject | None:
    points = weight["@Points"]
    total_points = weight["@PointsPossible"]
    if weight["@Type"] == "TOTAL":
        return Subject(
            points,
            total_points,
            final_grade=points/total_points,
            weighting=weights
        )

    weights.weighting[weight["@Type"]] = Weight(
        weight["@Weight"],
        points,
        total_points
    )
    return None


def parse_unweighted(assignments: list[dict], subject: Subject) -> None:
    for assign in assignments:
        if "Points Possible" in assign["@Points"]:
            continue
        points, possible_points = map(
            int,
            # parse stuff of form "3 / 4"
            assign["@Points"].replace(" ", "").split("/")
        )
        subject.points += points
        subject.points_possible = possible_points
        subject.final_grade = subject.points / subject.points_possible


def parse_subjects(subjects: dict[str, dict[str, dict]], course_idx: int) -> Subject:
    courses = subjects["Courses"]["Course"][course_idx]
    marks = courses["Marks"]["Mark"]
    grading_scheme = marks["GradeCalculationSummary"]
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
        subject = Subject(0, 0, Weighting(is_weighted=False), 0)
        parse_unweighted(
            marks["Assignments"]["Assignment"],  # type: ignore
            subject
        )
        return subject
    raise ValueError("Something went wrong?")

def parse_
