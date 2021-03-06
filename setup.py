#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-ctdata-datapackage',
    version='0.1.0',
    author='Sasha Cuerda',
    author_email='scuerda@ctdata.org',
    maintainer='Sasha Cuerda',
    maintainer_email='scuerda@ctdata.org',
    license='MIT',
    url='https://github.com/scuerda/pytest-ctdata-datapackage',
    description='Plugin for testing CTData datasets',
    long_description=read('README.rst'),
    py_modules=['pytest_ctdata_datapackage'],
    install_requires=['pytest>=2.9.2', 'datapackage'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'pytest11': [
            'ctdata_datapackage = pytest_ctdata_datapackage',
        ],
    },
)
