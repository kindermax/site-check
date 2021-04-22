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

Locally

```shell
lets kafka
lets checker https://google.com --interval=1 --kafka-bootstrap=localhost:9093 --kafka-topic=checks
```

Quick check whats going on in local kafka topic:

`lets kafka-console-consumer --bootstrap-server kafka:9092 --topic checks`

---
With cloud provider (Aiven)

```shell
lets checker https://google.com --interval=1 --kafka-bootstrap=localhost:9002 --kafka-topic=checks
```

3. Run consumer 

Locally

```shell
lets kafka # in one terminal
lets postgres  # in another terminal
lets consumer --kafka-bootstrap=localhost:9093 --kafka-topic=checks --postgres-uri=postgres://postgres:postgres@localhost:5432/site_check
```

Quick check whats going on in local kafka topic:

`lets kafka-console-consumer --bootstrap-server kafka:9092 --topic checks`

---
With cloud provider (Aiven)

```shell
lets consumer --kafka-bootstrap=localhost:9002 --kafka-topic=checks --postgres-uri=postgres://postgres:postgres@localhost:5432/site_check
```

## Test

```shell
lets test
```

## Dependencies

This project uses https://github.com/jazzband/pip-tools

To install all dependencies inside venv run:

```shell
lets install-deps
```

To update all dependencies run:

```shell
lets update-deps
```

To update one package run:

```shell
lets update-deps pytest
```

This will regenerate requirements.txt
