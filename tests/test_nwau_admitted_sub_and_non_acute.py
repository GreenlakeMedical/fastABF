import numpy as np

import pytest
from fastabf.datatypes import Care_Type, Remoteness_Category_RA16
from fastabf.pipelines import nwau_admitted_sub_and_non_acute


def test_nwau_admitted_sub_and_non_acute_abf_price_computation():
    r1 = nwau_admitted_sub_and_non_acute.Admitted_Subacute_Record(
        Birth_Date="23/12/1990",
        Admission_Date="25/09/2020",
        Separation_Date="30/09/2020",
        AN_SNAP_v4="4AA3",
        care_type=Care_Type.acute_care_admitted_care,
        Pat_Postcode="PC00",
        Pat_private_Flag=False,
        EST_Remoteness_Cat=Remoteness_Category_RA16.Inner_Regional,
    )
    abfprice = r1.get_abf_price()
    assert np.round(abfprice, 4) == 10105.34
