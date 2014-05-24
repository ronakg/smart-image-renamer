""" Install script for pyShortUrl """

import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "smart-image-renamer",
    version = "0.1",
    author = "Ronak Gandhi",
    author_email = "ronak.gandhi@ronakg.com",
    description = ("A script to intelligently bulk rename images using EXIF data contained within."),
    license = "GPLv2",
    keywords = "image photo rename bulk smart exif",
    platforms = ['Linux', 'Max OS X', 'Windows', 'BSD', 'Unix'],
    url = "https://github.com/ronakg/smart-image-renamer",
    data_files=[
        ('.', ['README.md']),
      ],
    packages = [],
    long_description = read('README.md'),
    scripts=['smart-image-renamer.py'],
    install_requires=['pillow'],
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Other Audience",
        "License :: OSI Approved :: GPLv2 License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Image Processing",
        "Topic :: File Processing",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
)
