from setuptools import setup

setup(
    name='greet',
    version=1.0,
    packages=['greet'],
    install_requires=['pytest'],
    entry_points={'console_scripts': ['greet = greet.cli.main:main']}
)
