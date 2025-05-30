from setuptools import find_packages, setup

long_description = open("README.md").read()

__ver = "0.2.0"

setup(
    name="ez_profile",
    packages=find_packages(include=["ez_profile"]),
    version=__ver,
    description="A basic wrapper around cProfile with snakeviz/tuna integration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    data_files=[("", ["README.md"])],
    author="oddbookworm",
    author_email="andrewryancoffey@hotmail.com",
    license="MIT",
    install_requires=["snakeviz", "tuna"],
    url="https://github.com/oddbookworm/ez_profile",
    download_url=f"https://github.com/oddbookworm/ez_profile/archive/refs/tags/v{__ver}.tar.gz",
    keywords=["ez_profile"],
    classifiers=[],
)

# release procedure:
# create github release
# python setup.py sdist
# twine upload dist/*
