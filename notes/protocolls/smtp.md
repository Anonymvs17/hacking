# mail servers

## receiving mails
### pop3
Receiving emails from a server to a local email client
Allows downloading email messages to read them offline
message are downloaded locally and removed from webserver (bad for multiple devices) 

Port 110 non-encrypted
Port 995 encrypted

## retrieving mails
### imap
used for accessing emails on a remote webserver
allows simultanous access

Port 143 unencrypred
Port 993 encrypted

## sending emails

### SMTP
Port 25 unencrypred
Port 2525 in case port 25 is filered and you want to send enencrypred mails
Port 465 encrypted

#### commands

verify 
expand (memebershop of mailing list)

##### verify

//connecting to port 25 on a mail servers
nc -nv 10.11.1.217 25 

// verify root
VRFY root

VRFY NonExistingUsers

# to enumerate users
smtp-user-enum -M VRFY -U /usr/share/wordlists/dirb/common.txt -t 192.168.2.4
