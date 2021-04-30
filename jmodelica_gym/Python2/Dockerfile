FROM yangyangfu/jmodelica_py2_gym_base
USER root
# install git
RUN apt-get -y update && apt-get install -y git

# install modelicagym from source
WORKDIR $HOME
RUN echo $HOME
RUN mkdir github && cd github && git clone https://github.com/YangyangFu/modelicagym.git && \
    cd modelicagym && python -m pip install -e .

WORKDIR $HOME

# install a modelica-opengym example: pole cart tutorial 
COPY ./gym-tutorial/gym_cart_jmodelica $HOME/github/Tutorials/gym_cart_jmodelica
COPY ./gym-tutorial/setup.py $HOME/github/Tutorials/setup.py
RUN ls ./github/Tutorials -l
RUN cd $HOME/github/Tutorials && pip install -e .

WORKDIR $HOME
USER developer


