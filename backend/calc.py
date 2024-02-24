from backend.classes import SimulatedAssignment, Subject


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
