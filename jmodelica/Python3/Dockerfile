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
ARG CONDA_VERSION=py38_4.9.2
ARG CONDA_MD5=122c8c9beb51e124ab32a0fa6426c656

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

# create a conda base envrionment for pyfmi
# copy pyfmi python3 environment path to conda env
COPY conda /opt/conda/etc/conda

# create a conda environment install pyfmi for load fmu 
RUN conda update conda && \
    conda config --add channels conda-forge && \
    conda install pyfmi 
# There will be two pyfmi in this dockerfile. One is for python2 and the other is for python3.
# need scecify different pyfmi when call different pythons
# activate pyfmi for conda python 3
#ENV PYTHONPATH /opt/conda/lib/python3.8/site-packages:$PYTHONPATH

USER developer

CMD [ "/bin/bash" ]