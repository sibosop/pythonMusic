#!/usr/bin/python
import mido
import Singleton
from threading import Thread,Lock
from CCEvent import CCEvent as cc
import sys

import time
import Loop
import Measure

measureSize = 96
loopSize = 4

class MidiScheduler(object):
  __metaclass__ = Singleton.Singleton
  
  
  def __init__(self,inPort,outPort):
    mido.set_backend('mido.backends.rtmidi')
    self.on=127
    self.off=0
    
    self.togStartStop = cc(0,self.on)
    self.muteAll = cc(127,self.on)
    self.reset=cc(126,self.on)
    
    self.measureSize = 96
    self.midiIn = mido.open_input(inPort,callback=self.eventHandler)
    self.midiOut = mido.open_output(outPort)
    self.running=False 
    self.first=False
    self.ignoreFlag = False
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
    if self.ignoreFlag is False and self.eventList.has_key(self.count):
      for e in self.eventList[self.count]:
        e.fire(self) 
    self.ignoreFlag = False
    self.count += 1
    #self.running = True
    self.first=True
    #print 'clock:'+str(msg)
    
  def stop(self,msg):
    print 'stop:'+str(msg)
    print "count:" + str(self.count)
    self.running = False
    self.ignoreFlag = True
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
    ev.fire(self)

  def eventHandler(self,msg):
    #print str(msg)
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
    tmp = self.getCount(cnt)
    if self.eventList.has_key(tmp):
      print 'adding event ' + str(event) + ' at ' + str(tmp)
      self.eventList[tmp].append(event)
    else:
      print 'creating event ' + str(event) + ' at ' + str(tmp)
      self.eventList[tmp] = [event]
      
  def run(self):
    self.fire(self.reset)
    self.fire(self.togStartStop)
    try:
      while self.loop():
        time.sleep(0.3)
      
    except:
      print("error:", sys.exc_info()[0])
      self.fire(self.togStartStop)
      
    
  def getCount(self,tv):
    nm = tv.__class__.__name__
    if nm == 'int':
      return tv
    return tv.count()
