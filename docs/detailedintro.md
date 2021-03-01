# Detailed overview

This page describes the parameters for the cases that are of primary interest to developers who want to start using fastABF.


!!! note 
    Readers who wish to *contribute* and extend this library should read this section as well as the section for library developers & contributors.

## Typical workflow

Normally users would like to calculate the ABF prices for episodes. In fastABF this is easily done by gathering various pieces of data required to invoke the corresponding pipeline for each of the ABF cases. In order to know which pieces of data are required and to construct them easily - here is a simple overview of the inputs for each of the four cases


### Admitted acute ABF
Parameters required

``` python
    class Admitted_Acute_Record: 
        Birth_Date: str,  # ddmmyy
        Admission_Date: str,  # ddmmyy
        Separation_Date: str,  # ddmmyy
        AR_DRG_v10: str,

        # [METeOR id: 269976] True if admitted patient transferred from another hospital.
        bool_transfer_status: bool,
        sex: int,  # [METeOR id: 635126]

        # [METeOR id: 269986] True if admission occurred on an emergency basis
        bool_is_emergency_admission: bool,
        bool_foetal_distress_flag: bool,
        bool_instrument_use_flag: bool,
        bool_ppop_flag: bool,
        bool_prima_flag: bool,
        HAC1: bool,
        HAC2: bool,
        HAC3: bool,
        HAC4: bool,
        HAC6: bool,
        HAC7: bool,
        HAC8: bool,
        HAC9: bool,
        HAC10: bool,
        HAC11: bool,
        HAC12: bool,
        HAC13: bool,
        HAC14: bool,
        HAC15p2: bool,
        Charlson_Score: int,
        patient_leave_days: float = 0,
        ICU_hours_L3: float = -1,
        ICU_hours_other: float = 0,
        Psych_Days: float = 0,  # METeOR id: 552375
        Pat_Postcode: str = "",  # Format PCNNNN, METeOR id: 429894
        Pat_SA2: int = 0,  # NNNNNNNNN (9 digit), METeOR id: 469909
        # Establishment's Remoteness Category
        EST_Remoteness_Cat: Remoteness_Category_RA16 = Remoteness_Category_RA16.Unknown,
        Indigenous_Status: Indigenous_Status_Category = \
            Indigenous_Status_Category.Unknown_or_not_stated,

        Pat_Radiotherapy_Flag: bool = False,
        #  Set to True if the patient has any of the ACHI 11th Edition codes
        #  listed in Appendices B and C of the `national efficient
        #  price determination 2020-21` document for radiotherapy relevant codes
        #  else False
        Pat_Dialysis_Flag: bool = False,
        #  Set to True if the patient has any of the ACHI 11th Edition codes
        #  listed in Appendices B and C of the `national efficient
        #  price determination 2020-21` document for dialysis relevant codes
        #  else False

        # Set to True if the patient is an eligible private patient
        Pat_private_Flag: bool = False,

        Pat_Covid19_Flag: bool = False,

        care_type: Care_Type = Care_Type.acute_care_admitted_care
```
### Admitted subacute ABF
Parameters required
``` python
    class Admitted_Subacute_Record:
        Birth_Date: str, # mmddyy
        Admission_Date: str,
        Separation_Date: str,
        AN_SNAP_v4: str,

        # [METeOR id: 269986] True if admission occurred on an emergency basis
        patient_leave_days: float = 0,
        Pat_Postcode: str = "",  # Format PCNNNN, METeOR id: 429894
        Pat_SA2: int = 0,  # NNNNNNNNN (9 digit), METeOR id: 469909
        # Establishment's Remoteness Category
        EST_Remoteness_Cat: Remoteness_Category_RA16 = Remoteness_Category_RA16.Unknown,
        Indigenous_Status: Indigenous_Status_Category = \
            Indigenous_Status_Category.Unknown_or_not_stated,

        Pat_Radiotherapy_Flag: bool = False,
        #  Set to True if the patient has any of the ACHI 11th Edition codes
        #  listed in Appendices B and C of the `national efficient
        #  price determination 2020-21` document for radiotherapy relevant codes
        #  else False
        Pat_Dialysis_Flag: bool = False,
        #  Set to True if the patient has any of the ACHI 11th Edition codes
        #  listed in Appendices B and C of the `national efficient
        #  price determination 2020-21` document for dialysis relevant codes
        #  else False

        # Set to True if the patient is an eligible private patient
        Pat_private_Flag: bool = False,

        Pat_Covid19_Flag: bool = False,
        care_type: Care_Type = Care_Type.acute_care_admitted_care
