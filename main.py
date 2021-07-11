import socket
import numpy as np
import matplotlib.pyplot as plt

serverAddressPort = ("152.67.115.238", 20001)
bufferSize = 1024
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPClientSocket.sendto(b"connect", serverAddressPort)


datapoints = []
timestamps = []
for x in range (100):
    print(x)
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    print(x)
    msg = msgFromServer[0].decode()
    msg = msg[1:-1].split(', ')
    # Testing
    data = msg[2:-1]
    csv_lst = [x for x in enumerate(data)]
    print(msg)
