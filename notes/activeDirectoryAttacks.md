# Theory
When an instance of Active Directory is configured, a domain is created with a name such as corp.com where corp is the name of the organization. Within this domain, we can add various types of objects, including computer and user objects.
System administrators can (and almost always do) organize these objects with the help of Organizational Units (OU)

Typically, client computers on an internal network are connected to the domain controller and to various other internal member servers such as database servers, file storage servers, etc.

An Active Directory environment has a very critical dependency on a Domain Name System (DNS) service. As such, a typical domain controller in an AD will also host a DNS server that is authoritative for a given domain.


# Active Directory Enumeration

## Traditional approach
an attack against Active Directory infrastructure begins with a successful exploit or client-side attack against either a domain workstation or server followed by enumeration of the AD environment.

* administrators use groups to assign permissions to member users, which means that during our assessment, we would target high-value groups. Usually very interesting: Domain Admins group
* `net user` enumerate all local user accounts (an workstation)
* `net user /domain` enumerate entire domain
* Once we done this, we can now query information about individual users (f.e.: *jeff_admin*)
* First we should look for *jeff_admin* (usually DC tend to give roles descriptions and pre/suffix), `net user jeff_admin /domain` => there we can check the global group membership
* To check for groups existing groups: `net group /domain` where me might find some secret groups - a group (and subsequently all the included members) can be added as member to another group. This is known as a nested group.
*the net.exe command line tool cannot list nested groups and only shows the direct user members*

## a modern approach for bigger networks
We will develop a powershell script that will enumerate the AD users along with all the properties of those user accounts.
We will use a DirectorySearcher object to query Active Directory using the *Lightweight Directory Access Protocol (LDAP)*, which is a network protocol understood by domain controllers also used for communication with third-party applications.
LDAP is an Active Directory Service Interfaces (ADSI) provider (essentially an API) that supports search functionality against an Active Directory.

* Our script will center around a very specific LDAP provider path: `LDAP://HostName[:PortNumber][/DistinguishedName]`
*more information will follow*

## useful blog

https://medium.com/@adam.toscher/top-five-ways-i-got-domain-admin-on-your-internal-network-before-lunch-2018-edition-82259ab73aaa

