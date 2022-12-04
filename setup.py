from setuptools import find_packages, setup

setup(
    name="ez_profile",
    packages=find_packages(include=["ez_profile"]),
    version="0.1.2",
    description="A basic wrapper around cProfile with optional snakeviz integration",
    author="oddbookworm",
    author_email="andrewryancoffey@hotmail.com",
    license="MIT",
    install_requires=['snakeviz'],
    url="https://github.com/oddbookworm/ez_profile",
    download_url="https://github.com/oddbookworm/ez_profile/archive/refs/tags/v0.1.1.tar.gz",
    keywords=["ez_profile"],
    classifiers=[],
)
