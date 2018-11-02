#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Copyright (c) 2018 Sonal Raj. This program is open-source software,
# and may be redistributed under the terms of the MIT license. See the
# LICENSE file in this distribution for details.

import os
import re


try:
    from setuptools import setup
    has_setuptools = True
except ImportError:
    from distutils.core import setup
    has_setuptools = False


if has_setuptools:
    additional_setup_options = dict(
        install_requires=['yuicompressor'],
        entry_points={
            'distutils.commands': [
                'js-min = amelio.compress:minify_js',
                'css-min = amelio.compress:minify_css',
            ],
        },
    )
else:
    # The packages that need obfuscation functionality should use import the amelio.compress
    # package and declare the cmdclass setup parameter like this:
    # cmdclass={
    #    'js-min': amelio.compress.minify_js,
    #    'css-min': minify.compress.minify_css
    #},
    additional_setup_options = dict()


def read(*path_parts):
    here = os.path.dirname(__file__)
    return open(os.path.join(here, *path_parts)).read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


# package description
desc = "Amelio: The code optimization library for compressing, decompressing and cleaning up code"
long_desc = '\n\n'.join(read(f) for f in ('README.rst', 'CHANGES.rst'))


setup(
    name='amelio',
    version=find_version('amelio', '__init__.py'),
    author='Sonal Raj',
    author_email='sonal.nitjsr@gmail.com',
    description=desc,
    long_description=long_desc,
    license='MIT License',
    keywords='amelio,css,javascript,js,distutils,setuptools,command,setup.cfg,compress,decompress,style',
    url='https://github.com/sonal-raj/amelio',
    packages=['amelio'],
    platforms='any',
    classifiers=[
        'Development Status :: 1 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
        'Programming Language :: Python',
    ],
    **additional_setup_options
)
