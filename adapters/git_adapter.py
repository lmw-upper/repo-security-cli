from dynaconf import settings
from git import Repo, InvalidGitRepositoryError, NoSuchPathError
from gtrending import fetch_repos
import os
import shutil
from typing import List

BASE_DIR = 'repos'

PACKAGES_LANGUAGE = settings.GIT.PACKAGES_LANGUAGE
TRENDING_PERIOD = settings.GIT.TRENDING_PERIOD

shutil.rmtree(BASE_DIR, ignore_errors=True)
os.mkdir(BASE_DIR)


def _is_git_repo(path):
    try:
        _ = Repo(path).git_dir
        return True
    except (InvalidGitRepositoryError, NoSuchPathError):
        return False


def get_most_trending_repos(number_of_repos: int) -> List[dict]:
    repos = sorted(fetch_repos(language=PACKAGES_LANGUAGE, since=TRENDING_PERIOD), key=lambda r: r['stars'])
    return repos[:number_of_repos]


def clone_repo(repo_name: str, repo_url: str) -> str:
    repo_path = os.path.join(BASE_DIR, repo_name)
    if not _is_git_repo(repo_path):
        Repo.clone_from(repo_url, repo_path)
    return repo_path
