from setuptools import setup, find_packages
import io
import os

VERSION = "0.1"


def get_long_description():
    with io.open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="validate-utf8",
    description="Python library and CLI for validating UTF-8 text",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    version=VERSION,
    license="Apache License, Version 2.0",
    packages=find_packages(),
    install_requires=["click"],
    setup_requires=["pytest-runner"],
    extras_require={"test": ["pytest"]},
    entry_points="""
        [console_scripts]
        validate-utf8=validate_utf8.cli:cli
    """,
    tests_require=["validate-utf8[test]"],
    url="https://github.com/simonw/validate-utf8",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
