from abc import ABC
from dynaconf import settings
import subprocess

from .abstract_controller import Controller

SEVERITY_TO_SCORE_MULTIPLIER = {severity.upper(): multiplier for severity, multiplier in
                                settings.CONTROLLERS.BANDIT.SEVERITY_TO_SCORE_MULTIPLIER.to_dict().items()}

METRICS_KEYWORD_IN_BANDIT_SUMMARY = 'metrics'


class BanditSASTController(Controller, ABC):
    def __init__(self):
        super().__init__('bandit_sast')

    @staticmethod
    def _extract_metrics_from_raw_section(raw_metrics_section: str) -> dict:
        metrics = {}
        raw_lines = [raw_line.replace(' ', '').replace('\t', '') for raw_line in raw_metrics_section.split('\n')[2:6]]
        for raw_line in raw_lines:
            severity, amount = raw_line.split(':')
            metrics[severity] = float(amount)
        return metrics

    def _compute_risk_factor(self, repo: dict, repo_path: str) -> int:
        command = f'bandit -r {repo_path}'
        bandit_summary = subprocess.run(command, capture_output=True, text=True, shell=True).stdout
        bandit_summary_partitioned = bandit_summary.split('\n\n')
        raw_metrics_section = next((section for section in bandit_summary_partitioned
                                    if METRICS_KEYWORD_IN_BANDIT_SUMMARY in section), None)
        if not raw_metrics_section:
            return 0
        metrics = BanditSASTController._extract_metrics_from_raw_section(raw_metrics_section)
        score = sum([int(amount * SEVERITY_TO_SCORE_MULTIPLIER.get(severity.upper(), 1))
                     for severity, amount in metrics.items()])
        return score
