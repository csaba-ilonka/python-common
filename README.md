# python-common

Common configuration and shareable utilities for Python projects.

### packaging.python.org
- [packaging-projects](https://packaging.python.org/tutorials/packaging-projects/)
- [installing-from-a-local-src-tree](https://packaging.python.org/tutorials/installing-packages/#installing-from-a-local-src-tree)

```shell
python setup.py sdist bdist_wheel
```

### Install:
```shell
python -m pip install --upgrade pip setuptools wheel
pip install git+https://github.com/csaba-ilonka/python-common.git@master#egg=MyPythonCommon
```

### Update:
```shell
pip install -U git+https://github.com/csaba-ilonka/python-common.git@master#egg=MyPythonCommon
```