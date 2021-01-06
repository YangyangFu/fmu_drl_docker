IMA_NAME = yangyangfu/jmodelica_py2_gym_pytorch_gpu
TAG = latest
VERSION = torch-1.4-cuda-10.1

build:
	docker build --no-cache --rm -t ${IMA_NAME}:${TAG} .

remove_image:
	docker rmi ${IMA_NAME}:${TAG}

tag:
	docker image tag ${IMA_NAME} ${IMA_NAME}:${VERSION}

push:
	docker push ${IMA_NAME}:${VERSION}
