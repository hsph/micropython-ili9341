import sys
sys.path.pop(0)
from setuptools import setup

setup(
    name="micropython-ili9341",
    py_modules=["ili934xnew"],
    version="0.1.0",
    description="Micropython Driver for ILI9341 display",
    long_description="",
    keywords="micropython tft lcd",
    url="https://github.com/jeffmer/micropython-ili9341",
    author="jeffmer",
    author_email="",
    maintainer="",
    maintainer_email="",
    license="MIT",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: Implementation :: MicroPython",
        "License :: OSI Approved :: MIT License",
    ],
)
