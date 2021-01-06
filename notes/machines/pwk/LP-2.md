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
Ubuntu

## Info about ports
* SSH:  SSH-2.0-OpenSSH_5.8p1 Debian-7ubuntu1 ( service.version=5.8p1 openssh.comment=Debian-7ubuntu1 service.vendor=OpenBSD service.family=OpenSSH service.product=OpenSSH service.cpe23=cpe:/a:openbsd:openssh:5.8p1 os.vendor=Ubuntu os.family=Linux os.product=Linux os.version=11.10 os.cpe23=cpe:/o:canonical:ubuntu_linux:11.10 service.protocol=ssh fingerprint_db=ssh.banner)



## Server
Apache/2.2.20

## Programming language
PHP 

## Database 
MySql

## Pages
    

# findings                                                                                                              

* Priviledge escalsation

https://www.exploit-db.com/exploits/37292


# Evidence


