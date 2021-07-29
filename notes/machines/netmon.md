# open ports

21/tcp  open  ftp          Microsoft ftpd
80/tcp  open  http         Indy httpd 18.1.37.13946 (Paessler PRTG bandwidth monitor)
135/tcp open  msrpc        Microsoft Windows RPC
139/tcp open  netbios-ssn  Microsoft Windows netbios-ssn
445/tcp open  microsoft-ds Microsoft Windows Server 2008 R2 - 2012 microsoft-ds
Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:mcrosoft:windows


# ftp 21
* login to ftp: `ftp -p IP`
User:  anonymous
Password:  anonymous@domain.com
http://help.websiteos.com/websiteos/using_anonymous_ftp_with_a_command_line_system.htm

Anonymous nmap port scan with `nmap -v -p 21 --script=/usr/share/nmap/scripts/ftp-anon.nse 10.129.1.126`
Output: 
tarting Nmap 7.91 ( https://nmap.org ) at 2021-03-25 17:04 EDT
NSE: Loaded 1 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 17:04
Completed NSE at 17:04, 0.00s elapsed
Initiating Ping Scan at 17:04
Scanning 10.129.1.126 [2 ports]
Completed Ping Scan at 17:04, 0.04s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 17:04
Completed Parallel DNS resolution of 1 host. at 17:04, 0.02s elapsed
Initiating Connect Scan at 17:04
Scanning 10.129.1.126 [1 port]
Discovered open port 21/tcp on 10.129.1.126
Completed Connect Scan at 17:04, 0.03s elapsed (1 total ports)
NSE: Script scanning 10.129.1.126.
Initiating NSE at 17:04
Completed NSE at 17:04, 0.26s elapsed
Nmap scan report for 10.129.1.126
Host is up (0.037s latency).

PORT   STATE SERVICE
21/tcp open  ftp
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
| 02-03-19  12:18AM                 1024 .rnd
| 02-25-19  10:15PM       <DIR>          inetpub
| 07-16-16  09:18AM       <DIR>          PerfLogs
| 02-25-19  10:56PM       <DIR>          Program Files
| 02-03-19  12:28AM       <DIR>          Program Files (x86)
| 02-03-19  08:08AM       <DIR>          Users
|_02-25-19  11:49PM       <DIR>          Windows

NSE: Script Post-scanning.
Initiating NSE at 17:04
Completed NSE at 17:04, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap

# Privliledge escalation

## Info gathering
### Programs installed
* WinPcap
* user pw found: PrTg@dmin2018 for prtgadmin as backup using later year PrTg@dmin2019 and works
* RCE can be created with msf module: windows/http/prtg_authenticated_rce
