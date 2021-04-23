# Site check

This project uses https://lets-cli.org/ task runner.

Install `lets` https://lets-cli.org/docs/installation.

How to use https://lets-cli.org/docs/getting_started


## Architecture

![alt text](./docs/site_check_arch.png)

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
lets checker https://google.com \
  --interval=1 \
  --kafka-bootstrap=kafka-site-check-project-7d36.aivencloud.com:13611 \
  --kafka-topic=checks \
  --kafka-ca-path=./certs/ca.pem \
  --kafka-cert-path=./certs/service.cert \
  --kafka-key-path=./certs/service.key
```

3. Run consumer 


Before first run we have to migrate database schema

```shell
lets migrate-up
# or 
lets migrate-up 1 # where 1 is number of specific migration
```

Or `lets migrate-down` to rollback all migrations

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
lets consumer \
  --kafka-bootstrap=kafka-site-check-project-7d36.aivencloud.com:13611 \
  --kafka-topic=checks \
  --kafka-ca-path=./certs/ca.pem \
  --kafka-cert-path=./certs/service.cert \
  --kafka-key-path=./certs/service.key \
  --postgres-uri="postgres://user:password@pg-site-check-project-7d36.aivencloud.com:13609/site_check?sslmode=require"
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