```

### Emergency  ABF 
Parameters required
``` python
    class Emergency_Record:
        Birth_Date: str,
        Admission_Date: str,
        URG_1p4_or_UDG_v1p3: int,
        Emergency_Care_Level: str,
        Pat_Postcode: str = "",  # Format PCNNNN, METeOR id: 429894
        Pat_SA2: int = 0,  # NNNNNNNNN (9 digit), METeOR id: 469909
        # Establishment's Remoteness Category
        EST_Remoteness_Cat: Remoteness_Category_RA16 = Remoteness_Category_RA16.Unknown,
        Indigenous_Status: Indigenous_Status_Category = \
            Indigenous_Status_Category.Unknown_or_not_stated,

        Pat_Covid19_Flag: bool = False,
        care_type: Care_Type = Care_Type.acute_care_admitted_care
```

### Non admitted ABF
Parameters required
``` python
    class Nonadmitted_Record:
        Birth_Date: str,
        Event_Service_Date: str,
        Tier2_CV5: str,
        patient_leave_days: float = 0,
        Pat_Postcode: str = "",  # Format PCNNNN, METeOR id: 429894
        Pat_SA2: int = 0,  # NNNNNNNNN (9 digit), METeOR id: 469909
        # Establishment's Remoteness Category
        EST_Remoteness_Cat: Remoteness_Category_RA16 = Remoteness_Category_RA16.Unknown,
        Indigenous_Status: Indigenous_Status_Category = \
            Indigenous_Status_Category.Unknown_or_not_stated,
        Multiple_Healthcare_Provider_Indicator: bool = False,

        Pat_Covid19_Flag: bool = False,
            care_type: Care_Type = Care_Type.acute_care_admitted_care
```
The four ABF cases above are located under the pipeline submodule as indicated below

```
fastabf
    └── pipelines (the most important module- contains the main pipelines)
        ├── nwau_admitted_acute.py 
        ├── nwau_admitted_sub_and_non_acute.py
        ├── nwau_emergency.py
        └── nwau_nonadmitted.py
```
### Convenience functions and interfaces
As you may observe from the input parameters in the cases above, they use 
specific classes/data types that were created for convenience. These convenience interfaces help avoid having to remember the METeOR parameter values thereby reducing errors and speeding up code development. 

These user friendly classes and routines can be found at the following locations in the library. 

**Structure of the fastABF library** 

A simplified overview for users of this library is as follows
``` 
.
├── datatypes.py (user friendly interfaces to data types used - more info below)
├── Helpers 
    └── charlson_class.py (computes the charlson complexity, if it is not known)
    └── helper_remoteness_mappings.py (computes remoteness categories)
```

#### Data types
The `datatypes` module contains user friendly mappings to several of the METeOR classes. Instead of having to remember formally designated numbers, you can use these convenient interfaces in your own code.  For the details of the possible values for each category, please refer to the specific section on [data types](datatypes.md).

``` python
class ABF_Service_Category(Enum)
class Care_Type(Enum)  
class Hosp_State_Category(Enum)
class Indigenous_Status_Category(Enum)
class MDC_Type(Enum)
class Remoteness_Category_RA16(Enum)
class Sex_Category(Enum)
class Stay_Category(Enum)
```


*[HAC]: hosptial acquired complications
*[IHPA]: Independent hospital pricing authority
*[METeOR]:  Metadata online registry 
*[ABF]: Activity based funding
*[NEP]: National efficient price


#### Helper functions
The Charlson class helps compute the Charlson complexity in case it is not known apriori. 
Similarly the remoteness mappings help automatically use the right order of priorities to assign a remoteness category to an episode. 