#!/bin/sh

cd
mkdir logs
cd /root/NAS_Software/PushbulletToGetHTTP
sudo python ./PushBulletToGetRequest_Server.py &
cd /
