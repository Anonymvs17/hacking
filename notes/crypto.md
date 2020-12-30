
# Encryption

## Synchronous
Only with public key 

Examples: AES 

## Asyncronous
Private and publish key
Example: RSA

### Diffie and Hellman key exchance
F.i.: for https one needs to exchange key in a non-encrypted way but the issue is if someone catches they key.
Key exchange possible without dirct key exanchange 
F.e.: 2^x mod privKey => 2^43 mod 32 
Bob: 2^2 mod 4 = 5
Alica: 2^5 mod 4 = 3
Then key exchange with 5 & 3

Reversing it: 
Bob: 5^2 mod 4 = 7
Alica: 3^5 mod 4 = 7

Once this is done they can start communicating encripted

# Encoding
For f.i.: files, binaries, etc.

UTF8, BASE64, etc.

# Hashing
Password are usually being saved in hashes but also making sure for integrity (data did not change)
Example: md5, sha1, sha2, etc.

## Hashcat
Decript hashes

## cracking md5 (0 => md5) -a attackmode
hashcat -m 0 -a 0 "5f4dcc3b5aa765d61d8327deb882cf99"
#OR --force run with CPU instead of GPU; 0 => md5
hashcat -m 0 md5hash.txt /home/kali/Documents/rockyou.txt --force

Wordlists: hastcat wordlists, password seclist, but also in Linux: /usr/share/wordlists/ in the zip file

## Which hashtype?
TO check which hashtype: https://gchq.github.io/CyberChef/

hases might be in: /var/www/html/CuteNews/cdata/users

## (Integrity) check that data is not corrupted

dev@localhost ~]# md5sum metasploitable-linux-2.0.0.zip
8825f2509a9b9a58ec66bd65ef83167f  metasploitable-linux-2.0.0.zip
[dev@localhost ~]# sha1sum metasploitable-linux-2.0.0.zip
84133002ef79fc191e726d41265cf5ab0dfad2f0  metasploitable-linux-2.0.0.zip