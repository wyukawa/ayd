#!/usr/bin/env python
# encoding: utf-8

from setuptools import find_packages, setup

setup(
    name='ayd',
    version='0.0.4',
    description='generate Azkaban Flow',
    long_description=open('README.md').read(),
    author='wyukawa',
    author_email='wyukawa@gmail.com',
    url='https://github.com/wyukawa/ayd',
    license='MIT',
    packages=find_packages(),
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python',
      'Programming Language :: Python :: 2.7',
      'Environment :: Console',
    ],
    install_requires=[
      'cliff',
      'PyYAML'
    ],
    entry_points={
        'console_scripts': [
            'ayd = ayd.main:main'
        ],
        'ayd': [
            'generateFlow = ayd.generate_flow:Generate_Flow',
            'migrate = ayd.migrate:Migrate'
        ]
    },
)

