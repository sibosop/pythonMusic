#!/usr/bin/python
import mido
from EvUtil import getVal
from Note import Note



class SpeakIt(object):
  Full=['effl','emfl','fffl','hffl']
  Forced=['eff','emf','hff']
  Meaningless=['efm','emm','hfm']
  Statements=['efs','ems','ffs','hfs']
  PhraseTable=(Full[0],Forced[0],Meaningless[0],Statements[0],Full[1],Forced[1],Meaningless[1],Statements[1],Full[2],Statements[2],Full[3],Forced[2],Meaningless[2],Statements[3])
  NoteOffset=60
  PanOffset=100
  EffectCC = 119
  EffectChan = 0
  DefaultLen=5
  PanChan=0
  
  def __init__(self,phrase='effl',vel=100,chan=5,pan=63,effect=0):
    self.vel = vel
    self.phrase = phrase
    self.chan = chan
    self.pan= pan
    self.effect = effect
    
  def fire(self,ms):
    playPhrase = SpeakIt.PhraseTable.index(getVal(self.phrase)) + SpeakIt.NoteOffset
    playVel = getVal(self.vel)
    playChan = getVal(self.chan)
    playPan = getVal(self.pan)
    playEffect = getVal(self.effect)
    panCC = (playPhrase-SpeakIt.NoteOffset)+SpeakIt.PanOffset
    print "Speakit Fire:"+str(playPhrase)
    msg=mido.Message('control_change',value=playPan,control=panCC,channel=SpeakIt.PanChan)
    print "Fire message:"+str(msg)
    ms.midiOut.send(msg)
    print "playEffect:"+str(playEffect)
    msg=mido.Message('control_change',value=playEffect,control=SpeakIt.EffectCC,channel=SpeakIt.EffectChan)
    print "Fire message:"+str(msg)
    ms.midiOut.send(msg)
    msg=mido.Message('note_on',note=playPhrase,velocity=playVel,channel=playChan)
    #print 'count:'+str(ms.count)+' '+str(msg)+' '
    ms.midiOut.send(msg)
    if playVel != 0:
      off=ms.count+SpeakIt.DefaultLen
      ms.addEvent(off,Note(note=playPhrase,vel=0,len=0,chan=playChan))
    