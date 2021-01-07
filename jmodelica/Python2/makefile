IMA_NAME = yangyangfu/jmodelica_py2
TAG = latest

build:
	docker build --no-cache --rm -t ${IMA_NAME}:${TAG} .

remove_image:
	docker rmi ${IMA_NAME}:${TAG}

push:
	docker push ${IMA_NAME}:${TAG}
