docker run^
	--user=root^
	--detach=false^
	-e DISPLAY=${DISPLAY}^
	-v /tmp/.X11-unix:/tmp/.X11-unix:rw^
	--rm^
	-v %CD%:/mnt/shared^
	-i^
	-t^
	yangyangfu/modelicagym_py3_pytorch_cpu /bin/bash -c "cd /mnt/shared && python /mnt/shared/test_torch.py"