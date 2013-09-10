#!/usr/bin/python
import serial
import os

#os.system("./rpi-serial-console enable 9600")
port = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=30.0)

def getTag():
  while True:
    port.flushInput()
    data = [ord(x) for x in port.readline(14)]
    return data

def rotate(l,n):
    return l[n:] + l[:n]

def checkTag(tag):
  for i in xrange(len(tag)):
    tag = rotate(tag, 1)
    if len(tag) != 14:
      continue
    if tag[0] != 2 and tag[-1] != 3:
      continue
    return tag
  return False

while True:
  tag = getTag()
  tag = checkTag(tag)
  if tag:
    print "Found Valid Tag:", tag


