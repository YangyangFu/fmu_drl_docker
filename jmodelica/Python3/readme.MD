# Description

No open-source jModelica in Python 3 is available. The provided source code for JModelica in github cannot be sucessfully compiled.
The workaround to use jModelica in python3 is using a python conda environment:

1. compile Modelica models to FMUs in python 2
2. simulate fmu in conda Python 3 using PYFMI

