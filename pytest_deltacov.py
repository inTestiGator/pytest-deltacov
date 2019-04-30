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


def set_cache(cov_list, uncov_list):
    """Caches covered and uncovered lines for use between runs"""
    for line in cov_list:
        config.cache.set("output/covered", line)
    for line in uncov_list:
        config.cache.set("output/uncovered", line)


def get_last_coverage(config):
    """Returns the coverage of the last test suit execution"""

    
def pytest_report_header(config):
    return "Using --delta coverage report"


def graphing_data():
    """Uses CSV file to create graph of code coverage"""


def notify_user():
    """Shows user what code changes decreased coverage"""
