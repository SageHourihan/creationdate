from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='creationdate',
      version='1.0',
      description='Command line tool',
      long_description=readme(),
      url='https://github.com/SageHourihan/creationdate.git',
      author='Sage Hourihan',
      author_email='samiho97@gmail.com',
      license='MIT',
      packages=['creationdate'],
      entry_points = {
        'console_scripts': ['creation-date=creationdate.command_line:main'],
    }
)
