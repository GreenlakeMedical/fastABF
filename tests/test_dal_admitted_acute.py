

import pytest
from fastabf.DAL import dal_admitted_acute


def test_get_paed_adj_factor_admitted_acute():
    assert dal_admitted_acute.get_paed_adj_factor_admitted_acute("A14C") == 1.0
    assert dal_admitted_acute.get_paed_adj_factor_admitted_acute(
        "801A") == 1.53


def test_dal_lookup_same_day_sanity_check():
    assert(
        set(
            [_.strip() for _ in dal_admitted_acute.lookup_is_same_day_drg.unique().tolist()
             ]) ==
        set(["YES", ""])
    )


def test_get_mdc_for_ardrgv10():
    assert dal_admitted_acute.get_mdc_for_ardrgv10(
        "I68") == dal_admitted_acute.MDC_Type.diseases_and_disorders_of_the_musculoskeletal_system_and_connective_tissue


def test_get_drg_stay_bounds():
    assert dal_admitted_acute.get_drg_stay_bounds('I68B') == (1, 5)


def test_get_private_patient_service_adjustment_lookup():
    assert dal_admitted_acute.get_private_patient_service_adjustment(
        "801B") == 0.16
    assert dal_admitted_acute.get_private_patient_service_adjustment(
        "Z63B") == 0.21
    try:
        _ = dal_admitted_acute.get_private_patient_service_adjustment(
            "063B")
    except Exception as E1:
        assert isinstance(E1, KeyError)


def test_only3letters_used_in_drgmdcmapper():
    uniqueelements = list(
        set([len(_) for _ in dal_admitted_acute.df_adrg_mdc_mapper.index.tolist()]))
    assert len(uniqueelements) == 1
    assert uniqueelements[0] == 3, 'expected only 3 chars in drg to be taken for MDC'
