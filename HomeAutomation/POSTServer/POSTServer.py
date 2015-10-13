#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Most of this code comes from aweinstein, THANK YOU
https://github.com/aweinstein/scrapcode/blob/master/post_server/server.py


Very simple HTTP server in python. It toggles an LED either on or off
when it gets specific POST message

Usage::
    'sudo python smarthomeserver.py [<port>]'
    or 'sudo python smarthomeserver.py' for default server port of 4050

Use 'http://pythoniter.appspot.com/' to beautify/indent python code
"""

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import urllib2


class S(BaseHTTPRequestHandler):

#    def _set_headers(self):
#        self.send_response(200)
#        self.send_header('Content-type', 'text/html')
#        self.end_headers()

#    def do_GET(self):
#        self._set_headers()
#        self.wfile.write("<html><body><h1>Hi! You just ran homeautomation!</h1></body></html>")

#    def do_HEAD(self):
#        self._set_headers()

    def do_POST(self):

#        self._set_headers()

        from time import gmtime, strftime

        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        # Check if you are entering or exiting the iBeacon area

        if 'LocationExit' in post_data:  # LocationExit is received on POST request
            print strftime('%Y-%m-%d %H:%M:%S', gmtime()),
            print 'You just exited the iBeacon area!'
            log = open('log.txt', 'wb')
            log.write('0')
            try:
                urllib2.urlopen('http://192.168.1.13:9500/3')  # Send command to HomeNetwork
            except:
                pass
        elif 'LocationEnter' in post_data:

                                          # LocationEnter is received on POST request

            print strftime('%Y-%m-%d %H:%M:%S', gmtime()),
            print 'You just entered the iBeacon area!'
            log = open('log.txt', 'wb')
            log.write('1')
            try:
                urllib2.urlopen('http://192.168.1.13:9500/4')  # Send command to HomeNetwork
            except:
                pass
        else:

              # What happens if command is not understood

            print post_data
            print "Didn't understand command!"


        # Print action feedback
        # self.wfile.write('<html><body><h1>' + returnmessage
        #                 + '</h1></body></html>')

def run(server_class=HTTPServer, handler_class=S, port=4050):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Started iBeacon Smart Home Server'

    httpd.serve_forever()


if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
