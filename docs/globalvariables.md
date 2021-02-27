# Global variables

As the fastABF module was created for use by health care providers, there are certain specific variables that do not change from one function call to the other -but which are used
in the ABF computations. These are as indicated below

## Constants fixed for the hospital during setup
The following are constants that can be initialised during setup and take their values from the environment. 

| Constant              | Description                | Environment variable |
| --------------------- | -------------------------- | -------------------- |
| `hosp_state_constant` | type `Hosp_State_Category` | `HOSPITAL_STATE_INT` |
| `HOSP_PAED_FLAG`      | type bool                  | `HOSP_PAED_FLAG`     |
| `hosp_level3ICU_flag` | type bool                  | `HOSP_L3_ICU_FLAG`   |
| `global_NEP`          | type float                 | `NEP`                |

!!! Warning
    During initialisation please set the above environmental variables  accordingly. They 
    affect the price computations but would not need to be changed very often.