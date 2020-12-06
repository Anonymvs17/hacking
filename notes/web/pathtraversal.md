# gobuster
gobuster  dir -u http://192.168.0.11:443 -w /usr/share/wordlists/dirb/big.txt -s 403,404
// -x sh,pl => appens sh or pl
//you can also run small.txt 
//will serach for 200 and 403 responses
gobuster dir -u http://10.10.10.56/cgi-bin/ -w /usr/share/wordlists/dirb/small.txt -s 403,200 -x sh

# wfuss
wfuzz -c -w /usr/share/seclists/Discovery/Web-Content/common.txt --hc 404,403 -u "http://10.10.10.191/FUZZ.txt" -t 100

# dirb
//delay of 10 ms for each request
dirb http//www.megacorpone.com -r -z 10