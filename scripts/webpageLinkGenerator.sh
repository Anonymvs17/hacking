#! /bin/bash
wget=/usr/bin/wget
cat=/usr/bin/cat
grep=/usr/bin/grep

read -p 'target url: ' url
read -p 'filename: ' filename

echo "Extracting links for $page"

#command: wget -O - www.megacorpone.com > myfile.html
$wget -O - $url | $grep -Po '(?<=href=")[^"]*' > $filename

# get file
#file=`$cat $filename`




