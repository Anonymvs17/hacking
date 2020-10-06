# open and read file
#f = open("demofile2.txt", "r");print(f.read())

#open bash, can call it with pyhton -c "those commands"
#import pty; pty.spawn('/bin/bash');


#echo "import pty; pty.spawn('/bin/bash')" > /tmp/real_term.py
#python /tmp/real_term.py

###############
# create a file
f = open("demofile1.txt", "w")

##write in a file
f.write("Woops! I have deleted the content!")
f.close()
#f = open('demo.py', 'w');f.write('import pty;pty.spawn(\"/bin/bash\")');f.close();

##reads in a file
f = open("demofile1.txt", "r")
print(f.read())

##################


python -c "import pty;pty.spawn('/bin/bash')"