"""Tests for data_quality.data_quality_report."""
import pytest

from data_quality import data_quality_report


def test_basic_report():
    rows = [
        {"a": 1, "b": "x"},
        {"a": 2, "b": "y"},
        {"a": None, "b": "z"},
        {"a": 4, "b": None},
    ]
    report = data_quality_report(rows)
    assert report["row_count"] == 4
    assert report["column_count"] == 2
    assert report["missing_counts"]["a"] == 1
    assert report["missing_counts"]["b"] == 1
    assert report["missing_fraction"]["a"] == 0.25
    assert report["missing_fraction"]["b"] == 0.25
    assert report["duplicate_rows"] == 0


def test_empty_rows():
    report = data_quality_report([])
    assert report["row_count"] == 0
    assert report["column_count"] == 0
    assert report["missing_counts"] == {}
    assert report["missing_fraction"] == {}
    assert report["duplicate_rows"] == 0


def test_duplicate_rows():
    rows = [
        {"a": 1, "b": "x"},
        {"a": 1, "b": "x"},
        {"a": 2, "b": "y"},
    ]
    report = data_quality_report(rows)
    assert report["duplicate_rows"] == 1


def test_all_missing_column():
    rows = [
        {"a": None, "b": 1},
        {"a": None, "b": 2},
    ]
    report = data_quality_report(rows)
    assert report["missing_counts"]["a"] == 2
    assert report["missing_fraction"]["a"] == 1.0
    assert report["missing_fraction"]["b"] == 0.0


def test_non_iterable_raises():
    with pytest.raises(TypeError):
        data_quality_report(123)


def test_columns_with_only_missing():
    rows = [
        {"a": None, "b": None},
        {"a": None, "b": None},
    ]
    report = data_quality_report(rows)
    assert report["missing_counts"] == {"a": 2, "b": 2}
    assert report["missing_fraction"] == {"a": 1.0, "b": 1.0}
