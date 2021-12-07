from abc import ABC, abstractmethod


class Controller(ABC):
    @abstractmethod
    def compute_risk_factor(self, repo: dict) -> int:
        pass
