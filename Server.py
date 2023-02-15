import socket
import sys
import time

s = socket.socket()
host = input(str('Please enter the host you want to connect to : '))
port = 1025

try:
    s.connect((host,port))
    print('Connected to Host')
except:
    print('Connection Failed')

while 1:
    incoming_msg = s.recv(1024)
    incoming_msg = incoming_msg.decode()   
    print('Reply -> ',incoming_msg)     

    msg = input('Enter your message -> ')    
    msg = msg.encode()    
    s.send(msg)