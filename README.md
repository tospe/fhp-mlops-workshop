# mlops

[![Python](https://img.shields.io/badge/python-3.7+-informational.svg)](<>)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=black)](https://pycqa.github.io/isort)
[![documentation](https://img.shields.io/badge/docs-mkdocs%20material-blue.svg?style=flat)](https://mkdocstrings.github.io)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![mlflow](https://img.shields.io/badge/tracking-mlflow-blue)](https://mlflow.org)
[![dvc](https://img.shields.io/badge/data-dvc-9cf)](https://dvc.org)
[![Hydra](https://img.shields.io/badge/Config-Hydra-89b8cd)](https://hydra.cc)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![pytest](https://img.shields.io/badge/pytest-enabled-brightgreen)](https://github.com/pytest-dev/pytest)
[![conventional-commits](https://img.shields.io/badge/conventional%20commits-1.0.0-yellow)](https://github.com/commitizen-tools/commitizen)

Contents for mlops workshop.

## Prerequisites

You will need:

- `python` (see `pyproject.toml` for full version)
- `Git`
- `Make`
- a `.secrets` file with the required secrets and credentials
- load environment variables from `.env`

## Installation

Clone this repository (requires git ssh keys)

```
git clone --recursive ssh://git@git.fraunhofer.pt/mlops/mlops_training.git
cd mlops_training && git init
```

Install dependencies

```
conda create -y -n mlops_training python=3.8
conda activate mlops_training
```

or if environment already exists

```
conda env create -f environment.yml
conda activate mlops_training
```

And then setup all virtualenv using make file recipe

```
(mlops_training) $ make setup-all
```

Use pre-commit hooks to standardize code formatting of your project and save mental energy.
Simply install pre-commit package and pre-commit hooks with:

```
make install-pre-commit
```

After that your code will be automatically reformatted on every new commit.

## Documentation

Full documentation is available here: [`docs/`](docs).