#!/usr/bin/env python

def list_favesong(string1, string2):
    print("'%s' is my fave!" % (string1))
    print("'%s' is too!!" % (string2))

list_favesong("Eleanor Rigby", "For No One")

def truly_faver(string):
    print("%s is truly my fave!!!" % string.upper())

truly_faver("Good Day Sunshine!!")

def shout_faver(string1, string2, string3):
    list_favesong(string1, string2)
    truly_faver(string3)

shout_faver("Michelle", "Nowhere Man!", "Drive My Car!!")

