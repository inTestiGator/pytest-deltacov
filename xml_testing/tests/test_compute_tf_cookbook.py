"""Test cases for the module that uses a cookbook programming style"""

import string
import sys
from termfrequency import compute_tf_cookbook


def test_read_file_populates_data_0():
    """Checks that reading the file populates global data variable"""
    # pylint: disable=len-as-condition
    assert len(compute_tf_cookbook.data) == 0
    compute_tf_cookbook.read_file("inputs/input.txt")
    assert len(compute_tf_cookbook.data) != 0


def test_check_for_isalnum():
    """Checks that all words are alphanumeric"""
    compute_tf_cookbook.filter_chars_and_normalize()
    compute_tf_cookbook.scan()
    for w in compute_tf_cookbook.words:
        assert w.isalnum()


def test_check_for_stopwords():
    """Checks that there are no stop words in the frequency list"""
    compute_tf_cookbook.remove_stop_words()

    with open("stopwords/stop_words.txt") as stop_file:
        stop_words = stop_file.read().split(",")
    # add single-letter words
    stop_words.extend(list(string.ascii_lowercase))

    for w in range(len(compute_tf_cookbook.words)):
        assert compute_tf_cookbook.words[w] not in stop_words


def test_check_sorted():
    """Checks that the frequencies and sort functions work together"""
    compute_tf_cookbook.frequencies()
    compute_tf_cookbook.sort()

    top = sys.maxsize
    for fr in compute_tf_cookbook.word_freqs:
        assert fr[1] <= top
        top = fr[1]


def test_naming_conventions():
    """Checks that the automatically generated path for the output is correct"""

    pathname = "inputs/input.txt"
    compute_tf_cookbook.create_output(pathname)
    assert compute_tf_cookbook.filename == "termfrequency/output/input.txt"
