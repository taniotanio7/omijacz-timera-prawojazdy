#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Setup file for omijacz_timera_prawojazdy.

    This file was generated with PyScaffold 3.0.2.
    PyScaffold helps you to put up the scaffold of your new Python project.
    Learn more under: http://pyscaffold.org/
"""

# import sys
# from setuptools import setup
#
# # Add here console scripts and other entry points in ini-style format
# entry_points = """
# [console_scripts]
# omijacz_timera=omijacz_timera_prawojazdy.__main__:main
# """
#
#
# def setup_package():
#     needs_sphinx = {'build_sphinx', 'upload_docs'}.intersection(sys.argv)
#     sphinx = ['sphinx'] if needs_sphinx else []
#     setup(setup_requires=['pyscaffold>=3.0a0,<3.1a0'] + sphinx,
#           entry_points=entry_points,
#           use_pyscaffold=True)
#
#
# if __name__ == "__main__":
#     setup_package()

# -----------------------------------------
# !/usr/bin/env python
# -*- coding: utf-8 -*-

# Note: To use the 'upload' functionality of this file, you must:
#   $ pip install twine
#
# setup.py by Kenneth Reitz (https://github.com/kennethreitz/setup.py)

import io
import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command

# Package meta-data.
NAME = 'omijacz_timera'
DESCRIPTION = 'Skrypt omijający zbyt długi wymagany czas na slajd na stronie prawojazdy.com.pl'
URL = 'http://github.com/taniotanio7/omijacz-timera-prawojazdy'
EMAIL = 'jonatanwitoszek@gmail.com'
AUTHOR = 'Jonatan Witoszek'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = '0.4.0'

# What packages are required for this module to be executed?
REQUIRED = [
    'requests', 'splinter', 'docopt'
]

DEPENDENCY_LINKS = [
    'git+ssh://git@github.com:taniotanio7/chromedriver_installer.git@master#egg=new_chromedriver_installer-0.0.7'
]

# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the Trove Classifier for that!

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.rst' is present in your MANIFEST.in file!
with io.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    with open(os.path.join(here, NAME, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION


class UploadCommand(Command):
    """Support setup.py upload."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPi via Twine…')
        os.system('twine upload dist/*')

        self.status('Pushing git tags…')
        os.system('git tag v{0}'.format(about['__version__']))
        os.system('git push --tags')

        sys.exit()


# Where the magic happens:
setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    # If your package is a single module, use this instead of 'packages':
    # py_modules=['mypackage'],

    entry_points={
        'console_scripts': ['omijacz_timera=omijacz_timera.omijacz_timera:main'],
    },
    install_requires=REQUIRED,
    dependency_links=DEPENDENCY_LINKS,
    include_package_data=True,
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    # $ setup.py publish support.
    cmdclass={
        'upload': UploadCommand,
    },
)
