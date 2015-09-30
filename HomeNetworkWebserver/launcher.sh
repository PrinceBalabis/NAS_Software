#!/bin/sh

cd
mkdir logs
cd /root/NAS_Software/HomeNetworkWebserver
sudo python ./HomeNetworkWebserver.py &
cd /
