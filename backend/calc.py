from backend.classes import SimulatedAssignment, Subject
from copy import deepcopy


def simulate_assignments(
    sub: Subject,
    *simulations: SimulatedAssignment
) -> None:
    for sim in simulations:
        for idx, weight in enumerate(sub.weights):
            if weight.name == sim.name:
                weights = sub.weights[idx]
                weights.points += sim.points
                weights.points_possible += sim.points_possible


def calc_final_grade(sub: Subject, *sims: SimulatedAssignment) -> float:
    subject_copy = deepcopy(sub)
    simulate_assignments(subject_copy, *(x for x in sims if x))
    return subject_copy.final_grade
