This webserver is used to connect HomeNetwork to the internet


Have GeoHooper installed on iPhone:
Webservice:
	URL: http://princehome.duckdns.org:4050/
	POST
Region:
	Name: Apartment
	UUID: 74278BDA-B644-4520-8F0C-720EAF059935


Make server launch at boot:
chmod 755 launcher.sh
cd
mkdir logs
sudo crontab -e
	@reboot /bin/sleep 120 ; sh /root/NAS_Software/HomeNetworkWebserver/launcher.sh >/root/logs/cronlog 2>&1
sudo reboot
