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

# Navigation 
/to root
ls -la /

//Navigation to usr path (incl. access rights)
ls -la /usr/

//displays hidden files, each file in each line (good for automation)
ls -a1



# editing files
* cat => just reads file
* gedit => opens editor
* nano (then interactions with f.i. ctrl + O for writing in file - saving)

# information (prints out information on command)
man ls 

# search for commands 
apropos someText

# search

//sarching recursivly all directories for a given file name
find / -name  md5*


# bash
//exporting variable
export myIP=192.168.0.31
//reading this variable
echo $myIP

## to see all environment variables
env

## command history (to see all comands that have been executed)
history 

//use it "!" and the number
!32

## redirecting (output to file)

//if file same will be overridden
echo "helloWorld" > somefile.txt

//if file exists will be appended
echo "helloWorld" >> somefile.txt

// errror reading
cd ./test 2>error.txt
//printing it out
cat error.txt leads to string in file: bash: cd: ./test: No such file or directory

## Piping
//redirect output of error.txt to wc command (wordcount) to redirect to a file amount.txt (which will contain f.e.: 32)
cat error.txt | wc -m > amount.txt


