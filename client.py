import socket
import time
import threading

host = input('your ip, please: ')
port = 0

serverIP = input('server IP, please: ')

server = (serverIP, 5000)
quitting = False
threadLock = threading.Lock()

def Receve (name, sock):
    while not quitting:
        try:
            threadLock.acquire()
            while True:
                data, address = sock.recvfrom(1024)
                print(str(data))
        except:
            pass
        finally:
            threadLock.release()


socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind((host, port))
socket.setblocking(0)

receveThread = threading.Thread(target = Receve, args = ('Receving Messages', socket))
receveThread.start()

name = input('name: ')
message = input()
while message != 'q':
    if message != '':
        socket.sendto((message).encode(), server)
    message = input()

quitting = True
receveThread.close()
socket.close()

    
