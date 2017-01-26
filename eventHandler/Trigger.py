#!/usr/bin/python
import MidiScheduler
import sys

class Trigger(object):
  def __init__(self,spec):
    self.loop = 0
    self.measure = 0
    self.beat = 0
    self.tick = 0
    if spec.__class__.__name__ == 'int':
      self.tick = spec
    else:
      #print "Trigger spec:"+spec
      vals = spec.split(":")
      try:
        l = len(vals)
        #print "Trigger len:" + str(l) + " vals:" + str(vals)
        if l == 1:
          self.tick = int(vals[0])
        elif l == 3:
          self.measure = int(vals[0])-1
          self.beat = int(vals[1])-1
          self.tick = int(vals[2])
        elif l == 4:
          self.loop = int(vals[0])-1
          self.measure = int(vals[1])-1
          self.beat = int(vals[2])-1
          self.tick = int(vals[3])
        else:
          raise Exception("Trigger bad parameter:"+spec)
      except:
        print("Unexpected error:", sys.exc_info()[0])
        raise Exception(sys.exc_info()[0])
    #print "trigger init done"
    
  def v(self):
    ms = MidiScheduler.measureSize
    ls = MidiScheduler.loopSize
    return (self.loop*(ms*ls))+(self.measure*ms)+(self.beat*24)+self.tick
      