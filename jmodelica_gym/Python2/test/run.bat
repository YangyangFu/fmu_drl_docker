docker run^
	--user=root^
	--detach=false^
	-e DISPLAY=${DISPLAY}^
	-v /tmp/.X11-unix:/tmp/.X11-unix:rw^
	--rm^
	-v %CD%:/mnt/shared^
	-i^
	-t^
	yangyangfu/jmodelica_py2_gym /bin/bash -c "cd /mnt/shared && python /mnt/shared/test_cart_pole_q_learner.py"

