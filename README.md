<p align="center">
    <a href="https://github.com/paulo-coutinho/pygemstones" target="_blank" rel="noopener noreferrer">
        <img width="120" src="extras/images/logo.png" alt="PyGemstones Logo">
    </a>
</p>

<h1 align="center">Python Gemstones</h1>

<p align="center">
  <a href="https://github.com/paulo-coutinho/pygemstones/actions"><img src="https://github.com/paulo-coutinho/pygemstones/actions/workflows/build.yml/badge.svg" alt="Build Status"></a>
  <a href="https://codecov.io/github/paulo-coutinho/pygemstones?branch=main"><img src="https://img.shields.io/codecov/c/github/paulo-coutinho/pygemstones/main.svg?sanitize=true" alt="Coverage Status"></a>
</p>

<p align="center">
Python package that group a lot of classes and functions that help software development.
</p>

<br>

### Requirements

* Python 3.6+

### How To Use

To use in your project, install `pygemstones` module:

```
pip install pygemstones
```

or:

```
poetry add pygemstones
```

And before call any pygemstones module, import system boostrap and call `init` method:

```python
from pygemstones.system import bootstrap
bootstrap.init()
```

### Modules

There are several implemented modules for you to use:

- io.file
- io.net
- io.pack
- system.bootstrap
- system.platform
- system.runner
- system.settings
- type.list
- type.string
- util.log
- vendor.aws

### Development

These are the requirements for local development:

* Python 3.6+
* Poetry (https://python-poetry.org/)

You can install locally:

```
poetry install
```

Or can build and generate a package:

```
poetry build
```

### Tests

```
poetry run pytest
```

### Coverage Tests

```
poetry run pytest --cov=pygemstones --cov-report=html tests
```

Note: see coverage report in htmlcov/index.html

### Linters

To run all linters use:

```
poetry run black --check pygemstones/
poetry run black --check tests/
poetry run mypy --ignore-missing-imports pygemstones/
poetry run mypy --ignore-missing-imports tests/
```

### Build and Publish

To build the package use:

```
poetry build
```

Set the token from your PyPI account with:

```
poetry config pypi-token.pypi [PyPI-Api-Access-Token]
```

And publish with:

```
poetry publish --build
```

### Release

To create a release for Github Action `publish steps` create a tag and push. Example:

```
git tag v0.0.1
git push origin v0.0.1
```

After release action finish, publish the release on Github `releases` page and Github Action will run `publish steps` automatically.
