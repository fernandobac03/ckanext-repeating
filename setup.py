from setuptools import setup, find_packages
import sys, os

version = '0.0.1'

setup(
    name='ckanext-repeating',
    version=version,
    description="Repeating fields for CKAN",
    long_description="""
    """,
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Government of Canada',
    author_email='Michel.Gendron@statcan.gc.ca',
    url='',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.repeating'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points=\
    """
    [ckan.plugins]
    repeating=ckanext.repeating.plugins:RepeatingPlugin
    """,
)
