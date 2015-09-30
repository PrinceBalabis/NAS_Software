Make server launch at boot:
chmod 755 launcher.sh
sudo crontab -e
	@reboot /bin/sleep 120 ; sh /root/NAS_Software/PushbulletToGetHTTP/launcher.sh >/root/logs/PushbulletToGetHTTP_log.txt 2>&1
sudo reboot
