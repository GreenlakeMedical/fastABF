import numpy as np

import pytest
from fastabf.DAL import dal_nonadmitted


def test_get_paed_adj_factor():
    padj = dal_nonadmitted.get_paed_adj_factor(tier2_cv5="10.06")
    assert np.round(padj, 3) == 0.86


def test_get_base_nwau():
    assert dal_nonadmitted.get_base_nwau('10.08') == 0.0427


def test_get_base_nwau_throw_error():
    with pytest.raises(Exception):
        _ = dal_nonadmitted.get_base_nwau('10.19')
