#!/usr/bin/env python

#  Run: "python -m pip install requests_oauthlib" first to install requests_oauthlib python module

import httplib
import json
import requests
from requests_oauthlib import OAuth1
import time
import urllib2

# Get the following values from the OAuth tool in your Twitter app dashboard.
access_token = '3375696081-BDamafVyBmwXmNu60VCVeVk89VK0DQUFDwGQ60e'
access_token_secret = 'L5lTG3i5eWadSkc6yLyF6hFHTWNu7E9wk9CqOmGhjeloI'
consumer_key = 'VLTP79KiKvyfzbnBX8AmObI88'
consumer_secret = 'nyEYix5Ri1RSHPMjvsZL85w6eGAKsC0Pk3pihqmgcDuFasOJrJ'

auth = OAuth1(consumer_key, consumer_secret, access_token, access_token_secret)
r = requests.get('https://userstream.twitter.com/1.1/user.json',
    params={'replies': 'all', 'delimited': 'length'}, stream=True, auth=auth)

last_request = time.time()
for line in r.iter_lines(chunk_size=64):
    # it doesn't print out until chunk_size bytes are received. Argh.
    # https://github.com/kennethreitz/requests/issues/844
    # and if I set chunk_size any lower, for some reason it exits immediately.

    # The fact that I use "delimited=length" means that at least the length
    # of the upcoming tweet will happen every time a tweet comes in. So...
    # just read the twitter feed every time a new tweet comes in. Meh!
    if time.time() - last_request > 1: # max 1 request/sec
        real_response = requests.get('https://api.twitter.com/1.1/statuses/mentions_timeline.json', params={'screen_name': 'PrinceHomeIoT', 'count': '1'}, auth=auth)
        text = real_response.json()[0]['text']
        #if (text.startswith('@PrinceHomeIoT ')):
        text = text.replace('@PrinceHomeIoT ', '')
        urllib2.urlopen("http://princehome.duckdns.org:9500?c"+text).read()
        last_request = time.time()
