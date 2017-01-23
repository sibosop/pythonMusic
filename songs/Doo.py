#!/usr/bin/python

from MidiScheduler import MidiScheduler, Measure as Me, Loop as Lo
from Event import CCEvent as cc
import sys
MidiScheduler.loopSize=4
MidiScheduler.measureSize=96
ms = MidiScheduler('IAC Driver IAC Bus 1')
off = ms.off
on = ms.on

class Tr(object):
  unused,bd3,snrd,midd,pink,bd1,clp,pluckb,tink,bd1Stretch,revBd3,pluckwah,bell,pluckbell,pluckbell1,pluckbell2,pluckbell3,beattone1,beattone2=range(19)
  


ms.addEvent(Lo("1:4:1:0"),cc(Tr.pink,off))
ms.addEvent(Lo("3:1:1:0"),cc(Tr.bd1Stretch,off))
ms.addEvent(Lo("5:1:1:0"),cc(Tr.revBd3,off))
ms.addEvent(Lo("5:4:1:0"),cc(Tr.pluckb,off))
ms.addEvent(Lo("6:1:1:0"),cc(Tr.revBd3,on))
ms.addEvent(Lo("7:4:1:0"),cc(Tr.bd1,off))
ms.addEvent(Lo("8:1:1:0"),cc(Tr.clp,off))
ms.addEvent(Lo("9:1:1:0"),cc(Tr.revBd3,off))
ms.addEvent(Lo("9:4:3:0"),cc(Tr.snrd,off))
ms.addEvent(Lo("10:1:1:0"),cc(Tr.revBd3,on))
ms.addEvent(Lo("11:1:1:0"),cc(Tr.bd3,off))
ms.addEvent(Lo("12:1:1:0"),cc(Tr.tink,off))
ms.addEvent(Lo("13:1:1:0"),cc(Tr.revBd3,off))
ms.addEvent(Lo("13:4:1:0"),cc(Tr.pluckwah,off))
ms.addEvent(Lo("14:1:1:0"),cc(Tr.revBd3,on))
ms.addEvent(Lo("14:1:1:0"),cc(Tr.bell,off))
ms.addEvent(Lo("15:1:1:0"),cc(Tr.bell,on))
ms.addEvent(Lo("16:1:1:0"),cc(Tr.bell,off))
ms.addEvent(Lo("17:1:1:0"),cc(Tr.bell,on))
ms.addEvent(Lo("17:4:1:0"),cc(Tr.pluckwah,on))

ms.addEvent(Lo("20:1:1:0"),cc(Tr.revBd3,off))
ms.addEvent(Lo("20:4:1:0"),cc(Tr.pluckbell,off))
ms.addEvent(Lo("21:1:1:0"),cc(Tr.revBd3,on))
ms.addEvent(Lo("21:1:1:0"),cc(Tr.pluckbell1,off))
ms.addEvent(Lo("22:1:1:0"),cc(Tr.pluckbell1,on))
ms.addEvent(Lo("22:1:1:0"),cc(Tr.pluckbell2,off))
ms.addEvent(Lo("23:1:1:0"),cc(Tr.pluckbell2,on))
ms.addEvent(Lo("23:1:1:0"),cc(Tr.pluckbell1,off))
ms.addEvent(Lo("24:1:1:0"),cc(Tr.pluckbell1,on))
ms.addEvent(Lo("24:1:1:0"),cc(Tr.pluckbell3,off))
ms.addEvent(Lo("24:4:1:0"),cc(Tr.pluckbell,on))
ms.addEvent(Lo("25:1:1:0"),cc(Tr.pluckbell3,on))

ms.addEvent(Lo("25:1:1:0"),cc(Tr.revBd3,off))
ms.addEvent(Lo("25:4:1:0"),cc(Tr.pluckwah,off))
ms.addEvent(Lo("26:1:1:0"),cc(Tr.revBd3,on))
ms.addEvent(Lo("26:1:1:0"),cc(Tr.bell,off))
ms.addEvent(Lo("27:1:1:0"),cc(Tr.bell,on))
ms.addEvent(Lo("28:1:1:0"),cc(Tr.bell,off))
ms.addEvent(Lo("29:1:1:0"),cc(Tr.bell,on))
ms.addEvent(Lo("29:4:1:0"),cc(Tr.pluckwah,on))
ms.addEvent(Lo("31:4:1:0"),cc(Tr.beattone1,off))
ms.addEvent(Lo("32:1:1:0"),cc(Tr.bell,off))
ms.addEvent(Lo("33:4:1:0"),cc(Tr.beattone1,on))
ms.addEvent(Lo("33:4:1:0"),cc(Tr.beattone2,off))
ms.addEvent(Lo("34:4:1:0"),cc(Tr.beattone2,on))
ms.addEvent(Lo("34:4:1:0"),cc(Tr.beattone1,off))
ms.addEvent(Lo("35:4:1:0"),cc(Tr.beattone1,on))

ms.addEvent(Lo("38:4:1:0"),cc(Tr.pluckwah,off))
ms.addEvent(Lo("38:4:1:0"),cc(Tr.beattone1,off))
ms.addEvent(Lo("40:4:1:0"),cc(Tr.beattone1,on))
ms.addEvent(Lo("40:4:1:0"),cc(Tr.beattone2,off))
ms.addEvent(Lo("41:4:1:0"),cc(Tr.beattone2,on))
ms.addEvent(Lo("41:4:1:0"),cc(Tr.beattone1,off))
ms.addEvent(Lo("42:4:1:0"),cc(Tr.beattone1,on))
ms.addEvent(Lo("42:4:1:0"),cc(Tr.pluckwah,on))

ms.addEvent(Lo("44:1:1:0"),cc(Tr.bell,on))
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



