[![Build status](https://travis-ci.org/IliaZenkov/TravisCI_pytest_tox_project.svg?branch=master)](https://travis-ci.org/github/IliaZenkov/TravisCI_pytest_tox_project)
[![Coverage Status](https://coveralls.io/repos/github/IliaZenkov/TravisCI_pytest_tox_project/badge.svg?branch=master)](https://coveralls.io/github/IliaZenkov/TravisCI_pytest_tox_project?branch=master)
[![Updates](https://pyup.io/repos/github/IliaZenkov/TravisCI_pytest_tox_project/shield.svg)](https://pyup.io/repos/github/IliaZenkov/TravisCI_pytest_tox_project/)
[![Python 3](https://pyup.io/repos/github/IliaZenkov/TravisCI_pytest_tox_project/python-3-shield.svg)](https://pyup.io/repos/github/IliaZenkov/TravisCI_pytest_tox_project/)





# How to Write a Python Package
This here is a project I made to get familiar with **Travis CI** running **pytest and pytest-cov**, with **tox as a Travis frontend**, **PyUp to automatically manage dependencies and their security**, and **Coveralls to track code coverage**. Of course, if the package doesn't adhere to PEP8 then **black** will prevent the Travis build from passing.<br/>Now let's get writing a hit Python package ;)
 
 The Travis build config in ```.travis.yml``` sets up and configures a python venv(s) and runs pytest to execute tests found in ```./tests``` against the substring module provided in the find_substrings package located at ```./src/find_substrings```
 
Next, we use [twine](https://pypi.org/project/twine/) to automatically upload the find_substrings package to PyPI, after which anyone can install it by running ```pip install find_substrings``` to install all python modules in ```./src``` and their dependencies as configured in ```setup.py```

Alternatively, a ```requirements.txt``` file is included so users can manually install dependencies using ```pip install -r requirements.txt``` - For a one-click solution not relying on the package's ```setup.py```, users can run a shell script command such as  ```virtualenv .env && source .env/bin/activate && pip install -r requirements.txt```

#ToDo:
-Use [pre-commit](https://pre-commit.com/) to automatically run pre-configured hooks on commits before merging e.g. to automatically format with Black.
-Actually configure tox

