"""Deltacov plugin for pytest.
Visually displays changes in code coverage in a graph and indicates changes that
result in decreased coverage
"""

import pytest
import argparse
import pkg_resources
from pkg_resources import DistributionNotFound, VersionConflict
from pytest import Collector

__version__= '1.0.0'

dependencies = [
    'pytest-cov>=2.6.0'
]

# pytest-cov
try:
    pkg_resources.require(dependencies)
except DistributionNotFound:
    print("pytest-deltacov requires the package pytest-cov")


def pytest_addoption(parser):
    """Collect coverage delta with --delta flag"""
    group = parser.getgroup('deltacov', 'Coverage deltas')
    group.addoption(
        '--delta',
        action='store',
        help='pytest-deltacov help:\n\
         --delta : Display a graph of code coverage over time (previous ten runs)'
    )

def run_subprocess():
    """ Runs a subprocess to create the xml file """
    cmd = "pipenv run pytest -x -s --cov-config pytest.cov --cov-report xml:cov.xml --cov"
    run.subprocess(cmd.split(), capture_output=False, shell=False)


# def parse_xml_for_coverage():
#     """ Parses the generated xml file """
#     xml_file = minidom.parse('cov.xml')
#     all_lines = xml_file.getElementsByTagName('line')
#
#     for line in all_lines:
#         if line.attributes['hits'].value == 0:
#             line_number = line.attributes['number'].value
#             #return uncovered lines
#         else:
#             #lines are covered

@pytest.fixture
def empty_cache(request):
    """Checks cache for covered and uncovered lines"""
    cov = request.config.cache.get("output/covered", None)
    uncov = request.config.cache.get("output/uncovered", None)
    if cov and uncov = None:
        print("First test execution")
    return 1


def set_cache(cov_list, uncov_list):
    """Caches covered and uncovered lines for use between runs"""
    for line in cov_list:
        config.cache.set("output/covered", line)
    for line in uncov_list:
        config.cache.set("output/uncovered", line)


def pytest_report_header(config):
    return "Using --delta coverage report"


def graphing_data():
    """Uses CSV file to create graph of code coverage"""


def notify_user(delta, cov_list, uncov_list):
    """Shows user what code changes decreased coverage"""
    i=0
    # list to hold lines that lost coverage
    changed = []
    # if coverage has decreased
    if delta < 0:
        # compares lines covered before to lines currently uncovered
        while i < len(cov_list):
            if cov_list[i] in uncov_list:
                changed.append(cov_list[i])
                i++
            else:
                i++
        print("The following lines are no longer covered in the most recent test suite execution: ")
        while changed[i] is not None:
            print(changed[i] + ", ")
            i++

    elif delta == 0:
        print("The coverage has not changed since the last test suite execution.")
        print("Please be advised that some lines' coverage status may have changed due to changes in code/tests")

    else:
        print("The coverage has increased since the last test suite execution.")
        print("Please be advised that some lines' coverage status may have changed due to changes in code/tests")
