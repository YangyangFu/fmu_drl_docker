IMA_NAME = yangyangfu/jmodelica_py2_gym_pytorch_cpu
TAG = latest

build:
	docker build --no-cache --rm -t ${IMA_NAME}:${TAG} .

remove_image:
	docker rmi ${IMA_NAME}:${TAG}

push:
	docker push ${IMG_NAME}:${TAG}
