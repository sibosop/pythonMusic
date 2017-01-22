#!/usr/bin/python
import mido
import Singleton
from threading import Thread,Lock

class MidiScheduler(object):
  __metaclass__ = Singleton.Singleton
  def __init__(self,port):
    mido.set_backend('mido.backends.rtmidi')
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
        
  def addEvent(self,cnt,event):
    if self.eventList.has_key(cnt):
      print 'adding event ' + str(event) + ' at ' + str(cnt)
      self.eventList[cnt].append(event)
    else:
      print 'creating event ' + str(event) + ' at ' + str(cnt)
      self.eventList[cnt] = [event]
    