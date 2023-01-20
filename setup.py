#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from setuptools import setup, find_packages

_here = os.path.dirname(__file__)

# Package meta-data.
REQUIRES_PYTHON = ">=3.4.2"


# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
with open("README.md", "r") as fh:
    long_description = fh.read()


# Where the magic happens:
setup(
    name="spin",
    version="0.0.0",
    description="Human body model for 3D pose estimation",
    long_description=long_description,
    python_requires=REQUIRES_PYTHON,
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3.4.2",
    ],
)
