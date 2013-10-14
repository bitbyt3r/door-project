#!/usr/bin/python

import threading

class Motor (threading.Thread):
  def run(self):
    with printLock:
      print "testing, Motor"
    while True:
      old
  
class Reader (threading.Thread):
  def run(self):
    with printLock:
      print "testing, Reader"
    
class ExtInt (threading.Thread):
  def run(self):
    with printLock:
      print "testing, External"
  
printLock = threading.Lock()
  
doorMotor = Motor()
cardReader = Reader()
externalInput = ExtInt()

doorMotor.start()
cardReader.start()
externalInput.start()