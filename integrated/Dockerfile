## A jmodelica docker image in python 2: call this using "python2 script.py".
FROM yangyangfu/jmodelica_py2

USER root
## add a conda for python 3 environment
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
    #echo "conda activate base" >> ~/.bashrc && \
    find /opt/conda/ -follow -type f -name '*.a' -delete && \
    find /opt/conda/ -follow -type f -name '*.js.map' -delete && \
    /opt/conda/bin/conda clean -afy

# create a conda environment install pyfmi for load fmu and gym for opengym environment
# numpy has to be <=1.17 for a succesful run of fmu. 
# see https://github.com/DigitalSlideArchive/HistomicsTK/issues/880.
RUN conda update conda && \
    conda config --add channels conda-forge && \
    conda install gym

CMD [ "/bin/bash" ]