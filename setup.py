#!/usr/bin/env python

try:
    import setuptools
    from setuptools import setup, find_packages
except ImportError:
    import sys
    print("Please install setuptools.")
    sys.exit(1)

f = open('README.rst')
__doc__ = f.read()
f.close()

VERSION = "1.0.1"

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "License :: OSI Approved :: Apache Software License",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Topic :: Software Development",
    "Topic :: Software Development :: Libraries",
]

setup(
    name='Marguerite',
    version=VERSION,
    description='Marguerite provides a declarative, consistent accessor to data layer.',
    long_description=__doc__,
    author='teitei-tk',
    author_email='teitei.tk@gmail.com',
    url='https://github.com/teitei-tk/Marguerite',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    classifiers=classifiers,
    install_requires=open('requirements.txt').read().splitlines(),
    keywords=['Marguerite', 'dispatcher', 'architecture'],
    download_url='https://github.com/teitei-tk/Marguerite/archive/master.tar.gz'
)
