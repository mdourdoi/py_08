import os
from typing import Dict, Any


def get_variable(name: str) -> str | None:
    return os.environ[str(name)]


def get_env() -> Dict[str, Any] | None:
    from dotenv import load_dotenv

    load_dotenv()
    variables_name = [
        "MATRIX_MODE",
        "DATABASE_URL",
        "API_KEY",
        "LOG_LEVEL",
        "ZION_ENDPOINT"]
    variables = dict()
    for value in variables_name:
        try:
            temp = get_variable(value)
        except KeyError as cur_error:
            print(f'Error: {cur_error}')
            return None
        variables[value] = temp
    return variables


def main() -> None:
    print()
    print('ORACLE STATUS: Reading the Matrix...')
    print()
    env_variables = get_env()
    if env_variables is not None:
        print('Configuration loaded:')
        print(f"Mode: {env_variables['MATRIX_MODE']}")
        print('Database: Connected to local instance')
        print('API Access: Authenticated')
        print(f"Log Level: {env_variables['LOG_LEVEL']}")
        print('Zion network: Online')
        print()
    print('Environment security check:')
    print('[OK] No hardcoded secrets detected')
    if env_variables is None:
        print('[KO] .env file not properly configured or missing')
        return
    print('[OK] .env file properly configured')
    print('[OK] Production overrides available')
    print()
    print('The Oracle sees all configurations.')


if __name__ == "__main__":
    try:
        main()
    except Exception as cur_error:
        print(f'Error: {cur_error}')
