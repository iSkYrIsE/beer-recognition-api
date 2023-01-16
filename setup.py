#!/usr/bin/python3
# Copyright 2022 Marcos Gómez de Quero Santos
# See LICENSE for details.
# Author: Marcos Gome de Quero (@iSkYrIsE on GitHub)


import io
from setuptools import setup, find_packages


def readme():
    with io.open('README.md', encoding='utf-8') as f:
        return f.read()


def requirements(filename):
    reqs = list()
    with io.open(filename, encoding='utf-8') as f:
        for line in f.readlines():
            yield line.strip()


setup(
    name='beer_recognition_api',
    version='2.0',
    packages=find_packages(),
    url="https://github.com/iSkYrIsE/beer-recognition-api",
    download_url='https://github.com/iSkYrIsE/beer-recognition-api/archive/1.0.tar.gz',
    license='LICENSE.md',
    author='Marcos Gómez de Quero Santos',
    author_email='marcgomezdequero99@gmail.com',
    description='',
    long_description=readme(),
    long_description_content_type='text/markdown',
    install_requires=list(requirements(filename='requirements.txt')),
    data_files=[],
    entry_points={
        'console_scripts': [
            'beer_recognition_api=beer_recognition_api.run:main'
        ],
    },
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Intended Audience :: Developers"
    ],
    python_requires='>=3',
    project_urls={
        'Bug Reports': 'https://github.com/iSkYrIsE/beer-recognition-api/issues',
        'Source': 'https://github.com/iSkYrIsE/beer-recognition-api'
    },
)