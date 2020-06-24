# docker_gym_pytorch_jmodelica
Docker file for OpenAI gym, pyTorch and jModelica. This is the virtual environment for deep reinforcement learning control on a Modelica/EnergyPlus environment.

# How to use
Here the docker environment is assumed to be executable on your local computer.


1. open a terminal and navigate to your work directory. For example, if we want to test the integrated enviroment of OpenGym, Pytorch and JModelica, we should direct to `your\folder\gym_python_jmodelica/Python2`

2. build a local docker container from docker file. This steo uses the `Dockerfile` and `makefile` in the current directory.

      `make build`

3. after a sucessful build, we can test the docker environment by running the given examples in `run.sh`. The bash file calls a python script, e.g., `test_gym_torch.py`. Running the bash file can be realized by typing:

      `bash run.sh`

You should be able to go.


