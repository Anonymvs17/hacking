//info about user
id

//check with shells are suppported 

cat /etc/shells 

//using different shell
shell

//getting bash with pyhton script usually works with shell
python -c "import pty;pty.spawn('/bin/bash')" 

//login as different user in bash
su - paul

//check with shells are supported for which user
cat /etc/passwd

//just creds for given user www-data


//to check which shell i am using
ps -p $$

/Navigation to root
ls -la /

//Navigation to usr path (incl. access rights)
ls -la /usr/