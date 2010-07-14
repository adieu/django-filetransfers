from setuptools import setup, find_packages

DESCRIPTION = 'Helper for writing reusable Django apps that handle uploads and downloads'

LONG_DESCRIPTION = None
try:
    LONG_DESCRIPTION = open('README.rst').read()
except:
    pass

setup(name='django-filetransfers',
      packages=find_packages(exclude=('tests', 'tests.*')),
      author='Waldemar Kornewald',
      url='http://www.allbuttonspressed.com/projects/django-filetransfers',
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      platforms=['any'],
      install_requires=[],
)
