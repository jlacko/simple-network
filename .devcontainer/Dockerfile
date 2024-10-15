# syntax=docker/dockerfile:1

# base image: plain vanilla ubuntu + build tools
FROM ubuntu:22.04

# set up environment
RUN apt-get update && apt-get install -y python3.9
RUN apt-get update && apt-get install -y python3-dev
RUN apt-get update && apt-get install -y python3-pip
RUN apt-get update && apt-get install -y git

# set up non-root user
RUN groupadd --gid 1000 vscode
RUN useradd --uid 1000 --gid 1000 --create-home vscode
USER vscode

# install sgeop from source
RUN pip install git+https://github.com/uscuni/sgeop.git