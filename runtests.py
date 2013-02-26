#!/usr/bin/env python
import logging
import sys

from optparse import OptionParser
from tests.config import configure

logging.disable(logging.CRITICAL)


def run_tests(*test_args):
    from django_nose import NoseTestSuiteRunner
    test_runner = NoseTestSuiteRunner()
    if not test_args:
        test_args = ['tests']
    num_failures = test_runner.run_tests(test_args)
    if num_failures:
        sys.exit(num_failures)

if __name__ == '__main__':
    parser = OptionParser()
    __, args = parser.parse_args()
    configure(nose_args=['-s', '-x', '--with-spec'])
    run_tests(*args)
