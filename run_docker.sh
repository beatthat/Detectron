#!/bin/sh
HOST_MOUNT=`pwd`

docker run \
    --rm \
    -it \
    --runtime=nvidia \
    -p 8888:8888 \
    -v ${HOST_MOUNT}:/docker_host \
    detectron run_jupyter.sh /docker_host 
