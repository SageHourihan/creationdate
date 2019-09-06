'''
This program gets the file name and date created from any directory.
Developed by: Sage Hourihan
Date: 8/13/2019
'''

# importing modules
import os.path
import time
import csv

def date():
        
    # creating instructions and variables
    print ("File directory path: ")
    path = input(r"> ")
    print ("Output file name: ")
    name = input("> ")
    fname = name + '.csv' #file extension
    start_time = time.time() #timer for the program
    os.chdir(path) #setting the path to the user specified path

    # opening, writing and closing file
    f = open(fname, 'w+')
    for file in os.listdir(path):
        print(file + "\tCreated: %s" % time.ctime(os.path.getctime(file)))
        f.write(file + ',' + "Created: %s" % time.ctime(os.path.getctime(file)) +'\n')
    f.close()
    elapsed_time = round(time.time() - start_time,2) #stopping timer
    print('It took: ',elapsed_time, ' seconds to run.') # output