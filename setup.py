#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
import imp

version = imp.load_source('postdecorate.version',
                          'postdecorate/version.py')


setup(name="postdecorator",
      version=version.__version__,
      description='Trollduction extension for image decoration',
      author='koe',
      author_email='nathan.koefer@gmail.com',
      url="",
      packages=['postdecorate'],
      scripts=['bin/postdecorator.py'],
      zip_safe=False,
      license="",
      classifiers=[],
      test_suite='',
      )
