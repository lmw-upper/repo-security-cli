from sanic import Sanic, request, response
from sanic_openapi import swagger_blueprint

sanic_app = Sanic('Repo Security')


def main():
    sanic_app.run(host='0.0.0.0', port=8080)


if __name__ == '__main__':
    main()
