#!/usr/bin/python
import mido
import sys
import time

mido.set_backend('mido.backends.rtmidi')
out= mido.open_output('IAC Driver IAC Bus 1') 
msg=mido.Message('note_on',note=int(sys.argv[1]),velocity=int(sys.argv[2]))
print msg
out.send(msg)
time.sleep(1)
msg=mido.Message('note_on',note=int(sys.argv[1]),velocity=0)
print msg
out.send(msg)