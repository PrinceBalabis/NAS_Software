Make server launch at boot:
chmod 755 launcher.sh
sudo crontab -e
	@reboot /bin/sleep 100 ; sh /root/NAS_Software/HomeAutomation/PushBulletClient/launcher.sh >/root/logs/PushBulletClient.log 2>&1
sudo reboot
