from abc import ABC
import subprocess

from .abstract_controller import Controller


class UnusedImportsController(Controller, ABC):
    def compute_risk_factor(self, repo: dict, repo_path: str) -> int:
        commands = [f'cd {repo_path}', 'pip-extra-reqs .']
        unused_imports_raw = subprocess.run(';'.join(commands), capture_output=True, text=True, shell=True).stderr
        return len(unused_imports_raw.split('\n')) - 2
