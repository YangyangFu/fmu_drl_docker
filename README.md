# to-do
1. update documentation by adding examples to customize building environment and customize DRL/MPC formulations

# docker_gym_pytorch_jmodelica
Docker file for OpenAI gym, pyTorch and jModelica. This is the virtual environment for deep reinforcement learning control on a Modelica/EnergyPlus environment.

# Description
This is a set of environments that support jModelica based deep reinforcement learning environment. 
The environments are divided into smaller environment following object-oriented syntax to support flexible customization.
Note now only Python 3 is supported.

Folder structure:
 - `jmodelica`: This folder contain source files for building jModelica in Python 3 from scratch, and examples for how to use.
 - `jmodelica_drl`: This folder contain source files for building jModelica-based deep reinforcment learning environment from scratch, and examples for how to use.
   
# Run Example
Here the docker environment is assumed to be executable on your local computer.

1. open a terminal and navigate to your work directory. For example, if we want to test the integrated enviroment of OpenGym, Pytorch and JModelica, we should direct to `your\folder\gym_python_jmodelica/Python2`

2. build a local docker container from docker file. This steo uses the `Dockerfile` and `makefile` in the current directory.

      `make build`

3. after a sucessful build, we can test the docker environment by running the given examples in `run.sh`. The bash file calls a python script, e.g., `test_gym_torch.py`. Running the bash file can be realized by typing:

      `bash run.sh`

You should be able to go.

# How to Customize the Environment


# Cite
If you find this framework helps your research, please consider to cite:
```
Yangyang Fu, Shichao Xu, Qi Zhu, and Zheng O’Neill. 2021. Containerized
Framework for Building Control Performance Comparisons:
Model Predictive Control vs Deep Reinforcement Learning
Control. In Proceedings of The 8th ACM International Conference
on Systems for Energy-Efficient Buildings, Cities, and Transportation
(BuildSys), Nov 17-18, 2021, Coimbra, Portugal. ACM, New York, NY,
USA, 5 pages. https://doi.org/10.1145/3486611.3492412.
