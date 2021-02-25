from fastabf.datatypes import Remoteness_Category_RA16
from fastabf.Helpers import helper_remoteness_mappings as remote


def test_postcode_to_remoteness_cat_mapper():
    assert remote.postcode_to_ra16mapper[812] == Remoteness_Category_RA16.Outer_Regional
    assert remote.get_remoteness_cat_for_postcode(
        812) == Remoteness_Category_RA16.Outer_Regional
    assert remote.get_remoteness_cat_for_postcode(
        8132) == Remoteness_Category_RA16.Unknown


def test_get_remoteness_cat_for_SA2():
    assert remote.get_remoteness_cat_for_SA2(
        109011172) == Remoteness_Category_RA16.Inner_Regional
    assert remote.get_remoteness_cat_for_SA2(
        1091172) == Remoteness_Category_RA16.Unknown
