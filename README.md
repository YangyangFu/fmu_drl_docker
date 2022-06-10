# FMU-DRL

# 1. Description
This is a set of environments that support FMU based deep reinforcement learning environment. 
The FMU can be generated from Dymola, jModelica and EnergyPlus.
The environments are divided into smaller environment following object-oriented syntax to support flexible customization.
Note now only Python 3 is supported, and only jModelica FMU is tested.

**Folder Structure**:
 - `jmodelica`: This folder contain source files for building jModelica in Python 3 from scratch, and examples for how to use.
 - `jmodelica_drl`: This folder contain source files for building jModelica-based deep reinforcment learning environment from scratch, and examples for how to use.

**Supported OS**:

This environment supports all three major OS but with limitations:
   - `Window OS`: Nvidia GPU cannot be called due to 
   - `Mac OS `: Mac usually doesn't have Nvidia GPU
   - `Linux`: works perfectly when Nvidia GPU is available

# 2. Installation
This documentation assumes the reader has necessary knowledge about how to use Docker.

## 2.1 Install jModelica
jModelica is supported in both Python 2 and Python 3, and the source file for building a docker on a local machine is located in `./jmodelica`.

`If the user doesn't want to install everything from scratch`, one can directly pull the image I uploaded in the dockerhub by:
```bash
      docker pull yangyangfu/jmodelica_py3
```
The name can be changed freely by using `docker tag` command after pulling to the local.

`If the user wants to build for fun`, we highly recommend the Python 3 version, and use it as an example here. To install jModelica in Python 3, direct to the subdirectory by

```bash
      cd ./jmodelica/Python3
```

Then call script to build the docker image locally by the following command, which executes the `build` command in the `makefile`, and run the docker building process.
```bash
      make build
```

If the reader wants a different name, please refer to `makefile`, and directly change the name before the build process.
If the build is successful, the docker image will be named `yangyangfu/jmodelica_py3` by checking:
```bash
      docker image ls
```

This would list all the images in the local computer. 
For how to test examples using jModelica, please refer to 3.2.

## 2.2 Install jModelica-based DRL envrionment
jModelica serves as a numerical environment, and the DRL algorithms need to be additionally installed.

`If the user doesn't want to install everything from scratch`, one can directly pull the image I uploaded in the dockerhub by:
```bash
      docker pull yangyangfu/jmodelica_drl_cpu      -> for CPU-only version
      docker pull yangyangfu/jmodelica_drl_gpu      -> for GPU version
```

`If the user wants to build for fun`, direct to the right folder by:
```bash
      cd ./jmodelica-drl/Python3
```

Build the docker image according to the availability of Nvidia GPU in your local computer OS by:
```bash
      make build_cpu
```
or 
```bash
      make build_gpu
```

A successful build would create a corressonding docker image in your local computer:
   - `jmodelica_drl_cpu` for CPU build
   - `jmodelica_drl_gpu` for GPU build

Customized cuda version can be defined in `/jmodelica-drl/Python3/Dockerfile_GPU`.

# 3. Test Examples
Here the docker environment is assumed to be executable on your local computer.

## 3.1 Test jModelica installation
1. open a terminal and navigate to your work directory, such as `jmodelica/Python3`

2. compile a Modelica file in `*.mo` into FMU using jModelica docker by running

```bash
      bash compile_fmu.sh -> for MacOS or Linux
      compile_fmu.bat     -> for windows OS
```

A successful compilation would generate a `*.fmu` file in the current folder.

3. simulate the generated fmu using pyFMI by typing:
```bash
      bash simulate_fmu.sh -> for MacOS or Linux
      simulate_fmu.bat     -> for windows OS
```

## 3.2 Test jModelica-based DRL installation
Here we provide an example using pytorch-based DRL algorithms to control a cart-pole environment modelel in Modelica FMU.
The opengym environment is implemented in `.jmodelica-drl/Python3/gym-tutorial`.
The scripts that run the DRL experiment using DDQN are located at `.jmodelica-drl/Python3/test`.

To run the experiment, type:
```bash
      bash test_cart_pole_ddqn.sh         -> for MacOS or Linux
      test_cart_pole_ddqn.bat             -> for Windows OS 
```

# 4. Use Cases

## 4.1 How to Customize the Docker Environment?

## 4.2 How to Customize OpenGym Environment?


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
