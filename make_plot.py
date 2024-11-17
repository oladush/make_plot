import sys
import argparse
import matplotlib.pyplot as plt

LINES_PARAMS = (
    {'marker': 'o', 'linestyle': '-', 'color': 'blue'},
    {'marker': 'x', 'linestyle': '--', 'color': 'red'},
    {'marker': 'o', 'linestyle': '-', 'color': 'green'},
    {'marker': 'x', 'linestyle': '--', 'color': 'cyan'},
    {'marker': '^', 'linestyle': '-', 'color': 'magenta'},
    {'marker': 's', 'linestyle': '--', 'color': 'orange'},
    {'marker': 'D', 'linestyle': '-.', 'color': 'purple'},
    {'marker': 'p', 'linestyle': '-', 'color': 'brown'},
    {'marker': '*', 'linestyle': ':', 'color': 'black'},
    {'marker': 'v', 'linestyle': '--', 'color': 'gray'},
    {'marker': 'H', 'linestyle': '-', 'color': 'pink'},
    {'marker': 'h', 'linestyle': '-.', 'color': 'lime'},
)

IGNORE_LABELS = ['diff']
PLOT_PARAMS = {'figsize': (8, 6)}
PLOT_GRID = {'visible': True, 'alpha': 0.5}
PLOT_X_LABEL = 'x'
PLOT_Y_LABEL = 'y'
PLOT_TITLE = 'Plot'


def parse_data(filename: str) -> tuple[list[float], list[tuple[str, list]]]:
    header = None
    table = {}

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('x'):
                header = line.split()
                for header_label in header:
                    table[header_label] = []

            elif header is not None:
                values = line.split()
                for i in range(len(header)):
                    table[header[i]].append(float(values[i]))

    x_values = table.get('x', [])

    if not x_values:
        raise ValueError('No x-values in the input file')
    print(f'[+] Got x_values(length: {len(x_values)}): {x_values}')

    functions = []

    for key in table:
        if key not in IGNORE_LABELS and key != 'x':
            print(f'[+] Got {key}(length: {len(table[key])}): {table[key]}')
            if len(table[key]) != len(x_values):
                raise ValueError(f'Length of x_values is not equal to length of {key}')

            functions.append((key, table[key]))

    return x_values, functions


def make_plot(x_values: list[float], y_series: list[tuple[str, list]], output_filename: str, need_show: bool = False):
    plt.figure(**PLOT_PARAMS)

    for i, (label, y_values) in enumerate(y_series):
        plt.plot(x_values, y_values, label=label, **LINES_PARAMS[i])

    plt.xlabel(PLOT_X_LABEL)
    plt.ylabel(PLOT_Y_LABEL)
    plt.title(PLOT_TITLE)
    plt.grid(**PLOT_GRID)

    plt.legend()

    if need_show:
        plt.show()

    if output_filename:
        plt.savefig(output_filename)
        print(f'[+] Plot saved to {output_filename}')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='Path to the input data file')
    parser.add_argument('-o', '--output', help='Path to the output file')
    parser.add_argument('-t', '--title', help='Plot title', default=PLOT_TITLE)
    parser.add_argument('-x', '--x_label', help='X-axis label', default=PLOT_X_LABEL)
    parser.add_argument('-y', '--y_label', help='Y-axis label', default=PLOT_Y_LABEL)
    parser.add_argument('--no-show', action="store_true", help="Disable showing the plot interactively")

    try:
        args = parser.parse_args()
        print(f'[*] Run script: "{sys.argv[0]} with args: {vars(args)}"')

        x, y_series = parse_data(args.input)

        make_plot(x, y_series, args.output, not args.no_show)

    except Exception as e:
        print(f'[-] Got error when making plot. Error: {e}')
        sys.exit(1)


if __name__ == '__main__':
    main()
