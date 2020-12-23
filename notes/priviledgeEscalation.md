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

# enumerating binaries that autoElevate
* on win ``reg query HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\Installer`` OR ``reg query HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\Installer`` is some of those are enabled any user can run windows installer packages with elevated priviledges
* Baniary is owned by root and has the suid bit set any user can execute this binary with elevating priviledges ``find / -perm -u=s -type f 2>/dev/null``, f.e.: if the copy command is suid set then we can copy to senenstive files



# automated enumeration
doing it manually takes too much time, thankfully can be automated, check [win-privesc-check](https://github.com/pentestmonkey/windows-privesc-check)
On linux: f.e.: https://github.com/leonteale/pentestpackage/blob/master/web_shells/unix-privesc-check
Automated good but it is important to watch out for manual configuration!