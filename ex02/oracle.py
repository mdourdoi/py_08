import os


class ConfigError(Exception):
    pass


def get_variable(name: str) -> str | None:
    value = os.gentenv(str(name))
    if value is None:
        raise ConfigError(f'{value} is missing in you environment')
    return value


def main() -> None:
    from dotenv import load_dotenv

    load_dotenv(override=False)
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
        except Exception as cur_error:
            print(f'Error: {cur_error}')
            return
        if not temp:
            return
        variables[value] = temp
    