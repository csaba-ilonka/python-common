#
# https://packaging.python.org/tutorials/packaging-projects/
#
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-common",
    version="0.0.1",
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
    python_requires='>=3.8',
)