# About

Correlation-Matrix-Script is a Python 3 script which performs a correlation metric
on expression data. The output is a correlation matrix (or similarity matrix)
in the form of a tab separated text file.

### Prerequisites

The user will need Python 3 installed to run this script. The latest version of Python 3
can be downloaded at the following url:

```
https://www.python.org/downloads/
```

The following python modules are required for use as well:

```
scikit-learn
numpy
pandas
argparse
```

### Installing

After requisite Python version and modules have been installed,
then paste the following into your shell.

```
git clone https://github.com/jambqc/Correlation-Matrix-Script
```

### Example 
An example expression matrix has been provided called:
example_expression_data.tsv  
To perform a Pearson correlation metric on this data, run the following command:

```
./correlation_metric_script.py example_expression_data.tsv Pearson
```

