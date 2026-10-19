from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def test_pipeline_defines_expected_ordered_stages() -> None:
    pipeline = yaml.safe_load((ROOT / "dvc.yaml").read_text(encoding="utf-8"))
    assert list(pipeline["stages"]) == [
        "data_ingestion",
        "data_preprocessing",
        "feature_engineering",
        "model_building",
        "model_evaluation",
    ]


def test_pipeline_parameters_are_present() -> None:
    parameters = yaml.safe_load((ROOT / "params.yaml").read_text(encoding="utf-8"))
    assert parameters["data_ingestion"]["test_size"] > 0
    assert parameters["model_building"]["n_estimators"] > 0
