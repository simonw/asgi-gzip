from setuptools import setup
import os

VERSION = "0.2"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="asgi-gzip",
    description="gzip middleware for ASGI applications, extracted from Starlette",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/asgi-gzip",
    project_urls={
        "Issues": "https://github.com/simonw/asgi-gzip/issues",
        "CI": "https://github.com/simonw/asgi-gzip/actions",
        "Changelog": "https://github.com/simonw/asgi-gzip/releases",
    },
    license="BSD",
    version=VERSION,
    packages=["asgi_gzip"],
    install_requires=[],
    extras_require={"test": ["pytest", "starlette", "requests", "trio", "httpx"]},
    python_requires=">=3.7",
)
