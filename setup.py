import setuptools

VERSION = '0.0.1'

with open("README.md", "r", encoding="UTF-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='MyPythonCommon',
    version=VERSION,
    author="Csaba Ilonka",
    author_email="24225461+csaba-ilonka@users.noreply.github.com",
    description="Common configuration and utilities for Python projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/csaba-ilonka/python-common",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    python_requires='>=3.8'
)