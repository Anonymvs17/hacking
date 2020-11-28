# simple network protocoll

1,2 & 2.3 no traffic encryption

# SNMP MIB Tree
Database containings info related to network management

## scan entire mib tree
snmpwalk -c public -v1 -t 10 10.11.1.14
# scan for snmp

// sU => udp; --open to only display open ports
sudo nmap -sU --open -p 161 10.11.1.1-254 -oG open-snmp.txt

