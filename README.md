# pytest-deltacov:
## Overview of Deltacov:

Deltacov is a plugin for [pytest](https://github.com/pytest-dev) that displays
the changes in code coverage between test suite executions in a graph. Developed using Python,
`deltacov` indicate changes in the code that can assist the user in achieving maximum
code coverage if code coverage decreases from one execution of the test suite or `deltacov` to another.

## Usage of Deltacov:

Deltacov has been configured to work with `Python 3.7.2`. Please ensure that the local version
of Python 3 has been installed by using the command `python3 --version`. If the terminal does not
display the correct version of Python, please update. Deltacov makes use of the cove plugin by running 
the command; `pipenv run pytest -x -s --cov-config pytest.cov --cov-report term-missing --cov` to retrieve
the code coverage. It also runs the command; `date +"%d-%m-%y"` to retrieve the time and date of when
the test was ran.
