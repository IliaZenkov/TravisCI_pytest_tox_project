[![Build status](https://travis-ci.org/IliaZenkov/TravisCI_pytest_tox_project.svg?branch=master)](https://travis-ci.org/github/IliaZenkov/TravisCI_pytest_tox_project)
[![Updates](https://pyup.io/repos/github/IliaZenkov/TravisCI_pytest_tox_project/shield.svg)](https://pyup.io/repos/github/IliaZenkov/TravisCI_pytest_tox_project/)
[![Python 3](https://pyup.io/repos/github/IliaZenkov/TravisCI_pytest_tox_project/python-3-shield.svg)](https://pyup.io/repos/github/IliaZenkov/TravisCI_pytest_tox_project/)




# Travis+pytest+pytest_cov+PyUp: find_substrings
 A project I made to get familiar with Travis CI running pytest and pytest-cov, with tox as a Travis frontend, PyUp to automatically manage dependencies and their security, and Coveralls to track code coverage. Of course, if the package doesn't adhere to PEP8 then ```black --check``` will prevent the Travis build. All this to better understand production-ready Python package deployment!
 
 The Travis build config in ```.travis.yml``` sets up and configures a python venv(s) and runs pytest to execute tests found in ```./tests``` against the substring module provided in the find_substrings package located at ```./src/find_substrings```
 
Next, we use [twine](https://pypi.org/project/twine/) to automatically upload the find_substrings package to PyPI, after which anyone can install it by running ```pip install find_substrings``` to install all python modules in ```./src``` and their dependencies as configured in ```setup.py```

Alternatively, a ```requirements.txt``` file is included so users can manually install dependencies using ```pip install -r requirements.txt``` - For a one-click solution not relying on the package's ```setup.py```, users can run a shell script command such as  ```virtualenv .env && source .env/bin/activate && pip install -r requirements.txt```

