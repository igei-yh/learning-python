#!/usr/bin/env python

# function is useful code blocks divided.
# follow it.

# in python, function are defined block keyword "def".

def functionA():
    print("Yea! Yea! Yea!")

functionA()

# function also receive arguments.
def functionB(name, title):
    print("%s ! , '%s' is my fave !" % (name, title)) 

functionB("john", "And Your Bird Can Sing")

# function may return value to caller.
def functionC(string1, string2):
    return string1 + string2

shout = functionC("Hey!", "Dudo!!")
print(shout)

