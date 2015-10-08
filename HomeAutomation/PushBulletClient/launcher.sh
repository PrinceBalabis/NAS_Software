#!/bin/sh

cd
mkdir logs
cd /root/NAS_Software/HomeAutomation/PushBulletClient/
sudo python ./PushBulletClient.py &
cd /
