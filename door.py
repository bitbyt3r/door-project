#!/usr/bin/python
import serial
import os
import RPi.GPIO as IO

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

class Motor:
  def __init__(self, pins, mode = "Normal", step = 0, resolution = 100, invert=False):
    self.pins = pins
    self.mode = mode
    self.step = 0
    self.resolution = 100
    if invert:
      self.low = IO.HIGH
      self.high = IO.LOW
    else:
      self.low = IO.LOW
      self.high = IO.HIGH
    IO.setmode(IO.BCM)
    for i in self.pins:
      IO.setup(i, IO.OUT, initial=IO.HIGH)

  def rotate(self, degrees):
    numSteps = int((degrees / 360) * self.resolution)
    if numSteps > 0:
      dir = "Forward"
    else:
      dir = "Backward"
      numSteps = numSteps * -1
    for i in xrange(numSteps):
      self.step(dir)

  def step(self, dir):
    self.pins[self.step], self.low)
    if dir == "Forward":
      self.step += 1
    if dir == "Backward":
      self.step += -1
    self.pins[self.step], self.high)
    
    
