# pytest-deltacov

![logo](.github/Logo.png "pytest-deltacov")

[![Build Status](https://api.travis-ci.com/inTestiGator/pytest-deltacov.svg?branch=master)](https://travis-ci.com/inTestiGator/pytest-deltacov)
[![codecov.io](http://codecov.io/github/inTestiGator/pytest-deltacov/coverage.svg?branch=master)](http://codecov.io/github/inTestiGator/pytest-deltacov?branch=master)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-orange.svg)](https://www.python.org/)

## Overview of Features

Deltacov is a plugin for [pytest](https://github.com/pytest-dev) that displays
the changes in code coverage between test suite executions in a graph. Developed
using Python, deltacov indicates changes in the code that can assist the user
in achieving maximum code coverage. If coverage decreases between executions of
test suites or uses of `deltacov`, the user is provided with the graph of changes
in code coverage and is also provided with the lines that are not covered.

Deltacov utilizes the [covplugin](https://pypi.org/project/pytest-cov/)
by using the command:
`pipenv run pytest -x -s --cov-config pytest.cov --cov-report term-missing --cov`
which retrieves the code coverage. Although the user can see
these commands executed in the terminal, it is necessary in order to capture the
information needed to produce the graph. Once this data has been recorded, the
plugin then utilizes the [termgraph tool](https://github.com/mkaz/termgraph) to
display a bar graph within the terminal.

## Requirements

Deltacov has been configured to work with `Python 3.7.2`. Please ensure that the
local version of Python 3 has been installed by using the command `python3 --version`.
If the terminal does not display the correct version of Python, please update. Details
on upgrading and installing Python can be found [here](https://www.python.org/downloads/)
In addition, due to the plugin's reliance on `pytest cov`, this plugin must be installed
and at least version 2.6.

If you are unable to install Python on your workstation, you can download
the [Pyenv](https://github.com/pyenv/pyenv) tool to set up a virtual environment
for the newest Python version. Further instructions for installing Pyenv can be
found [here](https://github.com/pyenv/pyenv-installer)

## Installation

Installation for pytest-deltacov, as of now, requires the cloning of its repository.
This requires using the command `git clone git@github.com:inTestiGator/pytest-deltacov.git`
within the command line interface.

If necessary you may need to install and upgrade `pipenv` using the command:
`pip install pipenv --user`
Next, you must install the dependencies of `pipenv` by running the command:
`pipenv install --dev`

Next, it is required to run the setup of pytest-deltacov, so it compiles
This requires you to type: `python3 setup.py install`

And finally, to run the plugin use the command `pytest --deltacov`

## Example Output

(Insert a screenshot once plugin is functioning)
