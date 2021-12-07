import subprocess
from abc import ABC

from .abstract_controller import Controller
from adapters import git_adapter


class UnusedImportsController(Controller, ABC):
    def compute_risk_factor(self, repo: dict) -> int:
        repo_path = git_adapter.clone_repo(repo['name'], repo['url'])
        commands = [f'cd {repo_path}', 'pip-extra-reqs .']
        unused_imports_raw = subprocess.run(';'.join(commands), capture_output=True, text=True, shell=True).stderr
        return len(unused_imports_raw.split('\n')) - 2
