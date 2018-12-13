#!/bin/bash
HOST_MOUNT=`pwd`

docker run \
    --rm \
    -it \
    --runtime=nvidia \
    -p 8888:8888 \
    --mount type=bind,src=${HOST_MOUNT},target=/docker_host \
    detectron run_detect_on_images /docker_host/data/images /docker_host/data/out
