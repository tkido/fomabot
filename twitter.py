#!/usr/bin/env python
# -*- coding: utf-8 -*-

from config import USER_ID, CK, CS, AT, AS
from requests_oauthlib import OAuth1Session

twitter = OAuth1Session(CK, CS, AT, AS)

def send(url, params):
	req = twitter.post(url, params = params)

	if req.status_code == 200:
	    print ("OK")
	else:
	    print ("Error: %d" % req.status_code)

	return req.status_code


def tweet(msg):
	url = "https://api.twitter.com/1.1/statuses/update.json"
	params = {"status": msg}
	send(url, params)

def selfdm(msg):
	url = "https://api.twitter.com/1.1/direct_messages/new.json"
	params = {"text": msg, "user_id": USER_ID}
	send(url, params)
