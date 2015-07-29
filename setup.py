#!/usr/bin/env python
# encoding: utf-8

from setuptools import find_packages, setup

setup(
    name='chaco',
    version='0.0.1',
    description='generate Azkaban Job File',
    long_description=open('README.md').read(),
    author='wyukawa',
    author_email='wyukawa@gmail.com',
    url='https://github.com/wyukawa/chaco',
    license='MIT',
    packages=find_packages(),
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: Apache License',
      'Programming Language :: Python',
      'Programming Language :: Python :: 2.7',
      'Environment :: Console',
    ],
    install_requires=[
      'cliff'
    ],
    entry_points={
        'console_scripts': [
            'chaco = chaco.main:main'
        ],
        'chaco': [
            'generateJob = chaco.generate_job:Generate_Job'
        ]
    },
)

