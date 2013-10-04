#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()


readme = open('README.rst').read()
doclink = """
Documentation
-------------

The full documentation is at http://quickdial.rtfd.org."""
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='quickdial',
    version='0.1.0',
    description='A fun little project to find the quickest gate address to dial.',
    long_description=readme + '\n\n' + doclink + '\n\n' + history,
    author='Taylor "Nekroze" Lawson',
    author_email='nekroze@eturnilnetwork.com',
    url='https://github.com/Nekroze/quickdial',
    packages=[
        'quickdial',
    ],
    package_dir={'quickdial': 'quickdial'},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'quickdial = quickdial.quickdial:main',
        ]
    },
    install_requires=[
    ],
    license='MIT',
    zip_safe=False,
    keywords='quickdial',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
