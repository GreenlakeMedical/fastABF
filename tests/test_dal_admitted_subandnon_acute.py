import numpy as np

import pytest
from fastabf.DAL import dal_admitted_subandnon_acute
from fastabf.datatypes import Care_Type, StayCategory


def test_get_private_patient_service_adjustment():
    assert dal_admitted_subandnon_acute.get_private_patient_service_adjustment(
        "4AZ2") == 0.036


def test_get_care_type():
    assert dal_admitted_subandnon_acute.get_care_type(
        "4AZ2") == Care_Type.rehabilitation_care_cannot_be_further_categorised


def test_bool_is_same_day_ansnap():
    assert dal_admitted_subandnon_acute.bool_is_same_day_ansnap(
        an_snap_v4="4AA7") == False
    assert dal_admitted_subandnon_acute.bool_is_same_day_ansnap(
        an_snap_v4="4J01") == True


def test_get_ansnap_stay_bounds():
    bnds = dal_admitted_subandnon_acute.get_ansnap_stay_bounds(
        an_snap_v4='4AA1')
    assert (bnds[0] == 8 and bnds[1] == 20)


def test_get_ansnap_stay_bound_raisealert():
    with pytest.raises(KeyError):
        bnds = dal_admitted_subandnon_acute.get_ansnap_stay_bounds(
            an_snap_v4="A14B")


def test_get_same_day_pw():
    pw = dal_admitted_subandnon_acute.get_same_day_pw("4J01")
    assert np.round(pw, 4) == 0.1269


def test_get_inlier_pw():
    inlier_pw = dal_admitted_subandnon_acute.get_inlier_pw(an_snap_v4="4AB7")
    assert np.round(inlier_pw, 4) == 9.8661

    inlier_pw = dal_admitted_subandnon_acute.get_inlier_pw(an_snap_v4="4ES5")
    assert np.round(inlier_pw, 4) == 3.703


def test_get_long_stay_outlier_perdiem():
    long_outlier_pw = dal_admitted_subandnon_acute.get_long_stay_outlier_perdiem(
        an_snap_v4="4A92"
    )
    assert np.round(long_outlier_pw, 4) == 0.1766


def test_get_long_stay_outlier_perdiem_raisealert():
    with pytest.raises(KeyError):
        long_outlier_pw = dal_admitted_subandnon_acute.get_long_stay_outlier_perdiem(
            an_snap_v4="4A2")


def test_get_short_say_outlier_perdiem():
    short_outlier_perdiem = dal_admitted_subandnon_acute.get_short_say_outlier_perdiem(
        '4AB4')
    assert np.round(short_outlier_perdiem, 4) == 0.3816


def test_get_short_say_outlier_perdiem_raisealert():
    with pytest.raises(KeyError):
        short_outlier_perdiem = dal_admitted_subandnon_acute.get_short_say_outlier_perdiem(
            an_snap_v4="4A2")


def test_helper_get_stay_category_sameday():
    assert (
        dal_admitted_subandnon_acute.helper_get_stay_category(
            an_snap_v4='4J01',
            bool_same_day_flag=True,
            los_days=1)
        == StayCategory.same_day
    )


def test_helper_get_stay_category_inlier():
    assert (
        dal_admitted_subandnon_acute.helper_get_stay_category(
            an_snap_v4='4F01',
            bool_same_day_flag=False,
            los_days=25)
        == StayCategory.inlier
    )

    assert (
        dal_admitted_subandnon_acute.helper_get_stay_category(
            an_snap_v4='4F01',
            bool_same_day_flag=False,
            los_days=14)  # on the boundary
        == StayCategory.inlier
    )


def test_helper_get_stay_category_short_stay_outlier():
    assert (
        dal_admitted_subandnon_acute.helper_get_stay_category(
            an_snap_v4='4F01',
            bool_same_day_flag=False,
            los_days=13)
        == StayCategory.short_stay_outlier
    )


def test_helper_get_stay_category_long_stay_outlier():
    assert (
        dal_admitted_subandnon_acute.helper_get_stay_category(
            an_snap_v4='4F01',
            bool_same_day_flag=False,
            los_days=34)
        == StayCategory.long_stay_outlier
    )


# def test_get_ansnap_stay_bounds()
