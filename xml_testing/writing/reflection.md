# Reflection by Tara Douglass

## Explain the use and benefits of the `pytest-sugar` and `pytest-clarity` plugins

Both the `pytest-sugar` and `pytest-clarity` plugins are useful tools which help
to visualize the results of test suites run through pytest. As demonstrated in the
fenced code block below, `pytest-sugar` adds check marks, or the letter x, which
is not pictured below, next to specific tests indicating whether they have
passed or failed. In addition, it also adds a progress bar to the right of each
check which indicates what percentage of tests have been run. The `pytest-clarity`
plugin is not displayed in this report, as it pertains to failed test cases. What
that tool does, however, is aid in debugging by reformatting the output of failed
tests and offering suggestions as to how they may be resolved.

## Explain why `compute_tf_cookbook` does not support parameterize testing

The `compute_tf_cookbook.py` program is not one which is built for parameterized
testing. Parameterized testing, as described in our pytest book, works well for
functions that can take parameters and return a value which is dependent on said
parameters. However, with the exceptions of the function that I have added, and
the `read_file` function, all of the other functions do not take in any
parameters. Thus, it would be impractical to try and implement parameterized
testing. An example of one of the other functions where this limitation exists
is in the code block below. However, it is important to note that this is just
one example of many.

```
def scan():
    “““
    Scans data for words, filling the global variable words
    ”””
    # pylint: disable=global-statement
    global data
    global words
    data_str = “”.join(data)
    words = words + data_str.split()
```

## Provide a fenced code block with the final code coverage report for your tests

```
 tests/test_compute_tf_cookbook.py::test_read_file_populates_data_0 ✓   20% ██
 tests/test_compute_tf_cookbook.py::test_check_for_isalnum ✓            40% ████
 tests/test_compute_tf_cookbook.py::test_check_for_stopwords ✓          60% ██████
 tests/test_compute_tf_cookbook.py::test_check_sorted ✓                 80% ████████
 tests/test_compute_tf_cookbook.py::test_naming_conventions ✓          100% ██████████
----------- coverage: platform linux, python 3.6.7-final-0 -----------
Name                                   Stmts   Miss  Cover   Missing
--------------------------------------------------------------------
termfrequency/__init__.py                  0      0   100%
termfrequency/compute_tf_cookbook.py      51     10    80%   123-133
--------------------------------------------------------------------
TOTAL                                     51     10    80%
```

## Briefly discuss at least three "red flags" for a software system

In the field of software design, there are many styles of coding which could be
considered red flags. Otherwise stated, these design choices often add to the
complexity or insecurity of a software system. One simple red flag that is
often found in code is a "vague name", where the naming convention that has been
used is so vague that it doesn't convey any useful data as to what it is or what
it does. Another red flag which adds to code complexity is when an entity is
"hard to describe", or it requires excessively long documentation to be able to
understand. A third red flag could be "nonobvious code", which would be code
written in such a manner that its purpose or behavior is unclear.
All of these red flags make code more complex by making it more
difficult for the software engineer to read and understand the code efficiently.
If code is hard to decipher, then a programmer is more likely to miss important
parts of it.

## Did you find any red flags in your implementation? How did you handle them?

Going off the examples in the back of the Philosophy of Software Design book,
I was only able to find two red flags within my code implementation. One red flag
was one which I had introduced, which would be a "vague name". This applied to my
variable simply named `f`, which represented a file object. I resolved this issue
by renaming the variable to `file` instead. The second and arguably most important
red flag which I found was "information leakage" in the form of global variables
used throughout the code. As this program was written in the cookbook style, I
could not figure out a way to eliminate global variables without refactoring the
whole program. As this is only a small application which will not be used
commercially, this should not be a problem. However, if this were on a larger
scale it would be imperative to avoid the use of global variables.

## Explain the challenges that you encountered and how you overcame them

This practical, in comparison to the others I have completed, has given me the
least amount of challenges. This is namely because for practical 4, I did not
have to write any new code, and could instead directly copy my code from
practical 3. The challenges which were presented in this practical came from
trying to find and resolve red flags. Whereas the red flag of the "vague name"
was easy to fix, the larger one still proves to be a problem. In order to
"overcome" this outstanding issue, I had to simply ignore it. The alternative,
as I had seen it, would have been a complete overhaul of the `compute_tf_cookbook.py`
program, which I felt was outside the scope of this practical.
