"""Deltacov plugin for pytest.

Visually displays changes in code coverage in a graph and indicates changes that
result in decreased coverage
"""
# -*- coding: utf-8 -*-

import pytest
import argparse
import pkg_resources
from pkg_resources import DistributionNotFound, VersionConflict

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


def parse_xml_for_coverage():
    """ Parses the generated xml file """
    xml_file = minidom.parse('cov.xml')
    all_lines = xml_file.getElementsByTagName('line')

    for line in all_lines:
        if line.attributes['hits'].value == 0:
            line_number = line.attributes['number'].value
            #these are the uncovered lines
        else:
            #lines are covered


def pytest_report_header(config):
    return "Using --delta coverage report"


def format_csv_file():
    """Retrieves coverage data and organizes it into a CSV file"""


def graphing_data():
    """Uses CSV file to create graph of code coverage"""


def notify_user():
    """Shows user what code changes decreased coverage"""
