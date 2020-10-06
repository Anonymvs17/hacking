# Hashcat

## cracking md5 (0 => md5) -a attackmode
hashcat -m 0 -a 0 "5f4dcc3b5aa765d61d8327deb882cf99"
#OR --force run with CPU instead of GPU; 0 => md5
hashcat -m 0 md5hash.txt /home/kali/Documents/rockyou.txt --force

Wordlists: hastcat wordlists, password seclist, but also in Linux: /usr/share/wordlists/ in the zip file

# Which hashtype?
TO check which hashtype: https://gchq.github.io/CyberChef/

hases might be in: /var/www/html/CuteNews/cdata/users