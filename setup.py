from setuptools import find_packages, setup

try:
    import pypandoc
    long_description = pypandoc.convert_file("README.md", "rst")
except (IOError, ImportError):
    long_description = open("README.md").read()

__ver = "0.1.5"

setup(
    name="ez_profile",
    packages=find_packages(include=["ez_profile"]),
    version=__ver,
    description="A basic wrapper around cProfile with optional snakeviz integration",
    long_description=long_description,
    data_files=[('', ['README.md'])],
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