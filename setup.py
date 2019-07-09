# -*- coding: utf-8 -*-
# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


def read_requirements():
    """Parse requirements from requirements.txt."""
    reqs_path = os.path.join('.', 'requirements.txt')
    with open(reqs_path, 'r') as f:
        requirements = [line.rstrip() for line in f]
    return requirements


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='twitter-api',
    version='1.0.0',
    description='Twitter API for Python',
    long_description=readme,
    author='nukopy',
    author_email='',
    url='https://github.com/nukopy/twitter-api',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=read_requirements()
)
