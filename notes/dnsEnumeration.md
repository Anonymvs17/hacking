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



