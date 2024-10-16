# syntax=docker/dockerfile:1

# base image: plain vanilla ubuntu + build tools
FROM ubuntu:24.04

# set up environment
RUN apt-get update && apt-get install -y python3.12
RUN apt-get update && apt-get install -y python3-dev
RUN apt-get update && apt-get install -y python3-pip
RUN apt-get update && apt-get install -y python3-setuptools
RUN apt-get update && apt-get install -y git

# set up non-root user
RUN usermod --login vscode --move-home --home /home/vscode ubuntu && \
    groupmod --new-name vscode ubuntu
USER vscode

WORKDIR /home/vscode

# add python user bin to path
ENV PATH="$PATH:/home/vscode/.local/bin"

# install not-quite-explicit dependencies
RUN python3 -m pip install --user matplotlib --break-system-packages

# install sgeop from source
RUN pip3 install --user git+https://github.com/uscuni/sgeop.git#egg=sgeop --break-system-packages