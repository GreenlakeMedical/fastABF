
import numpy as np

import pytest
from fastabf.datatypes import Care_Type, Remoteness_Category_RA16
from fastabf.pipelines import nwau_nonadmitted


def test_nwau_nonadmitted():
    r1 = nwau_nonadmitted.Nonadmitted_Record(
        Birth_Date="23/12/1990",
        Event_Service_Date="25/09/2020",
        Tier2_CV5="10.08",
        Pat_Postcode="PC00",
        Multiple_Healthcare_Provider_Indicator=False,
        EST_Remoteness_Cat=Remoteness_Category_RA16.Inner_Regional,
    )
    abfprice = r1.get_abf_price()
    assert np.round(abfprice, 4) == 227.16400


def test_nwau_nonadmitted_assertion():
    with pytest.raises(ValueError):
        r1 = nwau_nonadmitted.Nonadmitted_Record(
            Birth_Date="23/12/1990",
            Event_Service_Date="25/09/2020",
            Tier2_CV5="10.19",
            Pat_Postcode="PC00",
            Multiple_Healthcare_Provider_Indicator=False,
            EST_Remoteness_Cat=Remoteness_Category_RA16.Inner_Regional,
        )
        r1.compute_all_adjustments()
