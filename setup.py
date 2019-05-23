#!/usr/bin/env python3
# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

import io
import os
import re
from configparser import ConfigParser
from setuptools import setup


def read(fname):
    return io.open(
        os.path.join(os.path.dirname(__file__), fname),
        'r', encoding='utf-8').read()


def get_require_version(name):
    if minor_version % 2:
        require = '%s >= %s.%s.dev0, < %s.%s'
    else:
        require = '%s >= %s.%s, < %s.%s'
    require %= (name, major_version, minor_version,
        major_version, minor_version + 1)
    return require


config = ConfigParser()
config.read_file(open('tryton.cfg'))
info = dict(config.items('tryton'))
for key in ('depends', 'extras_depend', 'xml'):
    if key in info:
        info[key] = info[key].strip().splitlines()
version = info.get('version', '0.0.1')
major_version, minor_version, _ = version.split('.', 2)
major_version = int(major_version)
minor_version = int(minor_version)
name = 'trytond_api_token'

download_url = 'https://github.com/MaxTeiger/trytond-api-token/tree/add_setup'
if minor_version % 2:
    version = '%s.%s.dev0' % (major_version, minor_version)
    download_url = 'git+https://github.com/MaxTeiger/trytond-api-token/tree/add_setup'

requires = ['python-dateutil', 'python-sql >= 0.7', 'simpleeval']
for dep in info.get('depends', []):
    if not re.match(r'(ir|res)(\W|$)', dep):
        requires.append('trytond_%s' % dep)
requires.append('trytond')

tests_require = [get_require_version('proteus')]
dependency_links = []
dependency_links.append('git+https://github.com/coopengo/party#egg=trytond_party')
dependency_links.append('git+https://github.com/jcavallo/trytond@test_pip#egg=trytond')
if minor_version % 2:
    dependency_links.append('https://trydevpi.tryton.org/')

setup(name=name,
    version=version,
    description='api token module of tryton',
    author='Tryton',
    author_email='dev@coopengo.com',
    url='http://www.coopengo.com/',
    download_url=download_url,
    keywords='tryton api token',
    package_dir={'trytond.modules.api_token': '.'},
    packages=[
        'trytond.modules.api_token'
        ],
    package_data={
        'trytond.modules.api_token': (info.get('xml', [])
            + ['tryton.cfg', 'view/*.xml', 'locale/*.po', '*.fodt',
                'icons/*.svg', 'tests/*.rst']),
        },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Framework :: Tryton',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Legal Industry',
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
        'Topic :: Office/Business',
        'Topic :: Office/Business :: Financial :: Accounting',
        ],
    license='GPL-3',
    python_requires='>=3.4',
    install_requires=requires,
    dependency_links=dependency_links,
    zip_safe=False,
    entry_points="""
    [trytond.modules]
    api_token = trytond.modules.api_token
    """,
    test_suite='tests',
    test_loader='trytond.test_loader:Loader',
    tests_require=tests_require,
)