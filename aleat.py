#!/usr/bin/python3
"""
Simple HTTP Server
Jesus M. Gonzalez-Barahona and Gregorio Robles
{jgb, grex} @ gsyc.es
SAT and SARO subjects (Universidad Rey Juan Carlos)
"""

import socket
import random

# Create a TCP objet socket and bind it to a port
# We bind to 'localhost', therefore only accepts connections from the
# same machine
# Port should be 80, but since it needs root privileges,
# let's use one above 1024

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind(('localhost', 1234))


# Queue a maximum of 1 TCP connection requests

mySocket.listen(1)

# Accept connections, read incoming data, and answer back an HTML page
#  (in an infinite loop)

while True:
    urlaleatoria = random.randint(1,999999999)
    print('Waiting for connections')
    (recvSocket, address) = mySocket.accept()
    print('HTTP request received:')
    print(recvSocket.recv(1024))
    recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
                    "<html><body><h1>Hola.<a href='http://localhost:1234/"+ str(urlaleatoria) + "'> Ponme otra de lo mismo</a></h1></body></html>" +
                    "\r\n", 'utf-8'))
recvSocket.close()
