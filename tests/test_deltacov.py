"""Filler docstring, UPDATEME"""
# -*- coding: utf-8 -*-


def test_command_addoption_fixture(testdir):
    """Make sure that pytest accepts the --delta command."""

    # create a temporary pytest test module
    testdir.makepyfile(
        """
        def test_01():
            assert bar == True
    """
    )

    # run pytest with the following cmd args
    result = testdir.runpytest("--delta", "-v")

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines(["Using --delta coverage report"])

    # make sure that that we get a '0' exit code for the testsuite
    assert result.ret == 0


def test_help_message(testdir):
    """Filler docstring, UPDATEME"""
    result = testdir.runpytest("--help")
    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines(
        ["deltacov:", '*--foo=DEST_FOO*Set the value for the fixture "bar".']
    )


def test_hello_ini_setting(testdir):
    """Filler docstring, UPDATEME"""
    testdir.makeini(
        """
        [pytest]
        HELLO = world
    """
    )

    testdir.makepyfile(
        """
        import pytest

        @pytest.fixture
        def hello(request):
            return request.config.getini('HELLO')

        def test_hello_world(hello):
            assert hello == 'world'
    """
    )

    result = testdir.runpytest("--delta", "-v")

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines(["*::test_hello_world PASSED*"])

    # make sure that that we get a '0' exit code for the testsuite
    assert result.ret == 0
