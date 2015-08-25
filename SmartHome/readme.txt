sudo crontab -e

@reboot python /root/NAS_Software/SmartHome/smarthomeserver.py &


OLD WAY:
Make server launch at boot:
chmod 755 launcher.sh
cd
mkdir logs
sudo crontab -e
	@reboot /bin/sleep 120 ; sh /root/RaspberryPi/smarthome/launcher.sh >/root/logs/cronlog 2>&1
sudo reboot
