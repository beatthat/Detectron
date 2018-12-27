#!/bin/sh
HOST_MOUNT=`pwd`

docker run \
    --name detectron \
    --rm \
    -it \
    --runtime=nvidia \
    -p 8888:8888 \
    -v ${HOST_MOUNT}:/docker_host \
    detectron bash 
