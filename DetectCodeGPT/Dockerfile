FROM nvidia/cuda:12.1.1-devel-ubuntu22.04 as base
RUN apt-get update && apt-get install -y sudo 
RUN apt-get update && apt-get install -y git

ARG USERNAME=kato
ARG GROUPNAME=docker
ARG UID=1000
ARG GID=1000
ARG PASSWORD=kato-docker-pw
RUN groupadd -g $GID $GROUPNAME && \
    useradd -m -s /bin/bash -u $UID -g $GID -G sudo $USERNAME && \
    echo $USERNAME:$PASSWORD | chpasswd && \
    echo "$USERNAME   ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
USER $USERNAME
WORKDIR /work
COPY requirements.txt ./


RUN sudo apt-get update && \
    sudo apt-get install -y python3 python3-pip
RUN pip3 install -r requirements.txt
