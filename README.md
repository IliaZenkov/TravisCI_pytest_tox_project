[![Build status](https://travis-ci.org/IliaZenkov/TravisCI_pytest_tox_project.svg?branch=master)](https://travis-ci.org/github/IliaZenkov/TravisCI_pytest_tox_project)
[![Coveralls](https://coveralls.io/repos/github/IliaZenkov/TravisCI_pytest_tox_project/badge.svg?branch=HEAD&service=github)](https://coveralls.io/github/IliaZenkov/TravisCI_pytest_tox_project?branch=HEAD)
[![Test Coverage](https://api.codeclimate.com/v1/badges/b1345430b01dfb5ca59d/test_coverage)](https://codeclimate.com/github/IliaZenkov/TravisCI_pytest_tox_project/test_coverage)
[![Maintainability](https://api.codeclimate.com/v1/badges/b1345430b01dfb5ca59d/maintainability)](https://codeclimate.com/github/IliaZenkov/TravisCI_pytest_tox_project/maintainability)
[![Dependencies](https://pyup.io/repos/github/IliaZenkov/TravisCI_pytest_tox_project/shield.svg)](https://pyup.io/repos/github/IliaZenkov/TravisCI_pytest_tox_project/)
[![Python 3](https://pyup.io/repos/github/IliaZenkov/TravisCI_pytest_tox_project/python-3-shield.svg)](https://pyup.io/repos/github/IliaZenkov/TravisCI_pytest_tox_project/)





# How to Write a Python Package
This here is an example project I constructed from scratch (as opposed to using a [cookiecutter](https://github.com/cookiecutter/cookiecutter) template) to get familiar with [**Travis CI**](https://travis-ci.org/) running [**pytest**](https://docs.pytest.org/en/stable/contents.html) and [**pytest-cov**](https://pypi.org/project/pytest-cov/), with [**tox**](https://tox.readthedocs.io/en/latest/) as a Travis frontend, [**PyUp**](https://pyup.io/) to automagically manage dependencies and their security, and [**Coveralls**](https://pypi.org/project/coveralls/) to track code coverage. I'm also using [**CodeClimate**](https://codeclimate.com/) to track code quality. Of course, if the package doesn't adhere to PEP8 and consistent formatting then [**flake8**](https://pypi.org/project/flake8/) and [**Black**](https://pypi.org/project/black/) will prevent the Travis build from passing.

Now let's get writing a hit Python package ;)

# Selected Notes 
The Travis build config in ```.travis.yml``` tells Travis to build on Linux and OSX and specifies distribution(s) for each Python env. ```.travis.yml``` is mostly a wrapper around ```tox.ini``` - whereas tox itself sets up the python venvs inside Travis and runs pytest to execute tests found in ```./tests``` against the substring module provided in the find_substrings package located at ```./src/find_substrings```. Tox also covers all other aspects of the python environment config. 
 
Next, we use [twine](https://pypi.org/project/twine/) to automatically upload the find_substrings package to PyPI, after which anyone can install it by running ```pip install find_substrings``` to install all python modules in ```./src``` and their dependencies as configured in ```setup.py```

Alternatively, a ```requirements.txt``` file is included so users can manually install dependencies using ```pip install -r requirements.txt``` - For a one-click solution not relying on the package's ```setup.py```, users can run a shell script command such as  ```virtualenv .env && source .env/bin/activate && pip install -r requirements.txt```

# ToDo:  
- Add documentation with [**Sphinx**](https://www.sphinx-doc.org/en/master/)
- Use [**pre-commit**](https://pre-commit.com/) to automatically run pre-configured hooks on commits before merging e.g. to automatically format with Black.
- Publish to PyPI with [**Twine**](https://pypi.org/project/twine/)


