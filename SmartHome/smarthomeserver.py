#!/usr/bin/env python
"""
Most of this code comes from aweinstein, THANK YOU
https://github.com/aweinstein/scrapcode/blob/master/post_server/server.py


Very simple HTTP server in python. It toggles an LED either on or off
when it gets specific POST message

Usage::
    sudo python smarthomeserver.py [<port>]
    or sudo python smarthomeserver.py
"""
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
#import os ## Import library to run shell commands
#import RPi.GPIO as GPIO ## Import GPIO library

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

#    def do_GET(self):
#        self._set_headers()
#        self.wfile.write("<html><body><h1>Hi! You just ran homeautomation!</h1></body></html>")

#    def do_HEAD(self):
#        self._set_headers()

    def do_POST(self):
        self._set_headers()
	content_length = int(self.headers['Content-Length'])
	post_data = self.rfile.read(content_length)

	#Check if you are entering or exiting the iBeacon area
	action = "Didn't understand command!"
	returnmessage = "Didn't understand command!"
	if post_data[76] == 'x':
                returnmessage = "You just exited the iBeacon area!"
		#action = "03"
#		GPIO.output(7,False) ## Turn off GPIO pin 7
                log = open("log.txt", "wb")
                log.write("0");
                urllib2.urlopen("http://192.168.1.13:9500?c3").read() #Send command to HomeNetwork
	elif post_data[76] == 'n':
	        returnmessage = "You just entered the iBeacon area!"
                #action = "02"
#		GPIO.output(7,True) ## Turn on GPIO pin 7
                log = open("log.txt", "wb")
                log.write("1");
                urllib2.urlopen("http://192.168.1.13:9500?c4").read() #Send command to HomeNetwork

	#Print action feedback
	self.wfile.write("<html><body><h1>"+returnmessage+"</h1></body></html>")
	print returnmessage

	#Run shell command to send rf24 command
	#def main():
        #        os.system("../rf24/sendRF24Command "+action)
        #if __name__=="__main__":
        #        main()

def run(server_class=HTTPServer, handler_class=S, port=4050):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Started iBeacon Smart Home Server'

#    GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
#    GPIO.setup(7, GPIO.OUT) ## Setup GPIO Pin 7 to OUT
#    GPIO.setwarnings(False)

    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
