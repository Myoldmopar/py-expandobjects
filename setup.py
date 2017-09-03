import setuptools
import expandobjects


setuptools.setup(
    name='pyexpandobjects',
    version=expandobjects.__version__,
    description='EnergyPlus Expand Objects implementation in Python.',
    author="Edwin Lee",
    author_email="edwin.lee@nrel.gov",
    url='https://github.com/myoldmopar/py-expandobjects',
    packages=['expandobjects', ],
    long_description=open('README.md').read(),
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: Public Domain',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    entry_points={
        'console_scripts': [
            'expand_objects=expandobjects.main:main',
        ],
    },
    install_requires=['pyiddidf==0.5'],
    keywords='cli energyplus templates',
    test_suite='nose.collector',
    tests_require=['nose'],
)
