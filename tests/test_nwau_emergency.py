import numpy as np

import pytest
from fastabf.datatypes import Care_Type, Remoteness_Category_RA16
from fastabf.pipelines import nwau_emergency


def test_nwau_emergency():
    r1 = nwau_emergency.Emergency_Record(
        Birth_Date="23/12/1990",
        Admission_Date="25/09/2020",
        URG_1p4_or_UDG_v1p3=3,
        Pat_Postcode="PC00",
        EST_Remoteness_Cat=Remoteness_Category_RA16.Inner_Regional,
        Emergency_Care_Level="3A"
    )
    abfprice = r1.get_abf_price()
    assert np.round(abfprice, 4) == 971.432


def test_nwau_emergency_raiseError():
    with pytest.raises(Exception):
        r1 = nwau_emergency.Emergency_Record(
            Birth_Date="23/12/1990",
            Admission_Date="25/09/2020",
            URG_1p4_or_UDG_v1p3='3a',
            Pat_Postcode="PC00",
            EST_Remoteness_Cat=Remoteness_Category_RA16.Inner_Regional,
            Emergency_Care_Level="3A"
        )
        abfprice = r1.get_abf_price()


def test_nwau_emergency_auto_converts_udgurg_to_int():
    r1 = nwau_emergency.Emergency_Record(
        Birth_Date="23/12/1990",
        Admission_Date="25/09/2020",
        URG_1p4_or_UDG_v1p3='3',  # this is a string rather than an int
        Pat_Postcode="PC00",
        EST_Remoteness_Cat=Remoteness_Category_RA16.Inner_Regional,
        Emergency_Care_Level="3A"
    )
    abfprice = r1.get_abf_price()

    assert np.round(abfprice, 4) == 971.432
