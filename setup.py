from setuptools import find_packages, setup

__ver = "0.1.4"

setup(
    name="ez_profile",
    packages=find_packages(include=["ez_profile"]),
    version=__ver,
    description="A basic wrapper around cProfile with optional snakeviz integration",
    author="oddbookworm",
    author_email="andrewryancoffey@hotmail.com",
    license="MIT",
    install_requires=['snakeviz'],
    url="https://github.com/oddbookworm/ez_profile",
    download_url="https://github.com/oddbookworm/ez_profile/archive/refs/tags/v{__ver}.tar.gz",
    keywords=["ez_profile"],
    classifiers=[],
)

# release procedure:
# create github release
# python setup.py sdist
# twine upload dist/*