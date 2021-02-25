import pytest
from fastabf.Helpers.charlson_class import \
    compute_charlson_score_for_ICD10AM_list


def test_charlson_score_for_c80():
    assert compute_charlson_score_for_ICD10AM_list(["C80", ""]) == 2


def test_charlson_score_for_empty():
    assert compute_charlson_score_for_ICD10AM_list([""]) == 0


def test_charlson_score_for_max_16():
    assert (
        compute_charlson_score_for_ICD10AM_list(
            ["B24", "K766", "C77", "C96", "N053", "G820"]
        )
        == 16
    )


def test_charlson_score_for_duplicates():
    assert compute_charlson_score_for_ICD10AM_list(["B24", "B20"]) == 6
