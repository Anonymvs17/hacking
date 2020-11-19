# info (port 111)
distributes file system protocol, accessing files like local, unix based

# nmap 
scripts at: 
ls -l /usr/share/nmap/scripts/rpc*
ls -l /usr/share/nmap/scripts/nfs*

nmap -sV -p 111 --script=rpcinfo.nse 10.11.1.1-254

# run all scripts on specific host
nmap -p 111 --script=nfs* 10.11.1.72

// if mount is available: nolock to disable file locking
sudo mount -o nolock 10.11.1.72:/home ~/home/

