# A Dockerfile that sets up a full Gym install with test dependencies
ARG PYTHON_VER=3.7
FROM python:$PYTHON_VER
RUN apt-get -y update && apt-get install -y unzip libglu1-mesa-dev libgl1-mesa-dev libosmesa6-dev xvfb patchelf ffmpeg
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

#COPY . /usr/local/gym/
WORKDIR /usr/local/
#RUN [ "$PYTHON_VER" != "3.7" ] && pip install .[all] || pip install .
# install gym
RUN cd /usr/local \
    && git clone https://github.com/openai/gym.git \
    && cd /usr/local/gym \
    && pip install -e '.[all]' \
    && rm -rf ~/.cache/pip

## Install pytorch
# no cuda
RUN pip install torch==1.4.0+cpu torchvision==0.5.0+cpu -f https://download.pytorch.org/whl/torch_stable.html

ENTRYPOINT ["/usr/local/gym/bin/docker_entrypoint"]
CMD ["pytest","--forked"]
