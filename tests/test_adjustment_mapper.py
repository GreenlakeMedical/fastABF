from dateutil import relativedelta

import pytest
from fastabf.adjustment_mapper import compute_dialysis_adjustment
from fastabf.datatypes import ABF_Service_Category, MDC_Type


def test_dialysis_adjustment():
    assert compute_dialysis_adjustment(
        abf_service_cat=ABF_Service_Category.emergency_department, bool_dialysis_flag=True) == 0.0
    assert compute_dialysis_adjustment(
        abf_service_cat=ABF_Service_Category.emergency_services, bool_dialysis_flag=True) == 0.0
    assert compute_dialysis_adjustment(
        abf_service_cat=ABF_Service_Category.admitted_acute, bool_dialysis_flag=False) == 0.0
    assert compute_dialysis_adjustment(
        abf_service_cat=ABF_Service_Category.admitted_acute, bool_dialysis_flag=True) == 0.28


def test_compute_paediatric_adj():
    from fastabf.adjustment_mapper import compute_paediatric_adj
    assert compute_paediatric_adj(
        ardrgv10_or_tier2cv5="801A",
        patient_age=relativedelta.relativedelta(years=15, months=5),
        abf_service_cat=ABF_Service_Category.admitted_acute,
        __hosp_paed_flag=True) == 1.53

    assert compute_paediatric_adj(
        ardrgv10_or_tier2cv5="810A",
        patient_age=relativedelta.relativedelta(years=15, months=5),
        abf_service_cat=ABF_Service_Category.admitted_acute,
        __hosp_paed_flag=False) == 1.00


def test_compute_paediatric_adj_raise_ardrg_keyerror():
    from fastabf.adjustment_mapper import compute_paediatric_adj
    with pytest.raises(KeyError):
        compute_paediatric_adj(
            ardrgv10_or_tier2cv5="810A",
            patient_age=relativedelta.relativedelta(years=15, months=5),
            abf_service_cat=ABF_Service_Category.admitted_acute,
            __hosp_paed_flag=True) == 1.53


def test_compute_multidisciplinary_clinic_adj():
    from fastabf.adjustment_mapper import compute_multidisciplinary_clinic_adj
    assert compute_multidisciplinary_clinic_adj(
        abf_service_cat=ABF_Service_Category.nonadmitted,
        bool_non_admitted_multi_hcp_flag=True) == 0.45

    assert compute_multidisciplinary_clinic_adj(
        abf_service_cat=ABF_Service_Category.nonadmitted,
        bool_non_admitted_multi_hcp_flag=False) == 0.0


def test_compute_psychiatric_age_mdc_and_age_and_psych_adj():
    from fastabf.adjustment_mapper import compute_psychiatric_age_adj
    from dateutil import relativedelta
    assert compute_psychiatric_age_adj(
        patient_age=relativedelta.relativedelta(years=15, months=4),
        mdc_type=MDC_Type(19),
        psych_days=2,
        abf_service_cat=ABF_Service_Category.admitted_acute,
        __hosp_paed_flag=False
    ) == 0.44

    assert compute_psychiatric_age_adj(
        patient_age=relativedelta.relativedelta(years=15, months=4),
        mdc_type=MDC_Type(19),
        psych_days=2,
        abf_service_cat=ABF_Service_Category.admitted_acute,
        __hosp_paed_flag=True
    ) == 0.18


def test_compute_multidisciplinary_clinic_adj_error():
    from fastabf.adjustment_mapper import compute_multidisciplinary_clinic_adj
    for abf_service_cat in [
        ABF_Service_Category.admitted_acute, ABF_Service_Category.admitted_nonacute, ABF_Service_Category.emergency_department
    ]:
        with pytest.raises(RuntimeError):
            compute_multidisciplinary_clinic_adj(
                abf_service_cat=abf_service_cat,
                bool_non_admitted_multi_hcp_flag=False)

        with pytest.raises(RuntimeError):
            compute_multidisciplinary_clinic_adj(
                abf_service_cat=abf_service_cat,
                bool_non_admitted_multi_hcp_flag=True)
