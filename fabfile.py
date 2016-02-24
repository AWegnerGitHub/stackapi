#!/usr/bin/env python

from __future__ import print_function
from fabric.api import task, local, env, put
import re
import fileinput
import os
import datetime
import subprocess
import requests
try:
    import simplejson as json
except: 
    import json

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
    m = re.search(r'New version will be \'(\d+\.\d+\.\d+)\'', bumpver)
    version = m.groups(0)[0]

    # Really run bumpver to set the new release and tag
    bv_args = ['bumpversion', part]

    bv_args += ['--new-version', version]

    subprocess.check_output(bv_args)
    deploy(version)


@task
def deploy(version=None):
    if not version:
        version = subprocess.check_output(['python',
                                           'setup.py', '--version']).strip()

    # Build the package
    subprocess.check_output(['python', 'setup.py', 'sdist', 'upload', '-r', 'pypitest'])

