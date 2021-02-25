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
- **Lower bug count** - By leveraging a well tested and open source code base - developers can cut down on introducing bugs by over 25-30%* 
- **Incorporates METeOR conventions** - The METeOR identifiers have been mapped to user friendly Python `Enum` names. Now remembering the METeOR identifiers you can use these human readable class names out of the box - reducing the possibility of bugs and errors creeping in. 
- **HAC adjustment computations** - The detailed steps of the HAC computations 
- **Remoteness calculations** - The detailed steps of the remoteness calculations (from postcode and SA2 address have been incorporated to enable automatic mapping to the RA16 remoteness class)

<small>* based on the experience of the internal dev-team and bugs caught and resolved via type checking and testing during development.
- [HAC]: hosptial acquired complications
- [IHPA]: Independent hospital pricing authority
- [METeOR]:  Metadata online registry 
- [ABF]: Activity based funding
- [NEP]: National efficient price

It is assumed that you are familiar with 
    - python 
    - the terminology and concepts of ABF.