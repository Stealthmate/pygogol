from setuptools import setup

from generate import generate

generate()

setup(name='pygogol',
      version='0.1',
      description='A Google API library',
      url='http://github.com/stealthmate/pygogol.git',
      author='Stealthmate',
      author_email='stealthmate.dev@gmail.com',
      license='MIT',
      packages=['pygogol'],
      install_requires=[
          'google-auth',
      ],
      zip_safe=False)