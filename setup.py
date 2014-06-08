# encoding: utf-8

from __future__ import absolute_import, print_function
import postboy

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

long_description="""
PostBoy
=======

Simple distributed emailing system. Consists of broker (based on pyzmq) and worker.

Installation
++++++++++++

pip install postboy

Using
+++++

    /usr/bin/postboy-broker --debug
    /usr/bin/postboy-worker --debug

    /usr/bin/env python
    Python 2.7.6 (default, Apr  9 2014, 11:48:52)
    >>> from postboy import Email, BrokerHandler
    >>> broker = BrokerHandler()
    >>> email = Email(sender='info@test.name', recipient='user@localhost', subject='Test')
    >>> broker.store(email.dumps())
    1 # <= return task id

"""

setup(name='postboy',
    version=postboy.__version__,
    author=postboy.__author__,
    author_email='me@mosquito.su',
    license="MIT",
    description="postboy - simple distributed emailing system.",
    platforms="all",
    url="http://github.com/mosquito/postboy",
    classifiers=[
      'Environment :: Console',
      'Programming Language :: Python',
    ],
    long_description=long_description,
    packages=[
      'postboy',
    ],
    scripts=['bin/postboy-broker', 'bin/postboy-worker'],
    install_requires=[
        'pyzmq'
    ]
)