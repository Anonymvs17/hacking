# netbios: network basic input and output system (port 139 & serval udp port)
facilitates and allows communication between computers on a local networks 
Session layer protocol an service that allows hosts in a local network to communicate with each other.
// but netbios over TCP/IP also outside of subnets
## in powershell 
//to display information about a system
nbtstat -A 192.168.0.13 

# SMB (445)
seperate protocoll from netbios
modern application can work without netbios, netbios over tcp is required and is ofter enabled together

# nmap scanning
nmap -v -p 139,445 -oG smb.txt 10.11.1.1-254

## vulnscripts
ls -l /usr/share/nmap/scripts/smb-vuln-*

# nbtscan 
//find all computers in a windows network; 
//-r tackles port 137 which is UDP netbios name service
sudo nbtscan -r 10.11.1.0/24