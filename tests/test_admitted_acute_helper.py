import numpy as np

import pytest
from fastabf.DAL import admitted_acute_helper
from fastabf.datatypes import StayCategory


def test_is_icu_bundled_lookup():
    assert admitted_acute_helper.bool_is_icu_bundled("P01Z") == True


def test_get_base_nwau():
    base_nwau = admitted_acute_helper.get_base_nwau(
        ar_drg_v10="A14A",
        stay_cat=StayCategory.inlier,
        non_icu_los_days=9)
    assert np.round(base_nwau, 4) == 18.8534
