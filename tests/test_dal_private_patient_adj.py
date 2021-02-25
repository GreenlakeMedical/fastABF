import pytest
from fastabf.DAL import dal_private_patient_adj


def test_get_private_patient_accommodation_adjustment_perdiem():
    from fastabf import datatypes

    assert dal_private_patient_adj.get_private_patient_accommodation_adjustment_perdiem(
        True, datatypes.Hosp_State_Category.Australian_Capital_Territory) == 0.0505

    assert (
        dal_private_patient_adj.get_private_patient_accommodation_adjustment_perdiem(
            False, datatypes.Hosp_State_Category.New_South_Wales)
        == 0.0698
    )
    assert (
        dal_private_patient_adj.get_private_patient_accommodation_adjustment_perdiem(
            True, datatypes.Hosp_State_Category.New_South_Wales)
        == 0.0505
    )
