  exec docker run \
 	  --name test \
          --user=root \
	  --detach=false \
	  -e DISPLAY=${DISPLAY} \
	  -v /tmp/.X11-unix:/tmp/.X11-unix\
	  --rm \
	  -v `pwd`:/mnt/shared \
	  -i \
          -t \
	  yangyangfu/jmodelica_py2:base /bin/bash -c "cd /mnt/shared && python /mnt/shared/simulate_example.py"
    exit $
