#!/usr/bin/python
import mido
mido.set_backend('mido.backends.rtmidi')
with mido.open_input('IAC Driver IAC Bus 1') as input:
  for msg in input:
    print(msg)
