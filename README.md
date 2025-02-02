## automated-browsing
Before testing this make sure to have the Edge driver installed on your PC
Select Stable Channel:

https://developer.microsoft.com/en-gb/microsoft-edge/tools/webdriver/?cs=578062562&form=MA13LH

### HOW TO SET UP A VIRTUAL ENV 
> pip install virtualenv

> python<version> -m venv <virtual-environment-name>

ex. 
> mkdir projectA 
> cd projectA
> python3.13 -m venv env

### <ins> TO ACTIVATE PYTHON VIRTUAL ENVIRONMENT: </ins>

### WINDOWS

FOR WINDOWS POWERSHELL:

cd into project location

ex.
> "C:\Users\<youruser>\Desktop\automated browsing(2)\project1"

> .\env\Scripts\Activate.ps1

### UNIX/BASH 

MAC/LINUX/UNIX - BASH:

open terminal in project directory 

> source env/Scripts/activate
 
### PACKAGE INSTALLS 

once the virtual environemnt is set up run:

> pip install

if missing import error shows for selenium packages - ignore it. it's just gaslighting you. it should still work 