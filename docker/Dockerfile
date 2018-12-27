# Use Caffe2 image as parent image
FROM caffe2/caffe2:snapshot-py2-cuda9.0-cudnn7-ubuntu16.04

RUN apt-get update && apt-get install \
    -y --no-install-recommends --allow-downgrades --allow-change-held-packages \
    vim \
    wget \
    unzip && \
    rm -rf /var/lib/apt/lists/*


RUN mv /usr/local/caffe2 /usr/local/caffe2_build
ENV Caffe2_DIR /usr/local/caffe2_build

ENV PYTHONPATH /usr/local/caffe2_build:${PYTHONPATH}
ENV LD_LIBRARY_PATH /usr/local/caffe2_build/lib:${LD_LIBRARY_PATH}

# Clone the Detectron repository
RUN git clone https://github.com/beatthat/Detectron /detectron
RUN cd /detectron && git checkout docker-working

# Install Python dependencies
RUN pip install -r /detectron/requirements.txt

# Install the COCO API
RUN git clone https://github.com/cocodataset/cocoapi.git /cocoapi
WORKDIR /cocoapi/PythonAPI
RUN make install

WORKDIR /cocoapi

RUN wget http://images.cocodataset.org/annotations/annotations_trainval2014.zip && \
    unzip annotations_trainval2014.zip && \
    wget http://images.cocodataset.org/annotations/annotations_trainval2017.zip && \
    unzip annotations_trainval2017.zip

# Go to Detectron root
WORKDIR /detectron

# Set up Python modules
RUN make

# [Optional] Build custom ops
RUN make ops

COPY bin bin

# /detectron/bin has scripts intended to execute with docker,
# e.g. docker run ... bin/run_detect_on_images.
#
# /docker_host/bin is the same as /detectron/bin
# but /docker_host is expected to be a mounted directory
# from the host machine that's running docker. 
# This makes is easier to test changes without publishing to git.
ENV PATH /docker_host/docker/bin:${PATH}:/detectron/bin
ENV PYTHONPATH ${PYTHONPATH}:/detecton:/docker_host

RUN python ./bin/cache_weights.py

CMD [ "bin/bash" ]