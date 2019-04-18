"""configuration file for deltacov tests"""

import pytest
import argparse
import pkg_resources
import subprocess
import xml.dom
from xml.dom import minidom
from pkg_resources import DistributionNotFound, VersionConflict

__version__= '1.0.0'

pytest_plugins = ["pytester"]

dependencies = [
    'pytester','pytest-cov>=2.6.0'
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
            print("100% coverage")

def pytest_report_header(config):
    """ Prints to the header """
    str = "Using --delta coverage report"
    return str
