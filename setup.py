#!/usr/bin/env python3
# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from setuptools import setup, find_packages
import os
import re
import io
import platform


version = '2.5.0'
major_version, minor_version, _ = version.split('.', 2)
major_version = int(major_version)
minor_version = int(minor_version)
name = 'Coog'

if minor_version % 2:
    version = '%s.%s.dev0' % (major_version, minor_version)

if platform.python_implementation() == 'PyPy':
    pg_require = ['psycopg2cffi >= 2.5.4']
else:
    pg_require = ['psycopg2 >= 2.5.4']

setup(name=name,
    version=version,
    description='Coog',
    long_description='The future',
    author='Coopengo',
    author_email='issue_tracker@tryton.org',
    url='http://www.tryton.org/',
    keywords='business application platform ERP',
    packages=find_packages(exclude=['*.modules.*', 'modules.*', 'modulversion = '%s.%s.dev0' % (major_version, minor_version)

if platform.python_implementation() == 'PyPy':
    pg_require = ['psycopg2cffi >= 2.5.4']
else:
    pg_require = ['psycopg2 >= 2.5.4']

setup(name=name,
    version=version,
    description='Coog',
    long_description='The future',
    author='Coopengo',
    author_email='issue_tracker@tryton.org',
    url='http://www.tryton.org/',
    keywords='business application platform ERP',
    packages=find_packages(exclude=['*.modules.*', 'modules.*', 'modules',
            '*.proteus.*', 'proteus.*', 'proteus']),
    scripts=[
        'bin/coog',
        ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: No Input/Output (Daemon)',
        'Framework :: Tryton',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: Bulgarian',
        'Natural Language :: Catalan',
        'Natural Language :: Chinese (Simplified)',
        'Natural Language :: Czech',
        'Natural Language :: Dutch',
        'Natural Language :: English',
        'Natural Language :: French',
        'Natural Language :: German',
        'Natural Language :: Hungarian',
        'Natural Language :: Italian',
        'Natural Language :: Persian',
        'Natural Language :: Polish',
        'Natural Language :: Portuguese (Brazilian)',
     es',
            '*.proteus.*', 'proteus.*', 'proteus']),
    scripts=[
        'bin/coog',
        ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: No Input/Output (Daemon)',
        'Framework :: Tryton',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: Bulgarian',
        'Natural Language :: Catalan',
        'Natural Language :: Chinese (Simplified)',
        'Natural Language :: Czech',
        'Natural Language :: Dutch',
        'Natural Language :: English',
        'Natural Language :: French',
        'Natural Language :: German',
        'Natural Language :: Hungarian',
        'Natural Language :: Italian',
        'Natural Language :: Persian',
        'Natural Language :: Polish',
        'Natural Language :: Portuguese (Brazilian)',
        'Natural Language :: Russian',
        'Natural Language :: Slovenian',
        'Natural Language :: Spanish',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        ],
    platforms='any',
    license='GPL-3',
    python_requires='>=3.4',
    install_requires=[
        'trytond-party@git+https://github.com/coopengo/party',
        ],
    extras_require={
        'PostgreSQL': pg_require,
        'graphviz': ['pydot'],
        'Levenshtein': ['python-Levenshtein'],
        'BCrypt': ['passlib[bcrypt]'],
        'html2text': ['html2text'],
        },
    zip_safe=False,
)

