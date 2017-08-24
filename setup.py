from setuptools import setup

setup(
    name='ExpandObjects',
    version='0.1',
    author="Edwin Lee",
    author_email="edwin.lee@nrel.gov",
    packages=['expandobjects', ],
    long_description=open('README.md').read(),
    test_suite='nose.collector',
    tests_require=['nose'],
)
