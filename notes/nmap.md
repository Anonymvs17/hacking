# NMAP

## network scanning: iterate over all ip adresses within a given network
### nmap
nmap -sP 192.168.0.0/24

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