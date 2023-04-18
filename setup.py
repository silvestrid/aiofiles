# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import os.path

readme = ''
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, 'README.rst')
if os.path.exists(readme_path):
    with open(readme_path, 'rb') as stream:
        readme = stream.read().decode('utf8')

setup(
    long_description=readme,
    name='aiofiles',
    version='23.1.0',
    description='File support for asyncio.',
    python_requires='==3.*,>=3.7.0',
    project_urls={"repository": "https://github.com/Tinche/aiofiles"},
    author='Tin Tvrtkovic',
    author_email='tinchester@gmail.com',
    license='Apache-2.0',
    packages=['aiofiles', 'aiofiles.tempfile', 'aiofiles.threadpool'],
    package_dir={"": "src"},
    package_data={},
    install_requires=[],
    extras_require={
        "dev": [
            "black==22.*,>=22.8.0", "coverage==6.*,>=6.4.4",
            "flake8==5.*,>=5.0.4", "pytest==7.*,>=7.1.2",
            "pytest-asyncio==0.*,>=0.19.0", "tox==3.*,>=3.25.1"
        ]
    },
)
