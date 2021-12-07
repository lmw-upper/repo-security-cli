from abc import ABC, abstractmethod
import sys
from typing import Optional


class Controller(ABC):
    def __init__(self, name: Optional[str] = None):
        self.name = name

    @abstractmethod
    def _compute_risk_factor(self, repo: dict, repo_path: str) -> int:
        pass

    def compute_risk_factor(self, repo: dict, repo_path: str) -> int:
        try:
            return self._compute_risk_factor(repo, repo_path)
        except Exception:
            print('Failed getting risk factor from controller', self.name, 'on repo', repo['name'],
                  file=sys.stderr)
            return 0
