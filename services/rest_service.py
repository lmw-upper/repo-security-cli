from sanic import Sanic, response
from sanic_openapi import swagger_blueprint, doc

from controllers import fetch_repos_security_scores

sanic_app = Sanic('Repo Security')
sanic_app.blueprint(swagger_blueprint)


@sanic_app.get('/get_scores')
@doc.consumes(doc.Integer(name="number_of_repos"), location="query")
def get_scores(req):
    scores = {}
    number_of_repos = int(req.args.get('number_of_repos', 1))
    for repo_name, score in fetch_repos_security_scores(number_of_repos):
        scores[repo_name] = score
    return response.json(scores)


@sanic_app.get('/')
@doc.exclude(True)
def root(req):
    return response.redirect('/swagger')


def main():
    sanic_app.run(host='0.0.0.0', port=8080)


if __name__ == '__main__':
    main()
