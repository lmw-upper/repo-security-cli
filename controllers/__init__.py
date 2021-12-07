from typing import List

from .abstract_controller import Controller
from .unused_imports_controller import UnusedImportsController
from adapters import git_adapter

controllers: List[Controller] = [UnusedImportsController()]


def get_final_risk_score(repo: dict):
    score_sum = 0
    repo_path = git_adapter.clone_repo(repo['name'], repo['url'])
    for controller in controllers:
        score = controller.compute_risk_factor(repo, repo_path)
        score_sum += score
    return int(score_sum / len(controllers))
