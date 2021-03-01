
# Introduction

fastABF is a fast and robust computation module for activity based funding (ABF). It helps to 
streamline the computation of ABF activities as per the National Efficient Price (NEP) 20-21 framework guidelines.  It covers the following major ABF activity types

- admitted acute
- admitted sub/non-acute
- non-admitted
- emergency department or emergency service
---
## Features

- **Fast to setup** - go from start to computing an example ABF episode within 5 minutes. Save *close to a month* of development and testing time!
- **Robust** - with python type hints, strong version control (via Poetry) and strong test coverage, the code base has been prepared with production readiness for backend systems in mind.
- **Easy to understand and extend** - numerous comments and well structured code organisation, ensure that health IT developers can easily use and extend these modules. 
- **Pain free** - The code aims to distill the numerous computations detailed in the IHPA NEP 20-21 computation documentation and guidelines into ready to use packages. As those technical documents spans over **60 pages** (in addition to the HAC computation guidelines which themselves span **over 40 pages**), the creation of fastABF has required a considerable amount of effort. This effort is time that *you* can now save for making other innovative contributions (or taking several long walks :) ). 
- **Lower bug count** - By leveraging a well tested and open source code base - developers can reduce the chance of introducing bugs into their ABF calculations by over 25-30% [^1] 
- **Incorporates METeOR conventions** - The METeOR identifiers have been mapped to user friendly Python `Enum` names. Now instead of remembering the METeOR numerical identifiers you can use these human readable class names  - reducing the possibility of bugs and errors creeping in. 
- **HAC adjustment computations** - The detailed steps of the HAC adjustments (derived from the detailed HAC guidelines) are included as well. In addition the HAC are modeled using an easily reusable `Enum` class.
- **Remoteness calculations** - This code also contains the steps to obtain the remoteness values (from postcode and SA2 address). Hence it enables automatic extraction of the RA16 remoteness class)
- **Helper functions** - We have constructed helper functions to simplify workflow (e.g. a Charlson score calculator, remoteness calculators etc) aimed at simplifying future development.

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


!!! info "Version"
    fastABF requires `python 3.7` or higher. 


## Quick-start
Lets see how you can get started using fastABF in under 5 minutes! 
```
> pip install fastabf 
```
That installs fastabf.  Now we get on with using it. 

Open up a python shell or notebook and type in the following (or copy-paste it from the box below)
``` python

from fastabf.datatypes import (ABF_Service_Category, Care_Type,
                               Remoteness_Category_RA16)
from fastabf.pipelines.nwau_admitted_acute import Admitted_Acute_Record

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
```

!!! check "Nicely done!"
    In just 5 minutes you have computed the ABF price for an admitted acute episode that included various hospital acquired complication flags, location adjustments etc. This required over **20 steps** behind the scenes. The power of using this toolbox is that all of them were orchestrated for you. 


!!! Tip "Important"
    Please note that there are a few values that are unique to each hospital and must be set  accordingly. They affect the price computations but would not need to be changed very often. Refer to the [global variables ](globalvariables.md) section to learn more.

## Licensing
This project is licensed under the **open source** terms of the AGPLv3.0 license. 

!!! note
    For healthcare providers and IT departments who need a proprietary license please contact the [Greenlake Medical team](mailto: contact@greenlakemedical.ai) for more information.
