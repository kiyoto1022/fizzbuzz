#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='fizz_buzz',
    version='1.0',
    description='Enjoy FizzBuzz.',
    author='Kiyoto Akiyama',
    author_email='kiyoto@akiyama.co',
    url='https://github.com/kiyoto1022/fizzbuzz',
    packages = find_packages(exclude=('tests')),
    test_suite = 'tests'
)