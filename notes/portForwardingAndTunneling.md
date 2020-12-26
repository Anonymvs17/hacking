# port forwarding

For example: we have kali as debian server and have root of a client but this one can't access the internet. We can make it access the internet via google dns.

* on kali (first install): edit rinetd.conf file (216.x.x.x. google dns - connect address & port) ``0.0.0.0 80 216.58.207.142 80``
* on kali Restart service ``sudo service rinetd restart``
* on kali use ss to check that listening on port 80 ``ss -antp | grep "80"``
* on client check if connection possible ``nc -nvv 10.11.0.4 80``check also if our request was forwared to google dns

# ssh tunneling