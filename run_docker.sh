#!/bin/sh
HOST_MOUNT=`pwd`

docker run \
    --rm \
    -it \
    --runtime=nvidia \
    -p 8888:8888 \
    --mount type=bind,src=${HOST_MOUNT},target=/docker_host \
    detectron bash
