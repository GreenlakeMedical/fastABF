import numpy as np

import pytest
from fastabf.datatypes import Sex_Category
from fastabf.HACpackage import hac_helper, hac_processor
from fastabf.HACpackage.hac_processor import (HAC_Category,
                                              HAC_Complexity_Category)


def test_get_age_based_hac_complexity_read_OK():
    assert hac_helper.get_age_based_hac_complexity(
        23, HAC_Category.Delirium) == 4.7151
    assert hac_helper.get_age_based_hac_complexity(
        22, HAC_Category.Delirium
    ) == hac_helper.get_age_based_hac_complexity(21, HAC_Category.Delirium)

    assert hac_helper.get_age_based_hac_complexity(
        0, HAC_Category.Fourth_degree_perineal_laceration_during_delivery
    ) != hac_helper.get_age_based_hac_complexity(
        98, HAC_Category.Fourth_degree_perineal_laceration_during_delivery
    )
    assert (
        hac_helper.get_age_based_hac_complexity(
            0, HAC_Category.Fourth_degree_perineal_laceration_during_delivery
        )
        == 5.3001
    )


def test_get_baselinecomplexity_for_hac_read_OK():
    assert hac_helper.get_baselinecomplexity_for_hac(
        HAC_Category.Pressure_injury) == 50.3176


def test_get_drg_type_complexity_adjustment_for_HAC_read_OK():
    assert (
        hac_helper.get_drg_type_complexity_adjustment_for_HAC(
            HAC_Category.Falls_resulting_in_fracture_or_intracranial_injury, True
        )
        == 4.4895
    )


def test_get_gender_complexity_adjustment_for_HAC_read_OK():
    assert (
        hac_helper.get_gender_complexity_adjustment_for_HAC(
            HAC_Category.Cardiac_complications, Sex_Category.Female
        )
        == 0
    )


def test_get_adjustment_after_damping_read_OK():
    assert hac_helper.get_adjustment_after_damping(
        HAC_Category.Pressure_injury, HAC_Complexity_Category.Low) == 0.11


def test_compute_adjustment_to_apply_example27yo_female_hac2():
    from fastabf.datatypes import MDC_Type
    hac_res = hac_processor.compute_adjustment_to_apply(
        age=27,
        hac_cat_list=[
            HAC_Category.Falls_resulting_in_fracture_or_intracranial_injury],
        charlson_score=0,
        mdc_cat=MDC_Type.diseases_and_disorders_of_the_hepatobiliary_system_and_pancreas,
        bool_is_intervention=True,
        sex_category=Sex_Category.Female,
        bool_is_emergency_admission=False,   # METeOR id: 269986
        bool_ICU_hours=False,
        bool_is_admission_transfer=False,
        bool_foetal_distress_flag=False,
        bool_instrument_use_flag=False,
        bool_ppop_flag=False,
        bool_prima_flag=False)
    assert np.round(hac_res, 4) == 0.038


def test_compute_adjustment_to_apply_example73yo_male_hac2():
    from fastabf.datatypes import MDC_Type
    hac_res = hac_processor.compute_adjustment_to_apply(
        age=73,
        hac_cat_list=[
            HAC_Category.Falls_resulting_in_fracture_or_intracranial_injury],
        charlson_score=3,
        mdc_cat=MDC_Type.diseases_and_disorders_of_the_respiratory_system,
        bool_is_intervention=True,
        sex_category=Sex_Category.Male,
        bool_is_emergency_admission=True,   # METeOR id: 269986
        bool_ICU_hours=True,
        bool_is_admission_transfer=False,
        bool_foetal_distress_flag=False,
        bool_instrument_use_flag=False,
        bool_ppop_flag=False,
        bool_prima_flag=False)
    assert np.round(hac_res, 4) == 0.026


def test_compute_adjustment_to_apply_example87yo_female_hac2():
    from fastabf.datatypes import MDC_Type
    hac_res = hac_processor.compute_adjustment_to_apply(
        age=87,
        hac_cat_list=[
            HAC_Category.Falls_resulting_in_fracture_or_intracranial_injury],
        charlson_score=7,
        mdc_cat=MDC_Type.diseases_and_disorders_of_the_nervous_system,
        bool_is_intervention=True,
        sex_category=Sex_Category.Female,
        bool_is_emergency_admission=True,   # METeOR id: 269986
        bool_ICU_hours=True,
        bool_is_admission_transfer=False,
        bool_foetal_distress_flag=False,
        bool_instrument_use_flag=False,
        bool_ppop_flag=False,
        bool_prima_flag=False)
    assert np.round(hac_res, 4) == 0.008


def test_compute_adjustment_no_hac():
    from fastabf.datatypes import MDC_Type
    hac_res = hac_processor.compute_adjustment_to_apply(
        age=87,
        hac_cat_list=[],
        charlson_score=7,
        mdc_cat=MDC_Type.diseases_and_disorders_of_the_nervous_system,
        bool_is_intervention=True,
        sex_category=Sex_Category.Female,
        bool_is_emergency_admission=True,   # METeOR id: 269986
        bool_ICU_hours=True,
        bool_is_admission_transfer=False,
        bool_foetal_distress_flag=False,
        bool_instrument_use_flag=False,
        bool_ppop_flag=False,
        bool_prima_flag=False)
    assert np.round(hac_res, 4) == 0.0
