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
    
  def fire(self,ms):
    msg=mido.Message('control_change',value=self.val,control=self.cc,channel=self.chan)
    print 'count:'+str(ms.count)+' '+str(msg)+' '+ms.__class__.__name__+' '+ms.midiOut.__class__.__name__
    ms.midiOut.send(msg)
    
    
class EventList(object):
  def __init__(self,list):
    self.list = list[:]
    self.iter = 0
    self.base = 0
    self.first = True
    
  def fire(self,ms):
    print "EventList"+" iter:"+str(self.iter)
    if self.iter == 0 and self.first:
      print "first is True"
      self.first = False
      self.base = ms.count
      offset = self.list[0][0].count()
      print "offset:"+str(offset)+" base:"+str(self.base)
      if (self.base+offset) != ms.count:
        ms.addEvent(self.base+offset,self)
        return
    print "fire"
    ms.fire(self.list[self.iter][1])
    self.iter = self.iter+1
    if self.iter == len(self.list):
      print "Eventlist at end of list:" +str(self.iter)+' '+str(len(self.list))
      self.iter = 0
      self.first = True
    else:
      ms.addEvent(self.list[self.iter][0].count()+self.base,self)
      