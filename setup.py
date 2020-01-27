#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file exists within 'dob-viewer':
#
#   https://github.com/hotoffthehamster/dob-viewer

"""
Packaging instruction for setup tools.

Refs:

  https://setuptools.readthedocs.io/

  https://packaging.python.org/en/latest/distributing.html

  https://github.com/pypa/sampleproject
"""

from setuptools import find_packages, setup

# *** Package requirements.

requirements = [
# FIXME/2019-12-06: Find other click libs and verify all included.
    # (lb): Click may be the best optparser of any language I've used.
    #  https://github.com/pallets/click
# FIXME/2020-01-05 17:54: Using version is failing for me on `make develop`.
#    'click--hotoffthehamster >= 7.1.0',
    'click--hotoffthehamster',
    # INI/config parser, even better (preserves comments and ordering).
    #  https://github.com/DiffSK/configobj
    #  https://configobj.readthedocs.io/en/latest/
    'configobj >= 5.0.6',
# FIXME/2020-01-05 17:57: Require dob, or the other way around?
    # The dob CLI core.
    'dob',
    # The dob CLI prompter.
    'dob-prompt',
# FIXME/2020-01-05 17:31: Scrub the `future` library, but now it is!
    # Compatibility layer between Python 2 and Python 3.
    #  https://python-future.org/
    'future',
    # Vocabulary word pluralizer.
    #  https://github.com/ixmatus/inflector
    'Inflector',
    # The heart of Hamster. (Ye olde `hamster-lib`).
    'nark',
    # Amazeballs prompt library.
    # FIXME/2019-02-21: Submit PR. Until then, whose fork?
    'prompt-toolkit-dob >= 2.0.9',  # Imports as prompt_toolkit.
    # For the Carousel Fact description lexer.
    #  http://pygments.org/
    'pygments',
# FIXME/2020-01-05 17:50: Remove 'six', 'future', etc.
    # Virtuous Six Python 2 and 3 compatibility library.
    #  https://six.readthedocs.io/
    'six',
    # https://github.com/grantjenks/python-sortedcontainers/
    'sortedcontainers',
]

# *** Minimal setup() function -- Prefer using config where possible.

# (lb): All settings are in setup.cfg, except identifying packages.
# (We could find-packages from within setup.cfg, but it's convoluted.)

setup(
    install_requires=requirements,
    packages=find_packages(exclude=['tests*']),
    # Tell setuptools to determine the version
    # from the latest SCM (git) version tags.
    #
    # Without the following two lines, e.g.,
    #   $ python setup.py --version
    #   3.0.0a31
    # But with 'em, e.g.,
    #   $ python setup.py --version
    #   3.0.0a32.dev3+g6f93d8c.d20190221
    # Or, if the latest commit is tagged,
    # and your working directory is clean,
    # then the version reported (and, e.g.,
    # used on make-dist) will be from tag.
    # Ref:
    #   https://github.com/pypa/setuptools_scm
    setup_requires=['setuptools_scm'],
    use_scm_version=True,
)
