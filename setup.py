#!/usr/bin/env python3

from glob import glob
from setuptools import find_packages, setup
from distutils.core import setup

setup(name='find_substrings',
      version='1.0',
      description='Script to find all substrings of given input string',
      author='Ilia Zenkov',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
     )
#install_requires=['']