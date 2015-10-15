#!/bin/sh

cd /root/NAS_Software/HomeAutomation/POSTServer
chmod a+x POSTServer.py
sudo python ./POSTServer.py &
cd /
