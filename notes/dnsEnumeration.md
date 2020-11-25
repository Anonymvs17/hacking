# how it works

1) you type www.megacorp.com
2) Goes to internal operating system DNS client (might have something cached)
2) request goes to your ISP's or Offices DNS Server (DNS recurser); two zone for each domain (forwars and reverse lookup zone)
3) Then to external root DNS server

# Forward lookup
## interacting with dns

//by default looks for ahost => generates IP addr
host www.megacorpone.com

//to find email server
host -t mx megacorpone.com

## findings dns servers
host -t ns megacorpone.com
//has three dns servers

## host transfers (zone file copies from master dns server to slave servers, many admins misconfigs this)
host -l megacorpone.com ns1.megacorpone.com

## bruteforcing 
can be automated with bash scripts
create file list.txt containing
``
mail
www
owa
proxy
router
``

iterating over this routelist with a for

## install seclist for proper data
apt install seclists

# Reverse lookup
host 20.203.12.31

# dnrecon

## zone transer
dnsrecon -d megacorpone.com -t axtf 

## bruteforce add. domains

//-D specifiy filename containing subdomain strings -t bruteforce
dnrecon -d megacorpone.com -D ~/list.txxt -t brt

# dnsenum
dnsenum zonetransfer.me
