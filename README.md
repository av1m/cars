# Cars

[![Cars CI/CD](https://github.com/av1m/cars/actions/workflows/ci.yaml/badge.svg)](https://github.com/av1m/cars/actions/workflows/ci.yaml)
[![Python3.10](https://img.shields.io/badge/Python-3.10-blue)](https://docs.python.org/3/whatsnew/3.10.html)
[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/av1m/cars/blob/master/LICENSE)

## Abstract

This project was conducted as part of an agility course at Paris Dauphine University.
It is not necessarily a very great coherence because the goal was precisely to project into an Ireel world.
However, the "real" inconsistency does not prevent developing a high quality project.
We find thus:

- ABC
- Unit tests
- Code coverage
- Linter (pylint)
- Design Patterns
- Static typing (mypy)
- Formater (black and isort)
- Functional tests (with cucumber and behave)

This project consists of two packages:

1. `cars`
2. `foods`

The link between these two packages reside in the fact that a car can sell food (the Foodtruck concept)

## Get started 🎉

1. Clone the project

    ```bash
    git clone https://github.com/av1m/cars.git
    cd cars
    ```

2. Run make command

    ```bash
    make install
    ```

Test the project

```bash
make test
```

Format the code

```bash
make format
```

Check all useful commands

```bash
make help
```
