# MSF 

# WORKSPACES
# Create workspace
workspace -a

# Call workspaces
workspace

# Switch to workspace
workspace spaceName

## basics

//search
msf-pro > search platform:Windows
msf-pro > search type:exploit
msf-pro > search author:hd
msf-pro > search app:client
msf-pro > search name:ms08-067
//serach for contains http
grep http search type:exploit Apache


//Scanning dirs of webpages
auxiliary/scanner/http/dir_scanner

//in module use options not only show
options 

# Stage vs non staged payloads 

Overall there are non-staged  (pattern: linux/x86/shell_bind_ipv6_tcp) and staged (linux/x86/meterpreter/reverse_ipv6_tcp) on msf. stage will be done with a couple of smaller payloads
//settings different payload because the stage payload we provided might fail

set payload linux/ => hit double tab

see image ime/stagedVsNonStagedPayloads.png


# Adding custom modules

https://fmash16.github.io/content/writeups/hackthebox/htb-Passage.html

1) with searchsploit you can download file (see reconainssance)
2) save file in for instance:  /home/kali/.msf4/modules/exploits/cgi/webapps/ => having [exploits] or [auxilliary] is important
3) in msf reload modules by reload_all
4) custom module should appear

=> logs can be checked under: /home/kali/.msf4/logs/
![stagedVsNonStagedPayload](img/stagedVsNonStagedPayload.png)