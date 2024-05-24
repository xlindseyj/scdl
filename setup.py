#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from os import path

from setuptools import find_packages, setup

import scdl

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="scdl",
    version=scdl.__version__,
    packages=find_packages(),
    include_package_data=True,
    author="FlyinGrub & xlindseyj",
    author_email="flyinggrub@gmail.com",
    description="Download Music from Souncloud",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "docopt",
        "mutagen>=1.45.0",
        "termcolor",
        "requests",
        "clint",
        "pathvalidate",
        "soundcloud-v2>=1.3.7"
    ],
    url="https://github.com/xlindseyj/scdl",
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Internet",
        "Topic :: Multimedia :: Sound/Audio",
    ],
    python_requires = ">=3.7",
    entry_points={
        "console_scripts": [
            "scdl = scdl.scdl:main",
        ],
    },
)
