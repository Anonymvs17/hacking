# user 

# file of which user (example user uid: 1014)
f.e.. check file permissions (ls -al)
-rwx---------  1 1014 1014  48 Jun 21 08:31 creds.txt

## add user with name pwn
sudo adduser pwn
//generates uid 1001

## change uid 
//replaces all occurences from 1001 to 1014
sudo sed -i -e 's/1001/1014/g' /etc/passwd

## login as user
su pwn
or su - pwn

## checked uid of user
id

//check with shells are suppported 

cat /etc/shells 

//using different shell
shell

//getting bash with pyhton script usually works with shell
python -c "import pty;pty.spawn('/bin/bash')" 

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
* less => reads file
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

### text search and manipulation
### grep
//list files and search only for zip
ls -la /usr/bin | grep zip

### cut (cut can only acceppt single char as field delimiter)
//cutting something out of text
 echo "was, läuft, bei dir" | cut -f 2 -d ","
 //will print
 läuft

//from file (passwd): cutting first with : being the delimiter
cut -d ":" -f 1 /etc/passwd

### awk (can acceppt multiple char as field delimiter)
//removes "::" and returns first and 3rd group
echo "hello::how::are::you?" | awk -F "::" '{print $1, $3}'
hello are

### analysing file (advanced)
cat access.log | cut -d " " -f 1 | sort -u
//prints the ip addresses (unique)

## head (displays the first ten lines of a file)
head someFile.txt

## file editing
nano filename.txt

vi filename => then press I to change to insert text mode

## Comparing files
### comm
//prints out comparison, left handside unique for scan-a
comm scan-a.txt scan-b.txt

//just showns the common text
comm -12 scan-a.txt scan-b.txt

### diff
diff -c scan-a.txt scan-b.txt

### vmdiff (shows diffs seperated)

vmdiff scan-a.txt scan-b.txt

## background processes
bg

### return a job the foreground (just from the current cli)
#### see all jobs 
jobs
#### 1 being the job number
fg %1

### lists processes system wide (not only cli) => got to get clues
ps -ef 

//to get a specific process
ps -fC leafpad

//kill wiht process id
kill 1234

### file and commands monitoring
//montor logs at they are being logged 
tail -f /vat/log/apache2/access.log

## Download files or website (index file)
//download file via http or ftp protocolls
wget -O desiredName.pdf path

wget http://

### download or upload file 
curl -o report.pdf https://....

### useful for large downloads
axel -a -n 20 -o report.pdf https://...

## creating own commands with alias
 alias lsa='ls -la'

 //running it
 lsa

 ## bash behavior
 in "/etc/bash.bashrc"

 # backup linux
 sudo cp /etc/apt/sources.list /etc/apt/sources.list.backup

