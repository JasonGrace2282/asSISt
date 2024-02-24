from studentvue import StudentVue
from backend.classes import Account, Subject, Weighting, Weight


def login(username: str, password: str, domain: str) -> Account:
    account = check_account_success(username, password, domain)
    # convert courses to list of Subjects
    courses = account["Courses"]["Course"]  # type: ignore
    for idx, course in enumerate(courses):
        courses[idx] = parse_subjects(course)
    account = Account(
        username,
        courses
    )
    return account


def check_account_success(
        username: str,
        password: str,
        domain: str
        ) -> StudentVue:
    try:
        return StudentVue(username, password, domain)
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
        points, possible_points = map(
            int,
            # parse stuff of form "3 / 4"
            assign["@Points"].replace(" ", "").split("/")
        )
        subject.points += points
        subject.points_possible = possible_points
        subject.final_grade = subject.points / subject.points_possible


def parse_subjects(subjects: dict[str, list[dict]]) -> Subject:
    marks = subjects["Marks"]
    grading_scheme = marks["Mark"]["GradeCalculationSummary"]  # type: ignore
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
            subjects["Assignments"]["Assignment"],  # type: ignore
            subject
        )
    raise ValueError("Something went wrong?")
