import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "picar",
    version = "0.0.1",
    author = "Sun Founder",
    author_email = "",
    description = ("A library to run the Picar-X from Sun Founder."),
    license = "GNU v2",
    keywords = "picar picar-x smartcar",
    url = "",
    packages=['picar'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNUv2 License",
    ],
)
