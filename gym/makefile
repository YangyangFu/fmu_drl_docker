UBUNTU_VER = 18.04
PYTHON_VER = 3
IMA_NAME = yangyangfu/gym_modelica_py${PYTHON_VER}
IMA_NAME_BASE = yangyangfu/gym_base_py${PYTHON_VER}

COMMAND_RUN = docker run \
	  --name c1 \
	  --detach=false \
	  -e DISPLAY=${DISPLAY} \
	  -v /tmp/.X11-unix:/tmp/.X11-unix \
	  --rm \
	  -v `pwd`:/mnt/shared \
	  -i \
          -t \
	  ${IMG_NAME} /bin/bash -c

build:
	docker build --build-arg UBUNTU_VER=${UBUNTU_VER} --no-cache --rm -t ${IMA_NAME} .

build_base:
	docker build -f Dockerfile_base --build-arg UBUNTU_VER=${UBUNTU_VER} --no-cache --rm -t ${IMA_NAME_BASE} .

remove_image:
	docker rmi ${IMA_NAME}

push:
	docker push ${IMA_NAME}:latest

Run:
	${COMMAND_RUN} \
		"cd /mnt/shared && bash"