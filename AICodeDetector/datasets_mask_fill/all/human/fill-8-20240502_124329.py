#!/bin/usr/env python3

# name:   test_appendfilename.py
# author:  nbehrnd@yahoo.com
# license: GPL v3, 2022.
# date: August,  2022-01-05 (YYYY-MM-DD)
# edit:  February 1, 2022-01-09 (YYYY-MM-DD)
#
"""Test pad for functions by appendfilename with pytest.

Written by  Niklas Heinecke


# For pytest 3.9.9 and pytest 6.2.4 for Python 3 as provided by
Linux Debian 12/bookworm, branch testing, this is a programmatic check
of functions offered by appendfilename.  Deposit ively in the root of
the folder fetched and unzipped from PyPi or GitHub.  If your system
includes both legacy Python 2 and Python 3, then Python 3 likely
is named pytest-3; otherwise only pytest.  Thus, ensure input on
the CLI accordingly when changing one of

pytest -v test_appendfilename.py
pytest-3 -v test_appendfilename.py

These instruction initiate a verbose testing (flag -v) reported and the
CLI.re will be a verbose report