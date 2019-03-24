FROM ubuntu:16.04
MAINTAINER Naoya Sawada <naoya@tuntunkun.com>
RUN apt update
RUN apt install -y python-pip git
RUN pip install --upgrade pip
RUN pip install git+https://github.com/NaoyaSawada/a3.git@v0.1
CMD a3d
EXPOSE 1103

