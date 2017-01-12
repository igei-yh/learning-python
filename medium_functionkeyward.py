#!/usr/bin/env python

def keyward(**kwargs):
  for key in ('key1', 'key2', 'key3')
    if key in kwargs:
      print(kwargs)

cred = {
  'key1': 'value1',
  'key2': 'value2',
  'key3': 'value3'
}

keyward(**cred)

