exec docker run \
 	  --name gym_test \
      --user=root \
	  --detach=false \
	  -e DISPLAY=${DISPLAY} \
	  -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
	  --rm \
	  -v `pwd`:/mnt/shared \
	  -i \
      -t \
	  yangyangfu/gym_torch_py3 /bin/bash -c "cd /mnt/shared && python /mnt/shared/test_gym_torch.py"

exit $
  
