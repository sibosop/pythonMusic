#!/usr/bin/python
import time
import MidiScheduler
import Event

midiScheduler = MidiScheduler.MidiScheduler('IAC Driver IAC Bus 1')
off = 0
on = 127
midiScheduler.addEvent(360,Event.CCEvent(4,off))
midiScheduler.addEvent(384*4,Event.CCEvent(10,off))
togStartStop = Event.CCEvent(0,on)
muteAll = Event.CCEvent(127,on)
midiScheduler.addEvent((384*5) - 4,togStartStop)
midiScheduler.fire(muteAll)
midiScheduler.fire(togStartStop)
while 42:
  time.sleep(0.1)
  midiScheduler.loop();
  

