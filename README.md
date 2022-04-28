# asgi-gzip

[![PyPI](https://img.shields.io/pypi/v/asgi-gzip.svg)](https://pypi.org/project/asgi-gzip/)
[![Changelog](https://img.shields.io/github/v/release/simonw/asgi-gzip?include_prereleases&label=changelog)](https://github.com/simonw/asgi-gzip/releases)
[![License](https://img.shields.io/pypi/l/asgi-gzip)](https://github.com/simonw/asgi-gzip/blob/main/LICENSE)

gzip middleware for ASGI applications, extracted from Starlette

## Installation

Install this library using `pip`:

    pip install asgi-gzip

## Usage

Usage instructions go here.

## Tracking Starlette

Since this code is extracted from Starlette, it's important to keep watch for changes and bug fixes to the Starlette implementation that should be replicated here.

The GitHub repository for this library uses [Git scraping](https://simonwillison.net/2020/Oct/9/git-scraping/) to track changes to a copy of the Starlette `gzip.py` module, which is kept in the `tracking/` folder.

Any time a change to that file is detected, an issue will be automatically created in the repository. This issue should be closed once the change to Starlette has been applied here, if necessary.

## Development

To contribute to this library, first checkout the code. Then create a new virtual environment:

    cd asgi-gzip
    python -mvenv venv
    source venv/bin/activate

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
