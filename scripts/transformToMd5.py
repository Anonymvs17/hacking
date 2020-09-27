#!/usr/bin/env python3
import re
import requests
import sys
import argparse
import hashlib

#initialisation of variables
url = 'http://docker.hackthebox.eu:32620/'
regex = '<h3 align=\'center\'>(.+?)<'
def encryptRequest(response):
	#<h3 align='center'>mmCkmvWb9pk1CNGvsxDQ</h3>
	valueToEncrypt = re.search(regex, response.text).group(1)
	if valueToEncrypt is not None:
		print('[*] value:  "{p}"'.format(p = valueToEncrypt))

	result = hashlib.md5(valueToEncrypt.encode()) 
	print('[*] encrypted value:  "{p}"'.format(p = result.hexdigest()))

	headers = {
		'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
		'Referer': url
	}

	data = {
		'hash':result.hexdigest()
	}

	post_res = session.post(url, headers = headers, data = data, allow_redirects = True)
	return post_res
    

# iterating over passwords
session = requests.Session()
response = session.get(url)
#<h3 align='center'>mmCkmvWb9pk1CNGvsxDQ</h3>

i = 1
while i < 15:
  response = encryptRequest(response)
  if response is not None:
	print('[{r}] response "{p}"'.format(p = response.text, r = i))
  i += 1
