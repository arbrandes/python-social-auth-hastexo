#!/usr/bin/env python
from setuptools import setup, find_packages

from hastexo_backend import get_version

setup(
    name='python-social-auth-hastexo',
    version=get_version(),
    url='https://github.com/hastexo/python-social-auth-hastexo',
    description=("hastexo backend for python-social-auth"),
    long_description=open('README.rst').read(),
    keywords="oauth, social auth",
    license=open('LICENSE').read(),
    platforms=['linux'],
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    install_requires=['python-social-auth>=0.2.12'],
    extras_require={},
    # See http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Other/Nonlisted Topic'],
)
