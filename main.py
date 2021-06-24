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
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    msg = msgFromServer[0].decode()
    msg = msg[1:-1].split(', ')
    # Testing
    data = msg[2:-1]
    print(msg[0])
    if msg[0] == "'ENN'":
        
        datapoints.append(int(msg[2]))
        timestamps.append(int(x))

y = datapoints #datapoints
x = timestamps
fig3, ax3 = plt.subplots()
ax3.plot(x, y, color='k')
ax3.autoscale(enable=True, axis="y", tight=False)
plt.show()
