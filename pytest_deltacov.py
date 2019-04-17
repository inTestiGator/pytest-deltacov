"""Deltacov plugin for pytest.

Visually displays changes in code coverage in a graph and indicates changes that
result in decreased coverage
"""

import pytest
import argparse

def pytest_addoption(parser):
    """ Creates the command line argument for teh deltacov plugin """
    group = parser.getgroup('deltacov')
    group.addoption(
        '--delta',
        action='store',
        help='pytest-deltacov help:\n\
         --delta : Display a graph of code coverage over time (previous ten runs)'
    )

@pytest.fixture
def bar(request):
    """Filler docstring, UPDATEME"""
    return request.config.option.dest_foo


def format_csv_file():
    """Retrieves coverage data and organizes it into a CSV file"""


def graphing_data():
    """Uses CSV file to create graph of code coverage"""


def notify_user():
    """Shows user what code changes decreased coverage"""
