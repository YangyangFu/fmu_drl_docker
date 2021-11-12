# A jmodelica docker image hosted by michael wetter: https://github.com/lbl-srg/docker-ubuntu-jmodelica/blob/master/Dockerfile
FROM michaelwetter/ubuntu-1804_jmodelica_trunk
# Run a command to find JModelica installation location 
#find / -xdev 2>/dev/null -name "JModelica"

# Add to path
ENV ROOT_DIR /usr/local
ENV JMODELICA_HOME $ROOT_DIR/JModelica
ENV IPOPT_HOME $ROOT_DIR/Ipopt-3.12.4
ENV SUNDIALS_HOME $JMODELICA_HOME/ThirdParty/Sundials
ENV SEPARATE_PROCESS_JVM /usr/lib/jvm/java-8-openjdk-amd64/
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/
ENV PYTHONPATH $PYTHONPATH:$JMODELICA_HOME/Python:$JMODELICA_HOME/Python/pymodelica
