exec docker run \
      --user=root \
	  --detach=false \
	  -e DISPLAY=${DISPLAY} \
	  -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
	  --rm \
	  -v `pwd`:/mnt/shared \
	  -i \
      -t \
	  yangyangfu/modelicagym_py3_pytorch_gpu /bin/bash -c "cd /mnt/shared && python /mnt/shared/test_torch.py"
      
exit $
  
