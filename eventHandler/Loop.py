#!/usr/bin/python
import MidiScheduler
import sys

class Loop(object):
  def __init__(self,spec):
    try:
      vals = spec.split(":")
      if len(vals) != 4:
        raise Exception('bad parameter')
      self.loop = int(vals[0])-1
      self.measure = int(vals[1])-1
      self.beat = int(vals[2])-1
      self.clock = int(vals[3])
      print "Loop:"+str(self.loop)+" measure:"+str(self.measure)+" beat:"+str(self.beat)+" clock"+str(self.clock)
      if self.loop < 0 or self.measure < 0 or self.beat < 0:
        raise Exception("negative counts")
      if self.measure >= MidiScheduler.loopSize:
        raise Exception('bad measure param:'+str(self.measure))
    except:
      print("Unexpected error:", sys.exc_info()[0])
      raise 
      
  def count(self):
    rval = (self.loop*(MidiScheduler.loopSize*MidiScheduler.measureSize))+(self.measure*MidiScheduler.measureSize) + (self.beat*24) + self.clock
    print "loop count:"+str(rval)
    return rval