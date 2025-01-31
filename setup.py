# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from setuptools import setup, find_packages

setup(
    name='sccl',
    version='2.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'sccl = sccl.__main__:main',
        ],
    },
    install_requires=[
        'dataclasses; python_version < "3.7"',
        'z3-solver',
        'argcomplete',
        'lxml',
    ],
    python_requires='>=3.6',
)
