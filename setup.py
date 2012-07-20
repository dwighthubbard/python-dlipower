import os
from setuptools import setup

setup(
  name="dlipower",
  version="0.2.14",
  author="Dwight Hubbard",
  author_email="dwight@dwighthubbard.com",
  url="http://pypi.python.org/pypi/dlipower/",
  license="LICENSE.txt",
  packages=["dlipower",],
  scripts=["example.py","dlipower/dlipower.py"],
  long_description=open('README.txt').read(),
  description="Control digital loggers web power switch",
  requires=["BeautifulSoup"],
)
