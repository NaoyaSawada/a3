FROM ubuntu:16.04
MAINTAINER Naoya Sawada <naoya@tuntunkun.com>
RUN apt update && apt install -y \
	python-pip
CMD echo "now running...."

