import pytest
from fastabf.DAL import dal_emergency
from fastabf.datatypes import ABF_Service_Category


def test_get_base_bw_emergency_urg():
    assert dal_emergency.get_base_bw_emergency(abf_service_cat=ABF_Service_Category.emergency_department,
                                               urg_v1p4_or_udg_v1p3=10) == 0.2875


def test_get_base_bw_emergency_udg():
    assert dal_emergency.get_base_bw_emergency(abf_service_cat=ABF_Service_Category.emergency_services,
                                               urg_v1p4_or_udg_v1p3=2) == 0.2293
