FROM yangyangfu/jmodelica_py3
LABEL Yangyang Fu (yangyang.fu@tamu.edu)

# Install libgfortran for high-version pyfmi
#RUN apt-get update -q && \
#    apt-get install -q -y --no-install-recommends \
#    libgfortran4 \
#    && apt-get clean \
#    && rm -rf /var/lib/apt/lists/*

USER root
# may have conda install pip/git if one wants to install github repo directly to conda env
RUN conda install git pip

#### ==================================================================
#### install and test modelicagym
# install modelicagym from source
WORKDIR $HOME
RUN pip install git+git://github.com/YangyangFu/modelicagym.git@master 

# install a modelica-opengym example: pole cart tutorial 
RUN mkdir github && cd github 
COPY ./gym-tutorial/gym_cart_jmodelica $HOME/github/Tutorials/gym_cart_jmodelica
COPY ./gym-tutorial/setup.py $HOME/github/Tutorials/setup.py
RUN ls ./github/Tutorials -l
RUN cd $HOME/github/Tutorials && pip install -e .
WORKDIR $HOME

#### ========================================================
#### install gpu-supported pytorch
## add cuda
RUN apt-get update && apt-get install -y --no-install-recommends \
    gnupg2 curl ca-certificates && \
    curl -fsSL https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub | apt-key add - && \
    echo "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64 /" > /etc/apt/sources.list.d/cuda.list && \
    echo "deb https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64 /" > /etc/apt/sources.list.d/nvidia-ml.list && \
    apt-get purge --autoremove -y curl \
    && rm -rf /var/lib/apt/lists/*

ENV CUDA_VERSION 10.1.243
ENV CUDA_PKG_VERSION 10-1=$CUDA_VERSION-1

# For libraries in the cuda-compat-* package: https://docs.nvidia.com/cuda/eula/index.html#attachment-a
RUN apt-get update && apt-get install -y --no-install-recommends \
    cuda-cudart-$CUDA_PKG_VERSION \
    cuda-compat-10-1 \
    && ln -s cuda-10.1 /usr/local/cuda && \
    rm -rf /var/lib/apt/lists/*

# Required for nvidia-docker v1
RUN echo "/usr/local/nvidia/lib" >> /etc/ld.so.conf.d/nvidia.conf && \
    echo "/usr/local/nvidia/lib64" >> /etc/ld.so.conf.d/nvidia.conf

ENV PATH /usr/local/nvidia/bin:/usr/local/cuda/bin:${PATH}
ENV LD_LIBRARY_PATH /usr/local/nvidia/lib:/usr/local/nvidia/lib64

# nvidia-container-runtime
ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES compute,utility
ENV NVIDIA_REQUIRE_CUDA "cuda>=10.1 brand=tesla,driver>=396,driver<397 brand=tesla,driver>=410,driver<411 brand=tesla,driver>=418,driver<419"

# CUDNN
ENV CUDNN_VERSION 8.0.4.30

RUN apt-get update && apt-get install -y --no-install-recommends \
    libcudnn8=$CUDNN_VERSION-1+cuda10.1 \
    libcudnn8-dev=$CUDNN_VERSION-1+cuda10.1 \
    && apt-mark hold libcudnn8 && \
    rm -rf /var/lib/apt/lists/*

# install pyhton opengl - not necessary if no render
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python-opengl && \
    rm -rf /var/lib/apt/lists/*

# Install pytorch
RUN conda install pytorch torchvision torchaudio cudatoolkit=10.1 -c pytorch

# change user
USER developer

CMD [ "/bin/bash" ]