import importlib
import importlib.metadata
from importlib.metadata import PackageNotFoundError


def main() -> None:
    print()
    print("LOADING STATUS: Loading programs...")
    print()
    print("Checking dependencies:")
    checkers = {
        'pandas': [importlib.util.find_spec("pandas"),
                   'Data manipulation'],
        'requests': [importlib.util.find_spec("requests"),
                     'Network access'],
        'matplotlib': [importlib.util.find_spec("matplotlib"),
                       'Visualization'],
        'numpy': [importlib.util.find_spec("numpy"),
                  'Advanced calculation']}
    missing = []
    for key, value in checkers.items():
        if value[0] is None:
            print(f'[KO] Missing package: {key}')
            missing.append(key)
        else:
            try:
                version = importlib.metadata.version(key)
            except PackageNotFoundError:
                version = 'unknown version'
            print(f'[OK] {key} ({version}) - {value[1]} ready')
    if len(missing) != 0:
        print('Some dependencies are missing. You can install them with:')
        print('With the requirements.txt file:')
        print(' pip install -r requirements.txt')
        print()
        print('Without the requirements.txt file:\n pip install ', end='')
        for lib in missing:
            print(lib + ' ', end='')
        print('\n')
        print('With Poetry (must run with a terminal located at ex1 root):')
        print(' poetry install\n poetry run python loading.py')
        return
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    print()
    print('Analyzing Matrix data...')
    print('Processing 1000 data points...')
    points = np.random.normal(0, 1, 1000)
    points_df = pd.DataFrame(points, columns=['points'])
    print()
    print('Generating visualization...')
    plt.plot(points_df)
    plt.savefig("matrix_analysis.png")
    plt.show()
    print()
    print('Analysis complete!')
    print('Results saved to: matrix_analysis.png')


if __name__ == "__main__":
    main()
