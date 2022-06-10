# Description

No open-source jModelica in Python 3 is available. 
The provided source code for JModelica in github cannot be sucessfully compiled.
A workaround to use jModelica in python3 is using a Python conda environment to switch between Python 2 and Python 3 inside the docker image when necessary:

- Python 2: call jModelica to `compile` Modelica models to FMUs 
- Python 3: call pyFMI to `simulate` the generated FMUs

The default version of Python is Python 3.
