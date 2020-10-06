# Type of attacks
Overall there are different types of attacks depending on the OSI layer.

lvl 7 (application): https floods (most common), dns query floods
lvl 6 (presentation): SSL abuse 
lvl 5 (session): -
lvl 4 (transport): syn flood
lvl 3 (data): UDP reflection attacks

see img/typesOfDosAttacks
![Types of attacks](img/typeofDosAttacks.png)

# Slowloris
Type: 
//1. download git repository
//2. run
python3 slowloris.py -u www-qa.fiskars.com -s 300 -p 80