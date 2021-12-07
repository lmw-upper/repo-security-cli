from unittest import TestCase
from unittest.mock import patch
from controllers import UnusedImportsController, BanditSASTController

from tests.dataset import get_repo_path


class TestUnusedImportsController(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.controller = UnusedImportsController()

    def test_no_problem_repo(self):
        score = self.controller.compute_risk_factor({}, get_repo_path('bandit'))
        self.assertEqual(0, score)

    def test_repo_with_problem(self):
        score = self.controller.compute_risk_factor({}, get_repo_path('unused_imports'))
        self.assertGreater(score, 0)


class TestBanditSASTController(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.controller = BanditSASTController()

    def test_no_problem_repo(self):
        score = self.controller.compute_risk_factor({}, get_repo_path('unused_imports'))
        self.assertEqual(0, score)

    def test_repo_with_problem(self):
        score = self.controller.compute_risk_factor({}, get_repo_path('bandit'))
        self.assertGreater(score, 0)
