#!/bin/bash

sudo add-apt-repository ppa:jonathonf/python-3.6 -y
sudo apt-get update
sudo apt-get install python3.6 -y
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.6 1
curl -O https://bootstrap.pypa.io/get-pip.py /tmp/get-pip.py
sudo python /tmp/get-pip.py
