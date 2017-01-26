#!/usr/bin/python

from MidiScheduler import MidiScheduler 
from Trigger import Trigger as tg
from CCEvent import CCEvent as cc
from EventList import EventList as el
import sys

ms = MidiScheduler(inPort='IAC Driver IAC Bus 2',outPort='IAC Driver IAC Bus 1')
off = ms.off
on = ms.on

class Tr(object):
  unused,bd3,snrd,midd,pink,bd1,clp,pluckb,tink,bd1Stretch,revBd3,pluckwah,bell,pluckbell,pluckbell1,pluckbell2,pluckbell3,beattone1,beattone2=range(19)
  
revSound=el([[tg("1:1:1:0"),cc(Tr.revBd3,off)],[tg("2:1:1:0"),cc(Tr.revBd3,on)]])

pluckWah=el([[tg("1:4:1:0"),cc(Tr.pluckwah,off)],
  [tg("2:1:1:0"),cc(Tr.bell,off)],
  [tg("3:1:1:0"),cc(Tr.bell,on)],
  [tg("4:1:1:0"),cc(Tr.bell,off)],
  [tg("5:1:1:0"),cc(Tr.bell,on)],
  [tg("5:4:1:0"),cc(Tr.pluckwah,on)]])
  
beattone=el([[tg("1:4:1:0"),cc(Tr.beattone1,off)],
  [tg("3:4:1:0"),cc(Tr.beattone1,on)],
  [tg("3:4:1:0"),cc(Tr.beattone2,off)],
  [tg("4:4:1:0"),cc(Tr.beattone2,on)],
  [tg("4:4:1:0"),cc(Tr.beattone1,off)],
  [tg("5:4:1:0"),cc(Tr.beattone1,on)]])

pluckbell=el([[tg("1:4:1:0"),cc(Tr.pluckbell,off)],
  [tg("2:1:1:0"),cc(Tr.pluckbell1,off)],
  [tg("3:1:1:0"),cc(Tr.pluckbell1,on)],
  [tg("3:1:1:0"),cc(Tr.pluckbell2,off)],
  [tg("4:1:1:0"),cc(Tr.pluckbell2,on)],
  [tg("4:1:1:0"),cc(Tr.pluckbell1,off)],
  [tg("5:1:1:0"),cc(Tr.pluckbell1,on)],
  [tg("5:1:1:0"),cc(Tr.pluckbell3,off)],
  [tg("5:4:1:0"),cc(Tr.pluckbell,on)],
  [tg("6:1:1:0"),cc(Tr.pluckbell3,on)]])


ms.addEvent(tg("1:4:1:0"),cc(Tr.pink,off))

ms.addEvent(tg("3:1:1:0"),cc(Tr.bd1Stretch,off))

ms.addEvent(tg("5:1:1:0"),revSound)
ms.addEvent(tg("5:4:1:0"),cc(Tr.pluckb,off))

ms.addEvent(tg("7:4:1:0"),cc(Tr.bd1,off))
ms.addEvent(tg("8:1:1:0"),cc(Tr.clp,off))
ms.addEvent(tg("9:1:1:0"),revSound)
ms.addEvent(tg("9:4:3:0"),cc(Tr.snrd,off))

ms.addEvent(tg("10:4:4:20"),cc(Tr.bd3,off))

ms.addEvent(tg("12:1:1:0"),cc(Tr.tink,off))

ms.addEvent(tg("13:1:1:0"),revSound)
ms.addEvent(tg("13:1:1:0"),pluckWah)


ms.addEvent(tg("20:1:1:0"),revSound)
ms.addEvent(tg("20:1:1:9"),pluckbell)


ms.addEvent(tg("25:1:1:0"),revSound)
ms.addEvent(tg("25:1:1:0"),pluckWah)

ms.addEvent(tg("31:1:1:0"),beattone)


ms.addEvent(tg("38:1:1:0"),pluckWah)
ms.addEvent(tg("38:1:1:0"),beattone)


ms.addEvent(tg("45:4:1:0"),cc(Tr.bd1,on))
ms.addEvent(tg("46:1:1:0"),cc(Tr.clp,on))
ms.addEvent(tg("47:4:4:20"),cc(Tr.tink,on))
ms.addEvent(tg("49:4:1:0"),cc(Tr.pink,on))
ms.addEvent(tg("50:4:2:0"),cc(Tr.snrd,on))
ms.addEvent(tg("51:4:4:20"),cc(Tr.bd3,on))
ms.addEvent(tg("53:4:1:0"),cc(Tr.pluckb,on))
ms.addEvent(tg("54:3:2:0"),cc(Tr.bd1Stretch,on))

ms.addEvent(tg("55:1:1:1"),ms.togStartStop)
ms.fire(ms.muteAll)
ms.run()  



