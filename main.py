import click
from click_shell import shell

from adapters import git_adapter
from controllers import get_final_risk_score


@shell(prompt='>', intro='Starting my app...')
def my_app():
    pass


@my_app.command(name='repo_info')
@click.option('--n', default=1, help='Number of repos to fetch.')
def repo_info(n):
    repos = git_adapter.get_most_trending_repos(n)
    for repo in repos:
        score = get_final_risk_score(repo)
        click.echo(f'{repo}{score}')


def main():
    while True:
        my_app()


if __name__ == '__main__':
    main()
