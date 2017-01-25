#!/usr/bin/python
import mido
import time
import random
from MidiScheduler import MidiScheduler 
from Measure import Measure as Me
from Loop import Loop as Lo
from CCEvent import CCEvent as cc
from Note import Note as nt
from EventList import EventList as el
import sys

ms = MidiScheduler(inPort='IAC Driver IAC Bus 2',outPort='IAC Driver IAC Bus 1')
off = ms.off
on = ms.on
random.seed()
noteSeq = [60,62,64,65,67,69,71]

ms.addEvent(Me("1:1:0"),nt(note=lambda: random.choice(noteSeq),vel=lambda: random.randint(1,127),len=lambda: random.randint(1,48),chan=0))
ms.addEvent(Me("2:1:0"),nt(note=lambda: random.choice(noteSeq),vel=lambda: random.randint(1,127),len=lambda: random.randint(1,48),chan=0))
ms.addEvent(Me("3:1:0"),nt(note=lambda: random.choice(noteSeq),vel=lambda: random.randint(1,127),len=lambda: random.randint(1,48),chan=0))
ms.addEvent(Me("4:1:0"),nt(note=lambda: random.choice(noteSeq),vel=lambda: random.randint(1,127),len=lambda: random.randint(1,48),chan=0))
ms.addEvent(Me("5:1:0"),nt(note=lambda: random.choice(noteSeq),vel=lambda: random.randint(1,127),len=lambda: random.randint(1,48),chan=0))
ms.addEvent(Me("8:1:1"),ms.togStartStop)
ms.run()