#!/usr/bin/env python

__author__ = 'Prince Stevie-Ray Charles Balabis <princebalabis@gmail.com>'
import logging

from pushbullet import Listener
from pushbullet import Pushbullet

pb = 0

#logging.basicConfig(level=logging.DEBUG)

API_KEY = 'X5UEjwDNYFw4mWqa0GHF2KSvcSC3m51u'
HTTP_PROXY_HOST = None
HTTP_PROXY_PORT = None


def on_push(data):
    print(data)
    global pb
    pushes = pb.get_pushes()
    print(pushes)
    #print('Received data:\n{}'.format(data))


def main():
    global pb
    pb = Pushbullet(API_KEY)

    s = Listener(account=pb,
                 on_push=on_push,
                 http_proxy_host=HTTP_PROXY_HOST,
                 http_proxy_port=HTTP_PROXY_PORT)
    try:
        s.run_forever()
    except KeyboardInterrupt:
        s.close()


if __name__ == '__main__':
    main()
