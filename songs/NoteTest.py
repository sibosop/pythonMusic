#!/usr/bin/python
import mido
import time
import random
from MidiScheduler import MidiScheduler 
from Trigger import Trigger as Tg
from CCEvent import CCEvent as cc
from Note import Note as nt
from EventList import EventList as el
from Repeat import Repeat as rp
import sys

ms = MidiScheduler(inPort='IAC Driver IAC Bus 2',outPort='IAC Driver IAC Bus 1')
off = ms.off
on = ms.on
random.seed()
noteSeq = [60,62,64,65,67,69,71]
newSeq=noteSeq[:]
for x in noteSeq:
  x -= 12
  newSeq.append(x)
noteSeq = newSeq[:]
  
note=rp(reps=100,len=24,event=nt(note=lambda: random.choice(noteSeq),vel=lambda: random.randint(1,127),len=lambda: random.randint(1,48),chan=lambda: random.randint(0,1)))

ms.addEvent(Tg("1:1:0"),note)

ms.addEvent(Tg("20:1:1"),ms.togStartStop)
ms.run()