# simple network protocoll

1,2 & 2.3 no traffic encryption

# SNMP MIB Tree
Database containings info related to network management

## scan entire mib tree
snmpwalk -c public -v1 -t 10 10.11.1.14

# scan for snmp

// sU => udp; --open to only display open ports
sudo nmap -sU --open -p 161 10.11.1.1-254 -oG open-snmp.txt

# onesixty one
check scripts

onesixtyone is an SNMP scanner which utilizes a sweep technique to achieve very high performance. It can scan an entire class B network in under 13 minutes. It can be used to discover devices responding to well-known community names or to mount a dictionary attack against one or more SNMP devices.

onesixtyone takes a different approach to SNMP scanning. It takes advantage of the fact that SNMP is a connectionless protocol and sends all SNMP requests as fast as it can. Then the scanner waits for responses to come back and logs them, in a fashion similar to Nmap ping sweeps. By default onesixtyone waits for 10 milliseconds between sending packets, which is adequate for 100Mbs switched networks. The user can adjust this value via the -w command line option. If set to 0, the scanner will send packets as fast as the kernel would accept them, which may lead to packet drop.