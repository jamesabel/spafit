#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='main',
      version = '0.0',
      packages = find_packages(),
      options={
          'win': {
              'formal_name': 'main',
          },
          'macos': {
              'app_requires': [
                  'PyQt5',
                  'cryptography',
              ],
        },
    }
)
