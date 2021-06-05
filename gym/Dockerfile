# A Dockerfile that sets up a full Gym install with test dependencies
ARG PYTHON_VER
FROM continuumio/miniconda$PYTHON_VER:latest
LABEL maintainer yangyangfu(yangyang.fu@tamu.edu)

##################################################
# Avoid warnings
# debconf: unable to initialize frontend: Dialog
# debconf: (TERM is not set, so the dialog frontend is not usable.)
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

# Install required packages
RUN apt-get update && \
    apt-get install -y \
    ant=1.10.5-3~18.04 \
    autoconf=2.69-11 \
    cmake=3.10.2-1ubuntu2.18.04.1 \
    cython=0.26.1-0.4 \
    g++=4:7.4.* \
    gfortran=4:7.4.0-1ubuntu2.3 \
    libgfortran3 \
    ipython=5.5.0-1 \
    libboost-dev=1.65.1.0ubuntu1 \
    openjdk-8-jdk=8u222-b10-1ubuntu1~18.04.1 \
    pkg-config=0.29.1-0ubuntu2 \
    python-matplotlib \
    subversion=1.9.7-4ubuntu1 \
    swig=3.0.12-1 \
    wget=1.19.4-1ubuntu2.2 \
    zlib1g-dev=1:1.2.11.dfsg-0ubuntu2 \
    git && \
    rm -rf /var/lib/apt/lists/*

# minimal installation of opengym
# easy install: this is the version that can render on MacOS through docker python 2
#RUN pip install -Iv gym==0.15.3
RUN pip install gym

# copy bin to docker for entrypoint
COPY ./bin /usr/local/gym/bin

# define users
# Replace 1000 with your user / group id
RUN export uid=1000 gid=1000 && \
    mkdir -p /home/developer && \
    mkdir -p /etc/sudoers.d && \
    echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >> /etc/passwd && \
    echo "developer:x:${uid}:" >> /etc/group && \
    echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \
    chmod 0440 /etc/sudoers.d/developer && \
    chown ${uid}:${gid} -R /home/developer

ENV HOME /home/developer

# install modelicagym from source
WORKDIR $HOME
RUN mkdir github && cd github && git clone https://github.com/YangyangFu/modelicagym.git && \
    cd modelicagym && python -m pip install -e .

WORKDIR $HOME
# install a modelica-opengym example: pole cart tutorial 
COPY ./gym-tutorial/gym_cart_jmodelica $HOME/github/Tutorials/gym_cart_jmodelica
COPY ./gym-tutorial/setup.py $HOME/github/Tutorials/setup.py
RUN ls ./github/Tutorials -l
RUN cd $HOME/github/Tutorials && pip install -e .
WORKDIR $HOME

# install pyfmi for load fmu
RUN conda config --add channels conda-forge && \
    conda install pyfmi

# change user
USER developer

# Avoid warning that Matplotlib is building the font cache using fc-list. This may take a moment.
# This needs to be towards the end of the script as the command writes data to
# /home/developer/.cache
RUN python -c "import matplotlib.pyplot"

# entry point for gym
ENTRYPOINT ["/usr/local/gym/bin/docker_entrypoint"]
