import setuptools

from csabailonka.common import VERSION

with open("README.md", "r", encoding="UTF-8") as file:
    long_description = file.read()

setuptools.setup(
    name='MyPythonCommon',
    version=VERSION,
    author="Csaba Ilonka",
    author_email="csaba-ilonka@users.noreply.github.com",
    description="Common configuration and shareable utilities for Python projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/csaba-ilonka/python-common",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    python_requires='>=3.8'
)