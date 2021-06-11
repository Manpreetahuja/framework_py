# Python Test Auotmaiton project

This is simple test automation project built on python. it primarily uses python-behave frameowrk to execute BDD scenarios. 

## project Structure

- **./config** : contains the project configuration 
    - driver location
    - reporting format
    - reports folder

- **./features** : contains feature files *this needs to be maintained ina separate application project and should not be part of the framework*
    - **/stesp** : this would also be part of teh application project and not teh framework. it appears in the framework structire for testing purpose. **Place it anywhere in th directiry and pass the path as argument, the scenarios should still run fine**

- **./reports** : contains the allure reports that aalure-behave produces after execution. the report is in JSON format and captures time of execution, scenario name, feature name, steps, pass/fail status etc.

- **./resources** : contains the driver and other required resouces of teh application project. this should also be part of the application project.it appears in the framework structire for testing purpose

- **./runner** : This package would continue to stay in the framework project. this has runner method implementation and other helper modules to facilitate scenaio execution

- **.gitignore** : please mention files that needs to be ignored from git commit

- **README.md** : this file provides instruction

- **requirement.txt** : this file contains all the libraries required for project installation. **run `pip install -r requirement.txt`** to install all the reuired libraies at once

- **setup.py** : this is the build configuration file needed for building this project and producing a wheel file. this can be used with build commands to build the project and upload to PiPY.
