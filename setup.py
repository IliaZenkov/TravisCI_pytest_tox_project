#!/usr/bin/env python3

from glob import glob
from setuptools import find_packages, setup, Command

setup(name='find_substrings',
      version='1.0',
      description='Script to find all substrings of given input string',
      author='Ilia Zenkov',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
     )

install_requires=['']

class testcov(Command):
    description = "runs pytest and sends report through codeclimate"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        errno = call(["pytest --cov=src --durations=10 tests"], shell=True)
        if os.getenv("TRAVIS_PULL_REQUEST") == "false":
            call(["python -m codeclimate_test_reporter --file .coverage"], shell=True)
        raise SystemExit(errno)

cmdclass={'testcov': testcov}
