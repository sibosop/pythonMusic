#!/usr/bin/python
import mido

class CCEvent(object):
  cc=0
  val=0
  chan=0
  def __init__(self,cc,val,chan=0):
    self.cc = cc
    self.val = val
    self.chan = chan
    
  def fire(self,out):
    msg=mido.Message('control_change',value=self.val,control=self.cc,channel=self.chan)
    print msg
    out.send(msg)
    
    
