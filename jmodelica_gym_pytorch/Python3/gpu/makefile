IMA_NAME = yangyangfu/jmodelica_py3_gym_pytorch
TAG = gpu

build:
	docker build --no-cache --rm -t ${IMA_NAME}:${TAG} .

remove_image:
	docker rmi ${IMA_NAME}:${TAG}

tag:
	docker image tag ${IMA_NAME} ${IMA_NAME}:${TAG}

push:
	docker image push ${IMA_NAME}:${TAG}
