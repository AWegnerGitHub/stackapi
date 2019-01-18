#!/usr/bin/env python

from __future__ import print_function

import re
import subprocess

from fabric.api import task


@task
def release(part='patch'):
    """ Automated software release workflow

    * (Configurably) bumps the version number
    * Tags the release

    You can run it like::

        $ fab release

    which, by default, will create a 'patch' release (0.0.1 => 0.0.2).

    You can also specify a patch level (patch, minor, major) to change to::

        $ fab release:part=major

    which will create a 'major' release (0.0.2 => 1.0.0).

    """

    # Dry run 'bumpversion' to find out what the new version number
    # would be. Useful side effect: exits if the working directory is not
    # clean.

    bumpver = subprocess.check_output(
        ['bumpversion', part, '--dry-run', '--verbose'],
        stderr=subprocess.STDOUT)
    m = re.search(r'New version will be \'(\d+\.\d+\.\d+)\'', bumpver.decode('utf-8'))
    version = m.groups(0)[0]

    # Really run bumpver to set the new release and tag
    bv_args = ['bumpversion', part]

    bv_args += ['--new-version', version]

    subprocess.check_output(bv_args)

# @task
# def deploy(version=None):
#     """Since I handle deployment in Travis CI, this should never be called"""
#     if not version:
#         version = subprocess.check_output(['python',
#                                            'setup.py', '--version']).strip()
#
#     # Build the package
#     subprocess.check_output(['python', 'setup.py', 'sdist', 'upload', '-r', 'pypi'])
#
