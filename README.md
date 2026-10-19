# NLP Classification Pipeline

[![CI](https://github.com/ayusprasad/learning_pipeline/actions/workflows/ci.yml/badge.svg)](https://github.com/ayusprasad/learning_pipeline/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)
![DVC](https://img.shields.io/badge/DVC-Reproducible%20pipeline-945DD6?logo=dvc&logoColor=white)
![scikit--learn](https://img.shields.io/badge/ML-scikit--learn-F7931E?logo=scikitlearn&logoColor=white)

A DVC-managed natural-language classification pipeline that ingests text data, preprocesses it, builds TF-IDF features, trains a classifier, and records evaluation metrics.

## Pipeline

~~~text
data ingestion → preprocessing → TF-IDF features → model training → evaluation / DVC Live
~~~

Parameters are stored in params.yaml and stage dependencies are described in dvc.yaml. Source data is managed with DVC and must be available through a configured remote before running the complete pipeline.

## Run locally

### Prerequisites

- Python 3.11 or newer
- Git and DVC

### Install and run

~~~bash
git clone https://github.com/ayusprasad/learning_pipeline.git
cd learning_pipeline
python -m venv .venv
python -m pip install -r requirements.txt
dvc repro
~~~

Configure or pull the DVC-managed source data before running dvc repro. The pipeline writes intermediate data, model artifacts, logs, and evaluation metrics locally.

## Quality checks

~~~bash
pytest -q
ruff check --select E4,E7,E9,F src tests
python -m compileall -q src tests
~~~

GitHub Actions validates the pipeline configuration, lints source files, runs unit checks, and compiles the project without accessing a DVC remote.
