#!/usr/bin/python

import sys
import urllib2
import re

def getAddress():
	url = raw_input("Site to scrape: ")
	http = "http://"
	https = "https://"

	if http in url:
		return url
	elif https in url:
		return url
	else:
		url = "http://" + url
		return url

def parseAddress():
	try:
		website = urllib2.urlopen(getAddress())
		html = website.read()

		addys = re.findall('''[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?''', html, flags=re.IGNORECASE)

		print addys

	except urllib2.HTTPError, err:
		print "Cannot retrieve URL: HTTP Error Code: ", err.code
	except urllib2.URLError, err:
		print "Cannot retrive URL: " + err.reason[1]

def execute():
	parseAddress()

### MAIN

def main():
	execute()

main()
