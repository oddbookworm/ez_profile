# Contributing

First of all, thank you for considering to contributing. It means alot to me! To contribute, make sure to follow the steps given below.

## Building

To build ez_profile, you first need to fork this repository. Then you need to clone it using this command
```sh
git clone https://github.com/<your-username>/ez_profile/git
```
After this, enter the ez_profile folder:
```sh
cd ez_profile
```
Now make whatever changes you want to the source code. When you are done, build it by first installing the developer dependencies:
```sh
pip install -r requirements.txt
```
Now run this command:
```sh
python setup.py sdist
```
A folder named `dist` should be created and in it, would be the `.tar.gz` file. To install it, go to the main folder and install using this command:
```sh
pip install .
```
And to install in editable mode:
```sh
pip install -e .
```

## Contributing Guidelines

Make sure your code is styled according to the [PEP 8](https://peps.python.org/pep-0008/) style guide.


