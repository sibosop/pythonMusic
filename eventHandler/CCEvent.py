#!/usr/bin/python
import mido


class CCEvent(object):
  def __init__(self,cc,val,chan=0):
    self.cc = cc
    self.val = val
    self.chan = chan
    
  def fire(self,ms):
    msg=mido.Message('control_change',value=self.val,control=self.cc,channel=self.chan)
    print 'count:'+str(ms.count)+' '+str(msg)+' '+ms.__class__.__name__+' '+ms.midiOut.__class__.__name__
    ms.midiOut.send(msg)