# pytest-deltacov

![logo](.github/Logo.png "pytest-deltacov")

[![Build Status](https://api.travis-ci.com/inTestiGator/pytest-deltacov.svg?branch=master)](https://travis-ci.com/inTestiGator/pytest-deltacov)
[![codecov.io](http://codecov.io/github/inTestiGator/pytest-deltacov/coverage.svg?branch=master)](http://codecov.io/github/inTestiGator/pytest-deltacov?branch=master)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-orange.svg)](https://www.python.org/)

## Overview of Features

Deltacov is a plugin for [pytest](https://github.com/pytest-dev) that displays
the changes in code coverage between test suite executions in a graph. Developed
using Python, `deltacov` indicates changes in the code that can assist the user
in achieving maximum code coverage if coverage decreases from one execution of
the test suite or `deltacov` to another. Deltacov makes use of
[covplugin](https://pypi.org/project/pytest-cov/) by running the command:
`pipenv run pytest -x -s --cov-config pytest.cov --cov-report term-missing --cov`
to retrieve the code coverage. Although the user can see
these commands executed in the terminal, it is necessary in order to capture the
information needed to produce the graph. Once this data has been recorded, the
plugin then utilizes the [termgraph tool](https://github.com/mkaz/termgraph) to
display a bar graph within the terminal.

## Usage of Deltacov

In order to run `deltacov`, please ensure all requirements are met and use the command
`pipenv run pytest --delta`. Due to the nature of the plugin, changes involving the
restructure of a program or the addition of new code may result in false flags as
coverage is compared on a line by line basis.

## Requirements

Deltacov has been configured to work with `Python 3.7.2`. Please ensure that the
local version of Python 3 has been installed by using the command `python3 --version`.
If the terminal does not display the correct version of Python, please update. In
addition, due to the plugin's reliance on `pytest cov`, this plugin must be installed.

## Installation

  Include how to install the plugin in this section

## Example Output

  It may serve useful to have a picture of what the output should look like,
  so users know if they are running the plugin correctly.
