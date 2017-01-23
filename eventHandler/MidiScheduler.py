#!/usr/bin/python
import mido
import Singleton
from threading import Thread,Lock
from Event import CCEvent as cc
import sys

import time
loopSize=4
measureSize = 96

class Loop(object):
  loop=0
  measure=0
  beat = 0
  clock = 0
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
      if self.measure >= loopSize:
        raise Exception('bad measure param:'+str(self.measure))
    except:
      print("Unexpected error:", sys.exc_info()[0])
      raise 
      
  def count(self):
    rval = (self.loop*(loopSize*measureSize))+(self.measure*measureSize) + (self.beat*24) + self.clock
    print "measure count:"+str(rval)
    return rval
    
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
    except:
      print("Unexpected error:", sys.exc_info()[0])
      raise 
      
  def count(self):
    rval = (self.measure*measureSize) + (self.beat*24) + self.clock
    print "measure count:"+str(rval)
    return rval
    
class MidiScheduler(object):
  __metaclass__ = Singleton.Singleton
  
  def __init__(self,port):
    mido.set_backend('mido.backends.rtmidi')
    self.on=127
    self.off=0
    self.togStartStop = cc(0,self.on)
    self.muteAll = cc(127,self.on)
    self.reset=cc(126,self.on)
    
    self.measureSize = 96
    self.midiIn = mido.open_input(port,callback=self.eventHandler)
    self.midiOut = mido.open_output(port)
    self.running=False 
    self.first=False
    self.count=0
    self.realStart=False
    self.messages = {
      'clock' : self.clock
      ,'stop' : self.stop
      ,'start' : self.start
      ,'songpos' : self.songpos
      ,'continue' : self.cont
      ,'control_change': self.control_change
      ,'pitchwheel' : self.pitchwheel
    }
    self.eventList = {}
    
  def clock(self,msg):
    if self.running == False:
      print "clock while not running"
    if self.eventList.has_key(self.count):
      for e in self.eventList[self.count]:
        e.fire(self.midiOut) 
    self.count += 1
    #self.running = True
    self.first=True
    #print 'clock:'+str(msg)
    
  def stop(self,msg):
    print 'stop:'+str(msg)
    print "count:" + str(self.count)
    self.running = False
    self.count = self.count - 1
  
  def start(self,msg):
    print 'start:'+str(msg)
    self.running = True
    if self.realStart:
      print "doing real start"
      self.realStart = False
      self.count = 0
    print "count:" + str(self.count)
    
  def cont(self,msg):
    print 'cont:'+str(msg)
    print "count:" + str(self.count)
    if self.realStart:
      print "real continue"
      self.realStart = False
    self.running = True
    
  def songpos(self,msg):
    print 'songpos:'+str(msg)
    if not self.running:
      self.count = msg.pos * 6
    print "count:" + str(self.count)
  
  def control_change(self,msg):
    #print 'control_change:'+str(msg)
    if msg.channel == 15 and msg.control == 123:
      print "real start"
      self.realStart = True
  
  def pitchwheel(self, msg):
    #print 'pitchwheel'+str(msg)
    return

  def fire(self,ev):
    ev.fire(self.midiOut)

  def eventHandler(self,msg):
    self.messages[msg.type](msg)
    
  def loop(self):
    if ( self.running == False ):
      if self.first == True:
        print "clocks stopped"
        self.first = False
        self.realStart = False
        return False
    return True
        
  def addEvent(self,cnt,event):
    tmp = 0
    print "cnt type:"+cnt.__class__.__name__
    if cnt.__class__.__name__ == 'int':
      tmp = cnt
    else:
      tmp = cnt.count()
    if self.eventList.has_key(tmp):
      print 'adding event ' + str(event) + ' at ' + str(tmp)
      self.eventList[tmp].append(event)
    else:
      print 'creating event ' + str(event) + ' at ' + str(tmp)
      self.eventList[tmp] = [event]
      
  def run(self):
    self.fire(self.reset)
    self.fire(self.muteAll)
    self.fire(self.togStartStop)
    try:
      while self.loop():
        time.sleep(0.3)
    
    except:
      print("error:", sys.exc_info()[0])
      self.fire(self.togStartStop)