
# Introduction

fastABF is a fast and robust computation module for activity based funding (ABF). It helps to 
streamline the computation of ABF activities as per the National Efficient Price (NEP) 20-21 framework guidelines.  It covers the following major ABF activity types

- admitted acute
- admitted sub/non-acute
- non-admitted
- emergency department or emergency service

---
## Features

- **Fast to setup** - go from start to computing an example ABF episode within 5 minutes. 
- **Robust** - with python type hints, strong version control (via Poetry) and strong test coverage the code base is ready for use in backend systems.
- **Easy to understand and extend** - numerous comments and well structured organisation, ensure that health IT developers can easily use and extend these modules. 
- **Pain free** - The code implements  the IHPA NEP 20-21 computation documentation and guidelines that span over 60 pages (** in addition the HAC computation guidelines that also span >40 pages** ). This is time that you can spend on developing other tools or taking a walk.
- **Lower bug count** - By leveraging a well tested and open source code base - developers can cut down on introducing bugs by over 25-30% [^1] 
- **Incorporates METeOR conventions** - The METeOR identifiers have been mapped to user friendly Python `Enum` names. Now remembering the METeOR identifiers you can use these human readable class names out of the box - reducing the possibility of bugs and errors creeping in. 
- **HAC adjustment computations** - The detailed steps of the HAC computations 
- **Remoteness calculations** - The detailed steps of the remoteness calculations (from postcode and SA2 address have been incorporated to enable automatic mapping to the RA16 remoteness class)

[^1]: based on the experience of the internal dev-team and bugs caught and resolved via type checking and testing during development.
*[HAC]: hosptial acquired complications
*[IHPA]: Independent hospital pricing authority
*[METeOR]:  Metadata online registry 
*[ABF]: Activity based funding
*[NEP]: National efficient price

!!! note 
    It is assumed that you are familiar with 

    - python at atleast a basic level.
    - the terminology and concepts of ABF.
    
    You can follow along in the quick start example via a code editor, python commandline or a jupyter notebook



## Quick-start
Lets see how you can get started using fastABF in under 5 minutes! 
```
> pip install fastabf 
```
That installs fastabf.  Now we get on with using it. 

Open up a python shell or notebook and type in the following (or copy-paste it from the box below)
``` python
import fastabf

from fastabf.datatypes import (ABF_Service_Category, Care_Type,
                            Remoteness_Category_RA16)
from fastabf.pipelines.nwau_admitted_acute import Admitted_Acute_Record

aar = fastabf.Admitted_Acute_Record(
    Birth_Date="23/12/1990",
    Admission_Date="25/09/2020",
    Separation_Date="30/09/2020",
    AR_DRG_v10="H07B",
    care_type=fastabf.Care_Type.acute_care_admitted_care,
    Pat_Postcode="PC00",
    ICU_hours_L3=0,
    bool_transfer_status=False,
    sex=2, bool_is_emergency_admission=False, bool_foetal_distress_flag=False,
    bool_instrument_use_flag=False, bool_ppop_flag=False, bool_prima_flag=False,
    HAC1=False, HAC2=True, HAC3=False, HAC4=False, HAC6=False, HAC7=False, 
    HAC8=False, HAC9=False, HAC10=False, HAC11=False, HAC12=False,
    HAC13=False, HAC14=False, HAC15p2=False, Charlson_Score=0,
    Pat_private_Flag=False,
    EST_Remoteness_Cat=Remoteness_Category_RA16.Inner_Regional)
    abf_price = aar.get_abf_price()
```

!!! check "Nicely done!"
    In just 5 minutes you have computed the ABF price for an admitted acute episode that included various hospital acquired complication flags, location adjustments etc. This required over **20 steps** behind the scenes. The power of using this toolbox is that all of them were orchestrated for you. 


!!! Tip "Important"
    Before using this in production please note that there are a few values that
    are unique to each hospital and must be set  accordingly. They 
    affect the price computations but would not need to be changed very often.
    Refer to the [global variables ](globalvariables.md) section regarding this.

## Licensing
This project is licensed under the **open source** terms of the AGPLv3.0 license. 

!!! note
    For healthcare providers and IT departments who need a proprietary license please contact the [Greenlake Medical team](mailto: contact@greenlakemedical.ai) for more information.
