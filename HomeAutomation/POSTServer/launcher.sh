#!/bin/sh

cd
mkdir logs
cd /root/NAS_Software/HomeAutomation/POSTServer
sudo python ./POSTServer.py &
cd /
