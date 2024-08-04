# Testing Guide

## Unit Tests

Unit tests ensure that individual components work as expected. They are located in the  folder. To run unit tests, use the following command:

```sh
python -m unittest discover -s tests/unit
```

## Integration Tests

Integration tests verify that different parts of the application work together correctly. They are located in the  folder. To run integration tests, use the following command:

```sh
python -m unittest discover -s tests/integration
```

## User Acceptance Tests (UAT)

UAT ensures the application meets end-user requirements. They are located in the  folder. To run UAT, use the following command:

```sh
python -m unittest discover -s tests/uat
```
