"""Deltacov plugin for pytest.

Visually displays changes in code coverage in a graph and indicates changes that
result in decreased coverage
"""
# -*- coding: utf-8 -*-

import pytest


def pytest_addoption(parser):
    group = parser.getgroup('deltacov')
    group.addoption(
        '--delta',
        action='store',
        dest='dest_foo',
        default='2019',
        help='Display a graph of code coverage over time (previous ten runs)'
    )

    parser.addini('HELLO', 'Dummy pytest.ini setting')


@pytest.fixture
def bar(request):
    return request.config.option.dest_foo

def retrieve_coverage():
    """Runs test suite for coverage data"""

def format_csv_file():
    """Organizes collected data into a CSV file"""

def graphing_data():
    """Uses CSV file to create graph of code coverage"""

def notify_user():
    """Shows user what code changes decreased coverage"""
