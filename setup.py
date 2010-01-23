#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name = 'django-sluggable',
    version = '1.0',
    description = 'Automatically generated unique model slugs for Django models.',
    
    author = 'Ted Kaemming',
    author_email = 'ted@kaemming.com',
    url = 'http://www.github.com/tkaemming/django-sluggable/',
    
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    
    install_requires = ['setuptools']
)