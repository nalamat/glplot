#!/usr/bin/env python

from distutils.core import setup

setup(
    name='glplot',
    version='1.0',
    description='Real-time GPU-accelerated plotting library',
    author='Nima Alamatsaz',
    author_email='nima.alamatsaz@gmail.com',
    url='https://github.com/nalamat/glplot',
    py_modules=['glplot'],
    install_requires=[
        'numpy',
        'scipy',
        # 'qt~=5.0',
        'pyopengl',
        'pype',
        ],
    )
