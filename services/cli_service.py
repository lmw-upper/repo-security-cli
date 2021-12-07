import click
from click_shell import shell

from controllers import fetch_repos_security_scores


@shell(prompt='>', intro='Starting my app...')
def my_app():
    pass


@my_app.command(name='repo_info')
@click.option('-n', default=1, help='Number of repos to fetch.')
def repo_info(number_of_repos):
    for repo_name, score in fetch_repos_security_scores(number_of_repos):
        click.echo(f'{repo_name}, {score}')


def main():
    while True:
        my_app()


if __name__ == '__main__':
    main()
