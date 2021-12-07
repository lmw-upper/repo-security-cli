import os

from services import cli_service, rest_service

if __name__ == '__main__':
    if os.environ.get('SHOULD_RUN_REST', '0') == '1':
        rest_service.main()
    else:
        cli_service.main()
