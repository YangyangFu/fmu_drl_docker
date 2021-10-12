FROM yangyangfu/jmodelica_py3_gym
LABEL maintainer yangyangfu(yangyang.fu@tamu.edu)

#
USER root
# update
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python-opengl 
    
# install pytorch cpu only
RUN conda install pytorch torchvision cpuonly -c pytorch && \
    conda clean -ya

USER developer
WORKDIR $HOME