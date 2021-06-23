import os
from setuptools import setup, find_packages


def readme():
    with open("README.md") as f:
        return f.read()


PACKAGE_NAME = "yiopypi"
HERE = os.path.abspath(os.path.dirname(__file__))
VERSION = "0.0.1"

PACKAGES = find_packages(exclude=["tests", "tests.*", "dist", "ccu", "build"])

REQUIRES = []

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    license="MIT License",
    url="https://github.com/YIO-Remote/yiopypi",
    author="Marton Borzak",
    author_email="marton@yio-remote.com",
    description="YIO Remote V2 API python library",
    packages=PACKAGES,
    include_package_data=True,
    zip_safe=False,
    platforms="any",
    install_requires=REQUIRES,
    keywords=["yio", "yioremote"],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.4",
    ],
)
