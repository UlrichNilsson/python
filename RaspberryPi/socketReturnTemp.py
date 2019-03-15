#!/usr/bin/env python3

import socket
import sys
import os
import glob
import time
import pickle

mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        #temp_c = float(temp_string) / 1000.0
        #temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_string#temp_c#, temp_f


try:
    mysock.bind(("",80))
except socket.error:
    print("Failed to bind")
    sys.exit()
mysock.listen(5)
while True:
    conn, addr = mysock.accept()
    data = conn.recv(1000)
    if not data:
        break
#conn.sendall(b'Got a request!')
    print(read_temp)
    conn.sendall(read_temp.decode("utf-8"))
    
conn.close()
mysock.close()

