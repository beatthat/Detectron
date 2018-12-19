#!/bin/bash
HOST_MOUNT=`pwd`

docker run \
    --rm \
    -it \
    --runtime=nvidia \
    -p 8888:8888 \
    -v ${HOST_MOUNT}:/docker_host \
    detectron run_detect_on_images /docker_host/data/video/video_0.avi /docker_host/data/out /docker_host
