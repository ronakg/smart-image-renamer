===================
smart-image-renamer
===================

.. image:: https://travis-ci.org/ronakg/smart-image-renamer.svg?branch=master
   :alt: Current build status
   :target: http://travis-ci.org/#!/ronakg/smart-image-renamer

A script to intelligently bulk rename images using EXIF data contained within

Install
=======

To install smart-image-renamer:

Recommended method is via pip.

::

  pip install smart-image-renamer

Else install like any other python package.

::

  python setup.py install

Usage
=====

::
  
  usage: smart-image-renamer.py [-h] -f FORMAT [-s SEQUENCE] [-r] [-i] [-t] [-V]
                              [-v | -q]
                              input [input ...]

  Smart Image Renamer
  
  Rename your photos in bulk using information stored in EXIF.
  
  positional arguments:
    input          Absolute path to file or directory
  
  optional arguments:
    -h, --help     show this help message and exit
    -f FORMAT      Format of the new file name
    -s SEQUENCE    Starting sequence number (default: 1)
    -r             Recursive mode
    -i             Include hidden files
    -t             Test mode. Don't apply changes.
    -V, --version  show program's version number and exit
    -v, --verbose
    -q, --quiet
  
  Format string for the file name is defined by a mix of custom text and following tags enclosed in {}:
    YYYY        Year
    MM          Month
    DD          Day
    hh          Hours
    mm          Minutes
    ss          Seconds
    Seq         Sequence number
    Artist      Artist
    Make        Camera Make
    Model       Camera Model
    Folder      Parent folder of the image file
  
  Examples:
    Format String:          {YYYY}-{MM}-{DD}-{Folder}-{Seq}
    File Name:              2014-05-09-Wedding_Shoot-001.JPEG
                            2014-05-09-Wedding_Shoot-002.JPEG
  
    Format String:          {YYYY}{DD}{MM}_{Model}_Beach_Shoot_{Seq}
    File Name:              20140429_PENTAX K-x_Beach_Shoot_001.JPEG
                            20140429_PENTAX K-x_Beach_Shoot_002.JPEG
