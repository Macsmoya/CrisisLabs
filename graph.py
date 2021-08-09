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
    def __init__(self, name, start_time):
        self.name = name
        self.path = "data/" + name + ".csv"
        self.datapoints = 0.0
        self.create_clear()
        self.start_time = start_time
        self.last_value = 0
        self.addpacket(0, [0])
        
    def create_clear(self):
        f = open(self.path, "w+")
        f.close()

    def addpacket(self, time, elems):
        detrended_elems = detrend(self.last_value, elems) #Detrend data
        self.last_value = elems[-1]
        
        data = []                                         #Give each datapoint timestamps
        time_since_start = float(time) - float(self.start_time)
        for i in range(0, len(elems)):
            data.append([time_since_start + i * 0.01, detrended_elems[i]])
        
        append_list_as_rows(self.path, data)
        self.datapoints +=0.01
     
def detrend(start, lst):
    if len(lst) == 0:
        return lst
    else:
        return [float(lst[0]) - float(start)] + detrend(lst[0], lst[1:])

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
    init_msg = getMsg()
    
    channels = [ Channel(channel_name, float(init_msg[1])) for channel_name in ['ENN', 'ENZ', 'EHZ', 'ENE']]
    for channel in channels:
        print(channel.name)
        
    running = True
    while running == True:
        msg = getMsg()
        for channel in channels:
            if channel.name == msg[0]:
                channel.addpacket(msg[1], msg[2:])
                

main()    
        
    
    
