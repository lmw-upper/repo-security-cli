from typing import List

from .abstract_controller import Controller
from .unused_imports_controller import UnusedImportsController
from .bandit_sast_controller import BanditSASTController
from adapters import git_adapter

controllers: List[Controller] = [UnusedImportsController(), BanditSASTController()]


def get_final_risk_score(repo: dict):
    repo_path = git_adapter.clone_repo(repo['name'], repo['url'])
    score = sum([controller.compute_risk_factor(repo, repo_path) for controller in controllers])
    return score


def fetch_repos_security_scores(number_of_repos: int):
    repos = git_adapter.get_most_trending_repos(number_of_repos)
    for repo in repos:
        score = get_final_risk_score(repo)
        yield repo['name'], score
