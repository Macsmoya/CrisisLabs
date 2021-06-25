
from csv import writer
import time
import random

filename = "data.csv"
# opening the file with w+ mode truncates the file
f = open(filename, "w+")
f.close()



def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)
append_list_as_row("data.csv", [0, 0])
for x in range(1, 300):
    time.sleep(1)
    append_list_as_row('data.csv', [x, random.randint(-1000,1000)])
    
    
