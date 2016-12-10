FROM ubuntu:14.04

# Install python
RUN \
  apt-get update && \
  apt-get install -y python python-dev python-pip python-virtualenv software-properties-common libffi-dev

RUN add-apt-repository -y ppa:openaddresses/ci
RUN apt-get update -y

# Install machine prerequirements
RUN apt-get install -y python-cairo python-pip python-dev libpq-dev \
  python-gdal=1.11.2+dfsg-1~exp2~trusty

# Set up and configure machine
ADD . /machine
WORKDIR /machine

RUN CPLUS_INCLUDE_PATH=/usr/include/gdal C_INCLUDE_PATH=/usr/include/gdal pip install "GDAL==1.11.2"
RUN pip install cairocffi
RUN pip install -U .

# Default entrypoint
ENTRYPOINT ["openaddr-process-one"]