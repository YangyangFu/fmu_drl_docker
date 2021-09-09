IMA_NAME = yangyangfu/jmodelica_gym_py3
TAG = latest

# This is not very important
CONDA_VERSION=py38_4.9.2
CONDA_MD5=122c8c9beb51e124ab32a0fa6426c656

#build:
#	docker build --build-arg CONDA_VERSION=${CONDA_VERSION},CONDA_MD5=${CONDA_MD5} --no-cache --rm -t ${IMA_NAME} .
build:
	docker build --no-cache --rm -t ${IMA_NAME} .

remove_image:
	docker rmi ${IMA_NAME}

push:
	docker push ${IMA_NAME}:latest
