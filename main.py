import socket
import numpy as np
import matplotlib.pyplot as plt

serverAddressPort = ("152.67.115.238", 20001)
bufferSize = 1024
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPClientSocket.sendto(b"connect", serverAddressPort)


datapoints = []
timestamps = []
for x in range (10):
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    msg = msgFromServer[0].decode()
    msg = msg[1:-1].split(', ')
    # Testing
    data = msg[2:-1]
    print(data)
    datapoints.append(msg[2])
    timestamps.append(x)
plt.plot(timestamps, datapoints)    

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('My first graph!')
  
# function to show the plot
plt.show()
