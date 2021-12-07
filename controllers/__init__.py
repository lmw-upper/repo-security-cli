from typing import List

from .abstract_controller import Controller
from .unused_imports_controller import UnusedImportsController

controllers: List[Controller] = [UnusedImportsController()]


def get_final_risk_score(repo: dict):
    score_sum = 0
    for controller in controllers:
        score = controller.compute_risk_factor(repo)
        score_sum += score
    return int(score_sum / len(controllers))
