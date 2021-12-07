import os
import shutil
from git import Repo, GitCommandError
from gtrending import fetch_repos
from typing import List

BASE_DIR = 'repos'

PACKAGES_LANGUAGE = 'python'
TRENDING_PERIOD = 'daily'

shutil.rmtree(BASE_DIR, ignore_errors=True)
os.mkdir(BASE_DIR)


def get_most_trending_repos(number_of_repos: int) -> List[dict]:
    repos = sorted(fetch_repos(language=PACKAGES_LANGUAGE, since=TRENDING_PERIOD), key=lambda r: r['stars'])
    return repos[:number_of_repos]


def clone_repo(repo_name: str, repo_url: str) -> str:
    repo_path = os.path.join(BASE_DIR, repo_name)
    Repo.clone_from(repo_url, repo_path)
    return repo_path
