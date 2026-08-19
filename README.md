# Airflow Astro Project

An Apache Airflow project scaffolded for the Astronomer Runtime, with DAGs, tests, Docker configuration, and local development support.

## Overview

This repository is an Astro/Astronomer Airflow project. Workflows are defined as Python DAGs under `dags/`, with the project packaged and run locally through the Astro CLI and Docker.

## Architecture

```text
                 Astro / Docker
                       |
        +--------------+--------------+
        |              |              |
     Scheduler      DAG Processor   API Server
        |              |              |
        +--------------+--------------+
                       |
                    Triggerer
                       |
                    Postgres
              (Airflow metadata DB)
                       |
                       v
                 Python DAGs
```

## Repository Structure

- `dags/` — Airflow DAG definitions.
- `tests/` — DAG/project tests.
- `Dockerfile` — Astro Runtime image configuration.
- `requirements.txt` — Python dependencies.
- `packages.txt` — OS-level packages.
- `include/` — additional project files when required.
- `.astro/` — Astro project metadata/configuration.

## Local Development

Install the Astro CLI, then start the project:

```bash
astro dev start
```

The local Airflow UI is available at:

```text
http://localhost:8080
```

The Astro development environment runs Airflow components in Docker containers, including the scheduler, DAG processor, API server, triggerer, and PostgreSQL metadata database.

## DAG Development

Add or modify Python workflows under `dags/`. Keep DAGs focused on orchestration and move reusable business logic into testable Python modules where appropriate.

## Testing

Project tests are located under `tests/`. Run the repository's configured test suite from the project environment before deploying workflow changes.

## Deployment

The repository can be deployed through Astronomer. Keep deployment credentials and environment-specific connections outside source control.

## Project Status

This is an Airflow/Astro workflow project suitable for learning and building scheduled data-processing pipelines. The `dags/` directory is the primary location for workflow development.
