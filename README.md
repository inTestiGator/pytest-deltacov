# pytest-deltacov:
## Overview of Deltacov:

Deltacov is a plugin for [pytest](https://github.com/pytest-dev) that displays
the changes in code coverage between test suite executions in a graph. Developed using Python,
`deltacov` indicates changes in the code that can assist the user in achieving maximum
code coverage if coverage decreases from one execution of the test suite or `deltacov` to another.
Deltacov makes use of the [cov plugin](https://pypi.org/project/pytest-cov/) by running the command; `pipenv run pytest -x -s --cov-config pytest.cov --cov-report term-missing --cov`
to retrieve the code coverage. It also runs the command; `date +"%d-%m-%y"` to retrieve the time and date of when
the test was ran. Although the user can see these commands executed in the terminal, it is necessary
in order to capture the information needed to produce the graph. This is accomplished through the
use of the `script` command which saves the information to a file called `output.txt`. Due to potential
issues while graphing, `deltacov` only shows the ten most recent test execution reports, regardless of
the time or date.

## Usage of Deltacov:

Deltacov has been configured to work with `Python 3.7.2`. Please ensure that the local version
of Python 3 has been installed by using the command `python3 --version`. If the terminal does not
display the correct version of Python, please update.
