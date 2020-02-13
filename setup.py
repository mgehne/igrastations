from setuptools import setup

setup(
   name='igrastations',
   version='0.1',
   description='Functions and utilities for reading and analyzing IGRA station data',
   author='Maria Gehne',
   author_email='maria.gehne@noaa.gov',
   packages=['igrastations'],  #same as name
   install_requires=['numpy', 'pandas', 'urllib', 'io', 'zipfile', 'os'], #external packages as dependencies
)