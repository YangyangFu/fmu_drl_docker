exec docker run \
      --user=root \
	  --detach=false \
	  -e DISPLAY=${DISPLAY} \
	  -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
	  --rm \
	  -v `pwd`:/mnt/shared \
	  -i \
      -t \
	  conda_test /bin/bash -c "source activate py37 && cd /mnt/shared && python /mnt/shared/load_fmu.py"

exit $