IMA_NAME = yangyangfu/modelicagym_py3_pytorch_gpu
TAG = latest
VERSION = cuda-10.1

build:
	docker build --no-cache --rm -t ${IMA_NAME}:${TAG} .

remove_image:
	docker rmi ${IMA_NAME}:${TAG}

tag:
	docker image tag ${IMA_NAME} ${IMA_NAME}:${VERSION}

push:
	docker image push ${IMA_NAME}:${VERSION}
