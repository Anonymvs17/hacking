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

