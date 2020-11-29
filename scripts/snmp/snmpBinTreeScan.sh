#! /bin/bash

echo 'runs snmp bin tree scan'
read -p 'first three ip oktects: (f.i 10.11.1) ' baseIp
read -p 'min of 4th octet: ' min
read -p 'max of 4th octet: ' max

for ip in $(seq $min $max); do echo $baseIp.$ip; done  > ips
#for ip in $(seq 1 254); do echo 10.11.1.$ip; done > ips

echo 'done, check results file'
onesixtyone -c community -i ips > results

