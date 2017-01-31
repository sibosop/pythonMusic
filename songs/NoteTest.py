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
noteSeq = [72,70,68,67,65,63,62,60]

bassSeq = [70,74,75,77,79]

plickSeq = []
for x in noteSeq:
  plickSeq.append(x+24)


rbass = lambda: random.choice(bassSeq)
rch = lambda: chooseUnique(noteSeq,2)
noteChan=2
note=rp(reps=200,len=Tg('5:1:00'),event=el([
            [Tg('1:1:0'),nt(note=72,vel=lambda: random.randint(1,127),len=24,chan=noteChan)],
            [Tg('1:1:12'),nt(note=72,vel=lambda: random.randint(1,127),len=24,chan=noteChan)],
            [Tg('1:2:12'),nt(note=rbass,vel=lambda: random.randint(1,127),len=24,chan=noteChan)],
            [Tg('1:4:0'),nt(note=72,vel=lambda: random.randint(1,127),len=24,chan=noteChan)],
            [Tg('1:4:12'),nt(note=rbass,vel=lambda: random.randint(1,127),len=24,chan=noteChan)],
            [Tg('2:1:12'),nt(note=rbass,vel=lambda: random.randint(1,127),len=24,chan=noteChan)],
            [Tg('2:3:0'),nt(note=72,vel=lambda: random.randint(1,127),len=24,chan=noteChan)],
            [Tg('2:3:12'),nt(note=rbass,vel=lambda: random.randint(1,127),len=24,chan=noteChan)],
            [Tg('3:1:0'),nt(note=rbass,vel=lambda: random.randint(1,127),len=24,chan=noteChan)],
            [Tg('3:2:12'),nt(note=72,vel=lambda: random.randint(1,127),len=24,chan=noteChan)],
            [Tg('3:4:12'),nt(note=rbass,vel=lambda: random.randint(1,127),len=24,chan=noteChan)],
            [Tg('4:2:12'),nt(note=72,vel=lambda: random.randint(1,127),len=24,chan=noteChan)]
            ]))
chord1=rp(reps=100,len=lambda: 96 * random.randint(3,8),event=ch(chord=rch,vel=lambda: random.randint(1,127),len=lambda: random.randint(24,72),chan=1))
chord2=rp(reps=100,len=lambda: 96 * random.randint(1,3),event=ch(chord=rch,vel=lambda: random.randint(1,127),len=lambda: random.randint(24,159),chan=0))
plick=rp(reps=1000,len=lambda: random.choice([12,12,12,24,36,48]),event=nt(note = lambda: random.choice(plickSeq),vel=lambda: random.randint(1,127),len=lambda: random.randint(4,24),chan=3))
#len=lambda: random.randint(1,8)*24
ms.addEvent(Tg("1:1:0"),note)
ms.addEvent(Tg("5:2:18"),chord1)
ms.addEvent(Tg("1:1:0"),plick)
ms.addEvent(Tg("5:1:18"),chord2)


#ms.addEvent(Tg("20:1:1"),ms.togStartStop)
ms.run()