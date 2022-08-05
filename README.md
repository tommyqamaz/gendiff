### Tests and linter status:

![Project-check](https://github.com/tommyqamaz/python-project-lvl2/actions/workflows/project-check.yml/badge.svg)
[![Maintainability](https://api.codeclimate.com/v1/badges/cdc4111210f3539c20be/maintainability)](https://codeclimate.com/github/tommyqamaz/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/cdc4111210f3539c20be/test_coverage)](https://codeclimate.com/github/tommyqamaz/python-project-lvl2/test_coverage)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
### Install
<code>git clone git@github.com:tommyqamaz/gendiff.git</code>

<code>pip install poetry</code>

<code>make install</code>
## Usage

### As external library

```python
from gendiff import generate_diff

diff = generate_diff(path1, path2)
```

### As CLI tool

```
> gendiff --help
usage: gendiff [-h] [-f {stylish,plain,json}] first_file second_file

Compares two configuration files and shows a difference.

positional arguments:
  first_file
  second_file

optional arguments:
  -h, --help            show this help message and exit
  -f {stylish,plain,json}, --format {stylish,plain,json}
                        set format of output
```

## About gendiff
This is a cli utility that compares two configuration files with each other. The result of comparing files can be output in different formats: for example, plain ("flat"), json ("JSON format") or stylish ("nested").
## Demo
### Stylish
[![asciicast](https://asciinema.org/a/Yj8qVarAbMEZiSboOwx5lZFSE.svg)](https://asciinema.org/a/Yj8qVarAbMEZiSboOwx5lZFSE)
### Plain
[![asciicast](https://asciinema.org/a/CTfHD8nRjxNDDdPKYfOe1TCpF.svg)](https://asciinema.org/a/CTfHD8nRjxNDDdPKYfOe1TCpF)
### json
[![asciicast](https://asciinema.org/a/x1SPqVw9Mu0qQ5mJTplfXGyEh.svg)](https://asciinema.org/a/x1SPqVw9Mu0qQ5mJTplfXGyEh)
## Technologies
### CI/CD
GitHub Actions
### Testing
Pytest and pytest-cov
### CodeStyle
Flake8, Black, codeclimate
