#!/usr/bin/python
import RPi.GPIO as GPIO
import time

singlePattern = [[0],[1],[2],[3]]
doublePattern = [[0,1],[1,2],[2,3],[3,0]]
halfPattern = [[0],[0,1],[1],[1,2],[2],[2,3],[3],[3,0]]

class Motor:
  def __init__(self):
    self.stepsPerRotation = 200
    self.RPM = 30
    self.stepTime = 1.0/((self.stepsPerRotation*self.RPM)/60)
    self.pins = [21,22,23,24]
    self.current_pos = 0

    self.__setup()

  def step(self, pattern=singlePattern, direction=True):
    for i in xrange(len(self.pins)):
      if i in pattern[self.current_pos]:
        GPIO.output(self.pins[i], True)
      else:
        GPIO.output(self.pins[i], False)
    self.current_pos -= 1
    if direction:
      self.current_pos += 2
    self.current_pos %= len(pattern)

  def release(self):
    for i in self.pins:
      GPIO.output(i, False)

  def __setup(self):
    GPIO.setmode(GPIO.BCM)
    for i in self.pins:
      GPIO.setup(i, GPIO.OUT)
      GPIO.output(i, False)

  def run(self, rotations, direction=True):
    for i in xrange(int(rotations*self.stepsPerRotation)):
      self.step(direction=direction)
      time.sleep(self.stepTime)
