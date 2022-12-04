from setuptools import find_packages, setup

setup(
    name='ez_profile',
    packages=find_packages(include=['ez_profile']),
    version='0.1.0',
    description='A basic wrapper around cProfile with optional snakeviz integration',
    author='oddbookworm',
    license='MIT',
    install_requires=[]
)