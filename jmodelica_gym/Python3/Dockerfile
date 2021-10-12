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

# change user
USER developer

CMD [ "/bin/bash" ]