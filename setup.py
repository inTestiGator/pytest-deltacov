"""This file is used to deploy the plugin"""
import io
import os
from setuptools import setup

install_requires = ["pygithub", "pytest>=4.4.0", "gitpython", "requests"]


def read(filename):
    """This function takes in a filepath and reads the file"""
    filepath = os.path.join(os.path.dirname(__file__), filename)
    with io.open(filepath, mode="r", encoding="utf-8") as f:
        return f.read()


setup(
    name="pytest-deltacov",
    version="0.1.4",
    description="A pytest plugin that proivdes the user with a graph of changes in code coverage.",
    author="Team deltacov",
    author_email="reibelj@allegheny.edu",
    url="https://github.com/inTestiGator/pytest-deltacov",
    license="GNU",
    platforms="any",
    install_requires=install_requires,
    py_modules=["pytest_deltacov"],
    entry_points={"pytest11": ["deltacov = pytest_deltacov"]},
)
