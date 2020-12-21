#
# https://packaging.python.org/tutorials/packaging-projects/
# https://packaging.python.org/tutorials/installing-packages/#installing-from-a-local-src-tree
#
import os
import shutil
from pathlib import Path

import setuptools

PACKAGE = 'MyPythonCommon'
VERSION = '0.0.1'
RELEASE = Path('release')


def clear():
    for directory in ['build', 'dist', 'MyPythonCommon.egg-info']:
        shutil.rmtree(directory, ignore_errors=True)

def preRelease():
    if RELEASE.exists():
        for file in os.listdir(RELEASE):
            if VERSION in file:
                raise Exception(f"Version {VERSION} already exists")

def release():
    dist = Path('dist')
    for file in [file for file in os.listdir(dist) if VERSION in file]:
        os.makedirs(RELEASE, exist_ok=True)
        shutil.copy(dist.joinpath(file), RELEASE.joinpath(file))

with open("README.md", "r", encoding="UTF-8") as fh:
    long_description = fh.read()

preRelease()
setuptools.setup(
    name=PACKAGE,
    version=VERSION,
    author="Csaba Ilonka",
    author_email="24225461+csaba-ilonka@users.noreply.github.com",
    description="Common configuration and utilities for Python projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/csaba-ilonka/python-common",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires='>=3.8'
)
release()
clear()