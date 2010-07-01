from setuptools import setup
import os

DESCRIPTION = 'Helper for writing reusable Django apps that handle uploads and downloads'

LONG_DESCRIPTION = None
try:
    LONG_DESCRIPTION = open('README.rst').read()
except:
    pass

setup(name='django-filetransfers',
      packages=['filetransfers'],
      author='Waldemar Kornewald',
      url='http://www.allbuttonspressed.com/projects/django-filetransfers',
      include_package_data=True,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      platforms=['any'],
      install_requires=[],
)
