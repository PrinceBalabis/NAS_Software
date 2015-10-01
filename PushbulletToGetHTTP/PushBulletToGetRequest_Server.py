__author__ = 'Prince Stevie-Ray Charles Balabis <princebalabis@gmail.com>'
import logging
import json
import urllib2

from pushbullet import Listener
from pushbullet import Pushbullet

pb = 0

#logging.basicConfig(level=logging.DEBUG)

API_KEY = 'X5UEjwDNYFw4mWqa0GHF2KSvcSC3m51u'
HTTP_PROXY_HOST = None
HTTP_PROXY_PORT = None

def on_push(data):
    global pb
    pushes = pb.get_pushes(None, 1) #Get latest push, just one
    parsed_data = json.dumps(pushes[1]) # Convert to String
    json_object = json.loads(parsed_data) # Convert to JSON Object
    title_message = json_object[0]['title'] # Parse JSON Object
    body_message = json_object[0]['body'] # Parse JSON Object
    #print(title_message) #print title
    if title_message in 'PrinceHome': # Check if the push is a PrinceHome type
        from time import gmtime, strftime
        print strftime('%Y-%m-%d %H:%M:%S', gmtime()),
        print('Got PrinceHome command: ' + body_message)
        try:
            urllib2.urlopen("http://192.168.1.13:9500?c"+body_message).read() #Send command to HomeNetwork
        except:
            pass

def main():
    print 'Started PushBullet listener, relaying to Home Network'
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
