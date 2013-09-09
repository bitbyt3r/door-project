#!/usr/bin/python
import serial
import os

os.system("./rpi-serial-console enable 9600")
port = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=3.0)

def getTag():
  tag = port.read(14)
  if tag[0] == 

