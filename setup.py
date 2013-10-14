#!/usr/bin/env python
from setuptools import setup

setup(
    name='mdx_textalign',
    version='1.0',
    author='Andrew Horn',
    author_email='andrewphorn@gmail.com',
    description='Python-Markdown extension to support centering and right-aligning text.',
    url='https://github.com/andrewphorn/markdown.textalign',
    py_modules=['mdx_textalign'],
    install_requires=['Markdown>=2.0',],
    classifiers=[
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Markup :: HTML'
    ]
)