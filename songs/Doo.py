#!/usr/bin/python

from MidiScheduler import MidiScheduler 
from Measure import Measure as Me
from Loop import Loop as Lo
from Event import CCEvent as cc, EventList as el
import sys

ms = MidiScheduler('IAC Driver IAC Bus 1')
off = ms.off
on = ms.on

class Tr(object):
  unused,bd3,snrd,midd,pink,bd1,clp,pluckb,tink,bd1Stretch,revBd3,pluckwah,bell,pluckbell,pluckbell1,pluckbell2,pluckbell3,beattone1,beattone2=range(19)
  
revSound=el([[Lo("1:1:1:0"),cc(Tr.revBd3,off)],[Lo("2:1:1:0"),cc(Tr.revBd3,on)]])

pluckWah=el([[Lo("1:4:1:0"),cc(Tr.pluckwah,off)],
  [Lo("2:1:1:0"),cc(Tr.bell,off)],
  [Lo("3:1:1:0"),cc(Tr.bell,on)],
  [Lo("4:1:1:0"),cc(Tr.bell,off)],
  [Lo("5:1:1:0"),cc(Tr.bell,on)],
  [Lo("5:4:1:0"),cc(Tr.pluckwah,on)]])
  
beattone=el([[Lo("1:4:1:0"),cc(Tr.beattone1,off)],
  [Lo("3:4:1:0"),cc(Tr.beattone1,on)],
  [Lo("3:4:1:0"),cc(Tr.beattone2,off)],
  [Lo("4:4:1:0"),cc(Tr.beattone2,on)],
  [Lo("4:4:1:0"),cc(Tr.beattone1,off)],
  [Lo("5:4:1:0"),cc(Tr.beattone1,on)]])

pluckbell=el([[Lo("1:4:1:0"),cc(Tr.pluckbell,off)],
  [Lo("2:1:1:0"),cc(Tr.pluckbell1,off)],
  [Lo("3:1:1:0"),cc(Tr.pluckbell1,on)],
  [Lo("3:1:1:0"),cc(Tr.pluckbell2,off)],
  [Lo("4:1:1:0"),cc(Tr.pluckbell2,on)],
  [Lo("4:1:1:0"),cc(Tr.pluckbell1,off)],
  [Lo("5:1:1:0"),cc(Tr.pluckbell1,on)],
  [Lo("5:1:1:0"),cc(Tr.pluckbell3,off)],
  [Lo("5:4:1:0"),cc(Tr.pluckbell,on)],
  [Lo("6:1:1:0"),cc(Tr.pluckbell3,on)]])


ms.addEvent(Lo("1:4:1:0"),cc(Tr.pink,off))

ms.addEvent(Lo("3:1:1:0"),cc(Tr.bd1Stretch,off))

ms.addEvent(Lo("5:1:1:0"),revSound)
ms.addEvent(Lo("5:4:1:0"),cc(Tr.pluckb,off))

ms.addEvent(Lo("7:4:1:0"),cc(Tr.bd1,off))
ms.addEvent(Lo("8:1:1:0"),cc(Tr.clp,off))
ms.addEvent(Lo("9:1:1:0"),revSound)
ms.addEvent(Lo("9:4:3:0"),cc(Tr.snrd,off))

ms.addEvent(Lo("10:4:4:20"),cc(Tr.bd3,off))

ms.addEvent(Lo("12:1:1:0"),cc(Tr.tink,off))

ms.addEvent(Lo("13:1:1:0"),revSound)
ms.addEvent(Lo("13:1:1:0"),pluckWah)


ms.addEvent(Lo("20:1:1:0"),revSound)
ms.addEvent(Lo("20:1:1:9"),pluckbell)


ms.addEvent(Lo("25:1:1:0"),revSound)
ms.addEvent(Lo("25:1:1:0"),pluckWah)

ms.addEvent(Lo("31:1:1:0"),beattone)


ms.addEvent(Lo("38:1:1:0"),pluckWah)
ms.addEvent(Lo("38:1:1:0"),beattone)


ms.addEvent(Lo("45:4:1:0"),cc(Tr.bd1,on))
ms.addEvent(Lo("46:1:1:0"),cc(Tr.clp,on))
ms.addEvent(Lo("47:4:4:20"),cc(Tr.tink,on))
ms.addEvent(Lo("49:4:1:0"),cc(Tr.pink,on))
ms.addEvent(Lo("50:4:2:0"),cc(Tr.snrd,on))
ms.addEvent(Lo("51:4:4:20"),cc(Tr.bd3,on))
ms.addEvent(Lo("53:4:1:0"),cc(Tr.pluckb,on))
ms.addEvent(Lo("54:3:2:0"),cc(Tr.bd1Stretch,on))

ms.addEvent(Lo("55:1:1:1"),ms.togStartStop)

ms.run()  



