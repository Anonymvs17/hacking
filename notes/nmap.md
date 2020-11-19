# NMAP

## network scanning: iterate over all ip adresses within a given network => /24 stands for class C network
### nmap
nmap -sP 192.168.0.0/24

# just can port of within a network 
//-A aggressive scanning, -oG to save output in a file
nmap -A -p80 --open 10.11.1.0/24 -oG nmap-scan_10.11.1.1.-254

### arp scan
//scanning local network
sudo arp-scan -l

# Detect Services
nmap -sV 192.168.0.12

# Detect OS
nmap -A 192.168.0.1

# Scan all ports (not just top 1000)
sudo nmap -T4 -p- -A 192.168.0.6

# for AD and DNS => A OS version detection
nmap -A -Pn -sC -sV 10.10.10.193

# UDP 
is stateless so no three way handshake
usually if port is close ICMP port unreachable should appear
for common port => protocoll specific packet

# stealth scan default in nmap
syn => syn/ack => no final ack send by nmap, 
because the 3ways handshake is not completed does not reach application layer (appliction logs)

# UDP scanning
sudo nmap -sU 10.11.1.115

# TCP connect scan (usually for proxies)
nmap -sT -A --top-ports=20 10.1.1.1-254

# ping and save output to file
nmap -v -sn 10.11.1.1-254 -oG ping-sweep.txt

//grab file
grep Up ping-sweep.txt | cut .... | head
# MASScan (DON NOT RUN)
can easily handle type A & B network
was desing to scan the whole internet in 6 min

sudo masscan -p80 10.11.1.0/24 --rate=100 -e tab0 --router-ip 10.11.0.1

# nmap scripts
//contains useful scripts for example for smb
ls -l /usr/share/nmap/scripts/smb*

## running 1 script
nmap -v -p 139,445 --script=smb-os-discovery 10.11.1.227

## running all scripts
nmap -p 139,445 --script=smb* 10.11.1.227
