from __future__ import annotations

from copy import deepcopy

from .classes import SimulatedAssignment, Subject


def simulate_assignments(sub: Subject, *simulations: SimulatedAssignment) -> None:
    for sim in simulations:
        for idx, weight in enumerate(sub.weights):
            if (
                weight.name == sim.name
                and sim.points is not None
                and sim.points_possible is not None
            ):
                weights = sub.weights[idx]
                weights.points += sim.points
                weights.points_possible += sim.points_possible


def calc_final_grade(sub: Subject, *sims: SimulatedAssignment) -> float:
    subject_copy = deepcopy(sub)
    simulate_assignments(subject_copy, *(x for x in sims if x))
    return subject_copy.final_grade


def finals_grade_recalc(
    final_grade: float, finals_points: float, weighting: tuple[float, float]
) -> float:
    """Recalculates the grades from the finals

    Final grade comes form `calc_final_grade`.
    `finals_points` is the percent they got on their midterm/final.
    Weighting is the ratio of the rating of the final grade to the weighting of the final exam
    """
    # assert sum(weighting) == 1
    # weighting is the ratio of final grade to final exam grade
    if finals_points == "":
        return final_grade
    return final_grade * weighting[0] + finals_points * weighting[1]
