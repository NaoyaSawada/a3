FROM ubuntu:16.04
MAINTAINER Naoya Sawada <naoya@tuntunkun.com>
RUN apt update && apt install -y python-pip
RUN pip install git+https://github.com/NaoyaSawada/a3.git@v1.0
CMD a3d
EXPOSE 1103

