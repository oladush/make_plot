# Plotting Script

This script allows you to generate a line plot from a data file. The data file should have an `x` column and other columns that represent the corresponding `y` values. You can customize the plot's appearance, labels, and output file.

## Features

- Parse data from a file where the first line contains column headers.
- Plot multiple `y` values against a single `x` axis.
- Customize plot labels, title, and appearance.
- Save the plot to an output file.
- Optionally, display the plot interactively.

## Requirements

- Python 3.x
- `matplotlib` library for plotting

To install the required Python package, run:

```bash
pip install matplotlib
```

## Input File Format
The script expects a plain text file where:
- The first line contains space-separated column headers. One of the columns must be labeled x.
- Subsequent lines contain numerical values corresponding to the columns.

### Example input file (data.txt):
```
x column1 column2 column3
0 1.0 2.0 3.0
1 1.1 2.1 3.1
2 1.2 2.2 3.2
```

## Usage
### Command-Line Arguments
```
python make_plot.py [OPTIONS]
```
```
-i, --input: Path to the input data file (required).
-o, --output: Path to the output image file (optional). If not provided, the plot will not be saved.
-t, --title: Title of the plot (optional, default: 'Plot').
-x, --x_label: Label for the x-axis (optional, default: 'x').
-y, --y_label: Label for the y-axis (optional, default: 'y').
--no-show: Prevent the plot from being shown interactively (optional). If not specified, the plot will be displayed by default.
```

### Example
To generate a plot from `data.txt`, display it interactively, and save it as `output.png`:
```
python plot_script.py -i data.txt -o output.png
```

To generate a plot with custom labels and title:
```
python plot_script.py -i data.txt -t "Custom Title" -x "Time (s)" -y "Value"
```



