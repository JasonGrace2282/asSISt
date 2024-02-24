#Output is list of class 
from backend.classes import Account, Weighting, SimulatedAssignment

def calculate(account: Account, *news: SimulatedAssignment):
    subjects = account.subjects
    for sub in subjects:
        if sub.weighting:
            final = 0.0
            for name, weight in sub.weighting:
                final += (weight.points / weight.points_possible) * weight.percent
            Account.Subject.final_grade = final
        else:
            Account.Subject.final_grade = Account.Subject.points / Account.Subject.points_possible
    
