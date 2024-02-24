from backend.classes import SimulatedAssignment, Subject


def calculate(sub: Subject, *simulations: SimulatedAssignment) -> None:
    for sim in simulations:
        assignment_weight = sim.assignment_weight
        for idx, weight in enumerate(sub.weights):
            if weight.name == assignment_weight.name:
                weights = sub.weights[idx]
                weights.points += assignment_weight.points
                weights.points_possible += assignment_weight.points_possible
