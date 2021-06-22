
import socket

serverAddressPort = ("152.67.115.238", 20001)
bufferSize = 1024
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPClientSocket.sendto(b"connect", serverAddressPort)
 
while True:
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    msg = msgFromServer[0].decode()
    # do stuff with message
