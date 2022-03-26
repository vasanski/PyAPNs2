#!/usr/bin/env python

from setuptools import setup

setup(
    name='apns2-up',
    version='0.7.3',
    packages=['apns2'],
    install_requires=[
        'hyper-up>=0.8',
        'PyJWT>=2.0.0',
        'cryptography>=1.7.2',
    ],
    extras_require={
        "tests": [
            'freezegun',
            'pytest',
        ],
    },
    url='https://github.com/vasanski/PyAPNs2',
    license='MIT',
    author='Eduard Vasanski',
    author_email='eduard.vasanski@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries',
    ],
    description='A python library for interacting with the Apple Push Notification Service via HTTP/2 protocol'
)
