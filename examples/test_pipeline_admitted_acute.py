# This is an example of how to use the fastabf package to compute the ABF for
# admitted acute service

from fastabf.datatypes import (ABF_Service_Category, Care_Type,
                               Remoteness_Category_RA16)
from fastabf.pipelines.nwau_admitted_acute import Admitted_Acute_Record


def example_pipeline_admitted_acute():
    aar = Admitted_Acute_Record(
        Birth_Date="23/12/1990",
        Admission_Date="25/09/2020",
        Separation_Date="30/09/2020",
        AR_DRG_v10="H07B",
        care_type=Care_Type.acute_care_admitted_care,
        Pat_Postcode="PC00",
        ICU_hours_L3=0,
        bool_transfer_status=False,
        sex=2, bool_is_emergency_admission=False, bool_foetal_distress_flag=False,
        bool_instrument_use_flag=False, bool_ppop_flag=False, bool_prima_flag=False,
        HAC1=False, HAC2=True, HAC3=False, HAC4=False, HAC6=False, HAC7=False, HAC8=False,
        HAC9=False, HAC10=False, HAC11=False, HAC12=False, HAC13=False, HAC14=False,
        HAC15p2=False, Charlson_Score=0,
        Pat_private_Flag=False,
        EST_Remoteness_Cat=Remoteness_Category_RA16.Inner_Regional,

    )
    abf_price = aar.get_abf_price()
    print(f"The abf price is {abf_price}")


if __name__ == "__main__":
    example_pipeline_admitted_acute()
