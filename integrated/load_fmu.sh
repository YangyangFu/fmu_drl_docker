exec docker run \
      --user=root \
	  --detach=false \
	  -e DISPLAY=${DISPLAY} \
	  -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
	  --rm \
	  -v `pwd`:/mnt/shared \
	  -i \
      -t \
	  yangyangfu/jmodelica_py3 /bin/bash -c "source activate base && cd /mnt/shared && python /mnt/shared/load_fmu.py"

exit $