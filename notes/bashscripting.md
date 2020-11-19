# initial steps

//create file with nano
nono simple.sh

//to make it executable
chmod -x input.sh

//open file
./file.sh

# arguments

``
#! /bin/bash

echo "filename: $0, the first tow arguments are $1 and $2"
``
## call it with 
./simple.sh -boo -yolo

# user input
``
#! /bin/bash
read -p 'type you answer: ' answer
echo "your answer was: $answer"
``
### silent logging
for pw for example we can use -s as an read argument to not see the text when typing. f.e.: 
read -sp 'type your pw: ' pw

# if
if [ $age -lt 16 ]
then
fi

``
#!/bin/bash
# if statement

```
read -p 'What is your age: ' age

if [ $age -ge 18 ]
then
        echo "You are an adult"
fi
```

# logical operators
if [ $age -ge 18 ] && [ $age -ge 40 ]

# loops

## for
for ip in $(seq 1 10); do echo 10.11.1.$ip; done
for i in {1..10}; do

## while

```
#!/bin/bash
counter=1

while [ $counter -lt 10 ]
    do echo "10.11.1.$counter"
    ((counter++))
done
```

# functions
```
#!/bin/bash
# function should created before being called;
# arguments are being passed not with (arg1) instead via $1

print_me() {
    echo "yolooo $1"
}

# calling with argument Boo 
print_me Boo
```

