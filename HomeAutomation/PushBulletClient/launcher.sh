#!/bin/sh

cd /root/NAS_Software/HomeAutomation/PushBulletClient/
chmod a+x PushBulletClient.py
sudo python ./PushBulletClient.py &
cd /
