FROM yangyangfu/jmodelica_py2
LABEL maintainer yangyangfu(yangyang.fu@tamu.edu)

# A Dockerfile that sets up a full Gym install with test dependencies
USER root
RUN apt-get -y update && apt-get install -y \
    unzip \
    libglu1-mesa-dev \
    libgl1-mesa-dev \
    libosmesa6-dev \
    xvfb \
    patchelf \
    ffmpeg \
    curl
    
RUN \ 
# Download mujoco
    mkdir /root/.mujoco && \
    cd /root/.mujoco  && \
    curl -O https://www.roboti.us/download/mjpro150_linux.zip  && \
    unzip mjpro150_linux.zip

ARG MUJOCO_KEY
ARG PYTHON_VER
ENV MUJOCO_KEY=$MUJOCO_KEY

ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/root/.mujoco/mjpro150/bin
RUN echo $MUJOCO_KEY | base64 --decode > /root/.mujoco/mjkey.txt
RUN pip install pytest pytest-forked lz4

COPY . /usr/local/gym/
WORKDIR /usr/local/gym/
#RUN [ "$PYTHON_VER" != "2.7" ] && pip install .[all] || pip install .
# easy install: this is the version that can render on MacOS through docker python 2
RUN pip install -Iv gym==0.15.3

USER developer

# entry point for gym
ENTRYPOINT ["/usr/local/gym/bin/docker_entrypoint"]
