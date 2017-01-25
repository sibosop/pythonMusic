#!/usr/bin/python


def getVal(inVal):
  rval = 0
  if inVal.__class__.__name__ == 'int':
    rval = inVal
  else:
    rval = inVal()
  return rval