# A Dockerfile that sets up a modelicagym environment - no jModleica is installed due to its imcompitability to python 3
ARG UBUNTU_VER 
FROM ubuntu:${UBUNTU_VER}
LABEL maintainer yangyangfu(yangyang.fu@tamu.edu)

# Install miniconda - this is from 
# https://github.com/ContinuumIO/docker-images/blob/master/miniconda3/debian/Dockerfile
# =================================
# hadolint ignore=DL3008
RUN apt-get update -q && \
    apt-get install -q -y --no-install-recommends \
        bzip2 \
        ca-certificates \
        git \
        libglib2.0-0 \
        libsm6 \
        libxext6 \
        libxrender1 \
        mercurial \
        subversion \
        wget \
        libgfortran3 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV PATH /opt/conda/bin:$PATH

# Leave these args here to better use the Docker build cache
ARG CONDA_VERSION=py37_4.9.2
ARG CONDA_MD5=3143b1116f2d466d9325c206b7de88f7

RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-${CONDA_VERSION}-Linux-x86_64.sh -O miniconda.sh && \
    echo "${CONDA_MD5}  miniconda.sh" > miniconda.md5 && \
    if ! md5sum --status -c miniconda.md5; then exit 1; fi && \
    mkdir -p /opt && \
    sh miniconda.sh -b -p /opt/conda && \
    rm miniconda.sh miniconda.md5 && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate base" >> ~/.bashrc && \
    find /opt/conda/ -follow -type f -name '*.a' -delete && \
    find /opt/conda/ -follow -type f -name '*.js.map' -delete && \
    /opt/conda/bin/conda clean -afy

# create a conda environment install pyfmi for load fmu and gym for opengym environment
# numpy has to be <=1.17 for a succesful run of fmu. 
# see https://github.com/DigitalSlideArchive/HistomicsTK/issues/880.
RUN conda update conda && \
    conda config --add channels conda-forge && \
    conda install numpy=1.17.5 \
        matplotlib \
        pip \
        gym \
        pyfmi 

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

# change user
USER developer

# Avoid warning that Matplotlib is building the font cache using fc-list. This may take a moment.
# This needs to be towards the end of the script as the command writes data to
# /home/developer/.cache
RUN python -c "import matplotlib.pyplot"

CMD [ "/bin/bash" ]
