#!/usr/bin/python
import mido
from threading import Thread,Lock

class MidiScheduler(object):
  def clock(self,msg):
    if self.running == False:
      print "clock while not running" 
    self.count += 1
    self.running = True
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
      self.realStart = False;
      self.count = 0
    print "count:" + str(self.count)

  def songpos(self,msg):
    print 'songpos:'+str(msg)
    print "count:" + str(self.count)
  
  
  def control_change(self,msg):
    #print 'control_change:'+str(msg)
    if msg.channel == 15 and msg.control == 123:
      print "real start"
      self.realStart = True
  
  def pitchwheel(self, msg):
    print 'pitchwheel'+str(msg)

  def cont(self,msg):
    print 'cont:'+str(msg)
    print "count:" + str(self.count)
    self.running = True

  def eventHandler(self,msg):
    self.messages[msg.type](msg)
    
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
    
  def loop(self):
    if ( self.running == False ):
      if self.first == True:
        print "clocks stopped"
        self.first = False
        self.realStart = False