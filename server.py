import socket
import time

host = input('server IP, please: ')
port = 5000

clients = []

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind((host, port))
socket.setblocking(0)

quitting  = False
print ('\nServer Started\n')

while not quitting:
    try:
        data, address = socket.recvfrom(1024)

        if address not in clients:
            clients.append(address)
        
        print('receved from ' + str(address) + ' message: ' +  data.decode('utf-8'))
        for client in clients:
            socket.sendto(data, client)
    except:
        pass

socket.close()
