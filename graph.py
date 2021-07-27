from csv import writer
import time
import random
import math as maths
import socket
import numpy as np

serverAddressPort = ("152.67.115.238", 20001)
bufferSize = 1024
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPClientSocket.sendto(b"connect", serverAddressPort)


FILENAME = "data/data.csv"
# opening the file with w+ mode truncates the file
f = open(FILENAME, "w+")
f.close()



def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

append_list_as_row(FILENAME, [0, 0])

for i in range (100):
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    msg = msgFromServer[0].decode()
    msg = msg[1:-1].split(', ')
    # Testing
    data = msg[2:-1]
    csv_lst = [x for x in enumerate(data)]
    print(msg)
    if msg[0] == "'ENN'":
        append_list_as_row(FILENAME, (i, msg[3]))
        
    
    
