HOST = yangyangfu

# define image names
IMAGE_NAME_CPU = jmodelica_drl_cpu
IMAGE_NAME_GPU = jmodelica_drl_gpu

# some dockerfile
DOCKERFILE_CPU = Dockerfile_CPU
DOCKERFILE_GPU = Dockerfile_GPU

#build:
#	docker build --build-arg CONDA_VERSION=${CONDA_VERSION},CONDA_MD5=${CONDA_MD5} --no-cache --rm -t ${IMA_NAME} .
build_cpu:
	docker build -f ${DOCKERFILE_CPU} --no-cache --rm -t ${IMAGE_NAME_CPU} .

build_gpu:
	docker build -f ${DOCKERFILE_GPU} --no-cache --rm -t ${IMAGE_NAME_GPU} .

tag_cpu:
	docker tag ${IMAGE_NAME_CPU} ${HOST}/${IMAGE_NAME_CPU}:latest

tag_gpu:
	docker tag ${IMAGE_NAME_GPU} ${HOST}/${IMAGE_NAME_GPU}:latest

push_cpu:
	docker push ${HOST}/${IMAGE_NAME_CPU}:latest

push_gpu:
	docker push ${HOST}/${IMAGE_NAME_GPU}:latest
