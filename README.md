<p align="center">
    <a href="https://github.com/paulocoutinhox/pygemstones" target="_blank" rel="noopener noreferrer">
        <img width="120" src="extras/images/logo.png" alt="PyGemstones Logo">
    </a>
</p>

<h1 align="center">Python Gemstones</h1>

<p align="center">
  <a href="https://github.com/paulocoutinhox/pygemstones/actions"><img src="https://github.com/paulocoutinhox/pygemstones/actions/workflows/build.yml/badge.svg" alt="Build Status"></a>
  <a href="https://codecov.io/github/paulocoutinhox/pygemstones?branch=main"><img src="https://img.shields.io/codecov/c/github/paulocoutinhox/pygemstones/main.svg?sanitize=true" alt="Coverage Status"></a>
</p>

<p align="center">
Python package that group a lot of classes and functions that help software development.
</p>

<br>

### Requirements

* Python 3.7+

### How To Use

To use in your project, install `pygemstones` module:

```
python3 -m pip install pygemstones
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

* Python 3.7+
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

## Buy me a coffee

<a href='https://ko-fi.com/paulocoutinho' target='_blank'><img height='36' style='border:0px;height:36px;' src='https://az743702.vo.msecnd.net/cdn/kofi1.png?v=2' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>

## License

[MIT](http://opensource.org/licenses/MIT)

Copyright (c) 2021-2024, Paulo Coutinho
