FROM yangyangfu/jmodelica_py2_gym
LABEL maintainer yangyangfu(yangyang.fu@tamu.edu)

#
USER root
# Install pytorch=1.4.0, which is the lastest version that supports python 2
# no cuda
RUN pip install torch==1.4.0+cpu torchvision==0.5.0+cpu -f https://download.pytorch.org/whl/torch_stable.html

USER developer
WORKDIR $HOME