docker run^
	--name gym_test^
	--user=root^
	--detach=false^
	-e DISPLAY=${DISPLAY}^
	-v /tmp/.X11-unix:/tmp/.X11-unix:rw^
	--rm^
	-v %CD%:/mnt/shared^
	-i^
	-t^
	yangyangfu/pytorch_py3 /bin/bash -c "cd /mnt/shared && python /mnt/shared/test_torch.py"
