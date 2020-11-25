#! /bin/bash

# will be used if nothing is provided by user
url=megacorpone.com

read -p 'targeted url (without "www"): ' url
read -p 'desired name of file: ' name

#dnsServers=$(host -t ns $url)
# Define a timestamp function
timestamp() {
  date +"%T" # current time
}

filename=$name$(date +%s).txt

for i in $(host -t ns $url | cut -f 4 -d " " | sed 's/.$//')
do 
	echo "--------trying zone transfer for: $i--------"
	host -l $url $i >> $filename
done
echo "created file: $filename"
