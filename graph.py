from csv import writer
import time
import random
import math as maths
import socket
import numpy as np
import pandas as pd

serverAddressPort = ("152.67.115.238", 20001)
bufferSize = 1024
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPClientSocket.sendto(b"connect", serverAddressPort)


class Channel():
    def __init__(self, name):
        self.name = name
        self.path = "data/" + name + ".csv"
        self.datapoints = 0.0
        self.create_clear()
        self.addpacket([[0,0]])
        
    def create_clear(self):
        f = open(self.path, "w+")
        f.close()

    def addpacket(self, elem):
        data = enumerate(elem)  
        append_list_as_rows(self.path, data)
        self.datapoints +=0.01
        

def append_list_as_rows(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        for point in list_of_elem:
            csv_writer.writerow(point)
        
def getMsg():
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    msg = msgFromServer[0].decode()
    msg = msg.replace("'", "")
    msg = msg[1:-1].split(', ')
    return msg
        
def main():
    channels = [ Channel(channel_name) for channel_name in ['ENN', 'ENZ', 'EHZ', 'ENE']]
    for channel in channels:
        print(channel.name)
        
    running = True
    while running == True:
        msg = getMsg()
        for channel in channels:
            if channel.name == msg[0]:
                channel.addpacket(msg[2:])

main()    
        
    
    
