import sys
import os
import site


def main() -> None:
    in_venv = (sys.prefix != sys.base_prefix)
    print()
    print('MATRIX STATUS: ', end='')
    print('Welcome to the construct' if in_venv else "You're still plugged in")
    print()
    print('Current Python:', sys.executable)
    print('Virtual Environment:', os.path.basename(
        os.environ.get("VIRTUAL_ENV")) if in_venv else 'None detected')
    if in_venv:
        print('Environment Path:', sys.prefix)
        print()
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system.")
        print()
        print("Package installation path:")
        print(site.getsitepackages()[0])
        return
    print()
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print()
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env")
    print("Scripts")
    print("activate # On Windows")
    print()
    print("Then run this program again.")


if __name__ == "__main__":
    try:
        main()
    except Exception as cur_error:
        print(f'Error during execution: {cur_error}')
