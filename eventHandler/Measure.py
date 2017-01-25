#!/usr/bin/python

import MidiScheduler
class Measure(object):
  measure=0
  beat = 0
  clock = 0
  def __init__(self,spec):
    try:
      vals = spec.split(":")
      if len(vals) != 3:
        raise Exception('bad parameter')
      self.measure = int(vals[0])-1
      self.beat = int(vals[1])-1
      self.clock = int(vals[2])
      print "measure:"+str(self.measure)+" beat:"+str(self.beat)+" clock"+str(self.clock)
      if self.measure < 0 or self.beat < 0:
        raise Exception("negative counts")
    except:
      print("Unexpected error:", sys.exc_info()[0])
      raise 
      
  def count(self):
    rval = (self.measure*MidiScheduler.measureSize) + (self.beat*24) + self.clock
    print "measure count:"+str(rval)
    return rval