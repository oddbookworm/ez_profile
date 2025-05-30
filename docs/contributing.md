# Contributing

First of all, thank you for considering to contribute. It means a lot to me! To contribute, make sure to
follow the steps given below.

## Building

To build ez_profile, you first need to fork this repository. Then you need to clone it using this command

```sh
git clone https://github.com/<your-username>/ez_profile.git
```

After this, enter the ez_profile folder:

```sh
cd ez_profile
```

If you want to contribute, you need to create a separate branch from `dev` which would later be merged into `dev`.

```sh
git checkout dev
git branch <descriptive_branch_name>
git checkout <descriptive_branch_name>
```

Now make whatever changes you want to the source code. When you are done, build it by first installing
the developer dependencies:

```sh
pip install -r requirements.txt
```

Now install using this command:

```sh
pip install .
```

And to install in editable mode:

```sh
pip install -e .
```

When you are done, you can add all your changes which you intend to commit.

```sh
git add .
```

And there you have it! Now you can go to the `ez_profile` repository on GitHub and create a pull request.
Make sure that you merge it into the `dev`, not `main`.

## Contributing Guidelines

- Format your code with `ruff`.
- Make sure your code is styled according to the [PEP 8](https://peps.python.org/pep-0008/) style guide.
- Make sure to give a detailed explanation on what your pull request is about.
