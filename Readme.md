# Site check

This project uses https://lets-cli.org/ task runner.

Install `lets` https://lets-cli.org/docs/installation.

How to use https://lets-cli.org/docs/getting_started

## Run

Python >= 3.8 required

1. Create venv

```shell
lets vevn
```

2. Run checked/producer

```shell
lets checker
```

3. Run consumer

```shell
lets consumer
```

## Test

```shell
lets test
```


## Dependencies

This project uses https://github.com/jazzband/pip-tools

To update all dependencies run:

```shell
lets update-deps
```

To update one package run:

```shell
lets update-deps pytest
```

This will regenerate requirements.txt
