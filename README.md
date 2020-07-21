[![Build status](https://travis-ci.org/iliazenkov/travis-pytest-hello-world.svg?master)](https://travis-ci.org/iliazenkov)

# Travis+pytest find_substrings
 A project I made to get familiar with Travis CI running pytest in order to better understand production-ready Python package deployment.
 
 The Travis build config in ```.travis.yml``` sets up and configures a python venv(s) and runs pytest to execute tests found in ```./tests``` against the substring module provided in the find_substrings package located at ```./src/find_substrings```
 
 As an example, I would upload this package to PyPI and then be able to install it by running ```pip install find_substrings``` which should install all python modules in ```./src``` and their dependencies as configured in ```setup.py```

Alternatively, a ```requirements.txt``` file is included so users can manually install dependencies using ```pip install -r requirements.txt``` or for a one-click solution by running a shell script command such as  ```virtualenv .env && source .env/bin/activate && pip install -r requirements.txt```
