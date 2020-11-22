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

# for AD and DNS
nmap -A -Pn -sC -sV 10.10.10.193
