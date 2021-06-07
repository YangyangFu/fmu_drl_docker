IMA_NAME_DUBUG = yangyangfu/jmodelica_py3_debug
IMA_NAME = yangyangfu/jmodelica_py3
TAG = latest

build_debug:
	docker build -f Dockerfile_debug --no-cache --rm -t ${IMA_NAME}:${TAG} .

build:
	docker build -f Dockerfile --no-cache --rm -t ${IMA_NAME}:${TAG} .

remove_image:
	docker rmi ${IMA_NAME}:${TAG}

push:
	docker push ${IMA_NAME}:${TAG}
