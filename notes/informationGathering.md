# Website
check website to get understanding
social media etc,

# Who is
name server, registrary

//check also name server (dns)
whois megacorpone.com | less

//reverse lookup of ip addresses
whois 102.231.31.13 | less

# Google hacking
broad search then norror operators
//site limites just to domian
site:megacorpone.com filetype:php

//exclude filetypes
site:megacorpone.com -filetype:php

//find pages that contains index of tile and parent directoy anywhere in the page
intitle:"index of" "parent directory"

## google hacking database
https://www.exploit-db.com/google-hacking-database

# netcraft 
Gather information about domain

# recon-ng
//start with
recon-ng

//need to add modules (search for modules "github")
marketplace search github

//info about modules => check if license key required
marketplace info github

//Marketplace install
marketplace install recon/domain-hosts/google_site_web

//load module
modules load recon/domain-hosts/google_site_web

//see info
info

//recon with modules
options set SOURCE mengacorpone.com

//view stored data
show hosts

//resolving hosts
modules load recon/hosts-hosts/resolve

# open source code
github, gitlab or sourceforge

# shodan (cralls devices connected to the internet)
Google search for webserver content
shodan for internet connected devices

# security headers
www.securityheaders.com


# analyse ssl and compars with current best practises
www.ssllabs.com

# Serachsploit
searchsploit cutenews

## check file info 
Filename: 21398
`searchsploit -x 21398`

## download file
`searchsploit -m 46698.rb`

# to gather emails, ips, subdomains, etc.
theharvester -d megacorpone.com -b google


