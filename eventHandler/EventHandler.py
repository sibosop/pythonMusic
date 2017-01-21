#!/usr/bin/python
import time
import MidiScheduler

midiScheduler = MidiScheduler.MidiScheduler('IAC Driver IAC Bus 1')

while 42:
  time.sleep(0.1)
  midiScheduler.loop();
  

