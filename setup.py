#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import versioneer

NAME = 'py_translator'


def readme():
    with open('README.md', encoding='utf-8') as f:
        return f.read()


setup(
    name=NAME,
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description=readme(),
    long_description=readme(),
    author='GuQiangJS',
    author_email='guqiangjs@gmail.com',
    url='https://github.com/GuQiangJS/py_translator.git',
    keywords='translator',
    install_requires=['requests'],
    packages=find_packages(),
    zip_safe=False,
)