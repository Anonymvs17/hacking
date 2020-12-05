# simple network protocoll
used for tracking health of device, switchtes, etc. Like for instance temperature

1,2 & 2.3 no traffic encryption, use "community string", no username

# SNMP MIB Tree
Database containings info related to network management
contains OIDs (object ids) - like for instance of temperature, status types
f.e.: 
oid |   name     |type       |   status type    | explainatinon
.2  | temperature| Integer   | -                | Temperature of the NAS 

## scan entire mib tree
// -c community, version 1 & timout 10 sec
snmpwalk -c public -v1 -t 10 10.11.1.14

###  enumerate users on windows system
snmpwalk -c public -v1 10.11.1.14 1.3.6.1.4.1.77.1.2.25

### enumerate running windows processes
snmpwalk -c public -v1 10.11.1.73 1.3.6.1.2.1.25.4.2.1.2

### enumerate open tcp ports
snmpwalk -c public -v1 10.11.1.73 1.3.6.1.2.1.6.13.1.3

### enumerating installed software
snmpwalk -c public -v1 10.11.1.73 1.3.6.1.2.1.25.6.3.1.2

# scan for snmp

// sU => udp; --open to only display open ports
sudo nmap -sU --open -p 161 10.11.1.1-254 -oG open-snmp.txt

# onesixty one
check scripts

onesixtyone is an SNMP scanner which utilizes a sweep technique to achieve very high performance. It can scan an entire class B network in under 13 minutes. It can be used to discover devices responding to well-known community names or to mount a dictionary attack against one or more SNMP devices.

onesixtyone takes a different approach to SNMP scanning. It takes advantage of the fact that SNMP is a connectionless protocol and sends all SNMP requests as fast as it can. Then the scanner waits for responses to come back and logs them, in a fashion similar to Nmap ping sweeps. By default onesixtyone waits for 10 milliseconds between sending packets, which is adequate for 100Mbs switched networks. The user can adjust this value via the -w command line option. If set to 0, the scanner will send packets as fast as the kernel would accept them, which may lead to packet drop.