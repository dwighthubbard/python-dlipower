import os
from setuptools import setup

setup(
  name="dlipower",
  version="0.1.9",
  author="Dwight Hubbard",
  author_email="dwight@dwighthubbard.com",
  url="http://pypi.python.org/pypi/dlipower/",
  license="LICENSE.txt",
  packages=["dlipower",],
  scripts=["example.py","dli_power"],
  long_description=open('README.txt').read(),
  description="Control digital loggers web power switch",
  requires=["BeautifulSoup"],
)
