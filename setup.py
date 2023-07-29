from setuptools import setup
from typing import List
NAME = 'Housing-predictor'
VERSIOn = '0.0.0.1'
AUTHOR = 'Sherin Thomas'
REQUIREMENTS_FILE = 'requirements.txt'
def get_requirements_list()-> List[str]:
    with open(REQUIREMENTS_FILE) as req:
        return req.readlines()
setup(
    name=NAME,
    version=VERSIOn,
    author=AUTHOR,
    packages=['Housing'],
    install_requires = get_requirements_list()

)

