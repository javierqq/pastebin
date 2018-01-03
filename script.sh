#!/bin/bash

sudo add-apt-repository ppa:jonathonf/python-3.6 -y
sudo apt-get update
sudo apt-get install python3.6 -y
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.6 1
curl -s -o /tmp/get-pip.py https://bootstrap.pypa.io/get-pip.py
sudo python /tmp/get-pip.py
sudo pip install virtualenv
mkdir project
cd project
virtualenv venv
. venv/bin/activate
pip install Flask
