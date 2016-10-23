#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='main',
      version = '0.0',
      packages = find_packages(),
      options={
          'app': {
              'formal_name': 'main',
              'bundle': 'co.abel',
          },
          'macos': {
              'app_requires': [
                  'toga-cocoa',
                  'PyQt5',
                  'cryptography',
              ],
              'icon': 'icons/circle',
        },
    }
)
