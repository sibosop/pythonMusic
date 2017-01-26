#!/usr/bin/python
import mido
import time
import random
from MidiScheduler import MidiScheduler 
from Trigger import Trigger as Tg
from CCEvent import CCEvent as cc
from Note import Note as nt
from Chord import Chord as ch
from EventList import EventList as el
from Repeat import Repeat as rp
from EvUtil import chooseUnique
import sys

ms = MidiScheduler(inPort='IAC Driver IAC Bus 2',outPort='IAC Driver IAC Bus 1')
off = ms.off
on = ms.on
random.seed()
noteSeq = [48,50,51,53,55,56,58,60,62,63,65,67,68,70]

bassSeq = []
for x in noteSeq:
  bassSeq.append(x-12)

rch = lambda: chooseUnique(noteSeq,4)
note=rp(reps=200,len=24,event=nt(note=lambda: random.choice(bassSeq),vel=lambda: random.randint(1,127),len=24,chan=1))
chord=rp(reps=100,len=lambda: random.randint(1,8)*24,event=ch(chord=rch,vel=lambda: random.randint(1,127),len=lambda: random.randint(1,48),chan=0))

#ms.addEvent(Tg("1:1:0"),note)
ms.addEvent(Tg("1:1:0"),chord)


ms.addEvent(Tg("20:1:1"),ms.togStartStop)
ms.run()