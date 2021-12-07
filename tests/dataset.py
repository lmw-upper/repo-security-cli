import os

BASE_REPO_DIR = 'tests/test_repos'


def get_repo_path(name: str) -> str:
    return os.path.join(BASE_REPO_DIR, name)
