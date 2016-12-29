#!/usr/bin/env python

mystring = "Hello"
myfloat = 10.0
myint = 20

if mystring == "Hello":
    print("String is %s" % mystring)

if isinstance(myfloat, float) and myfloat ==10.0:
    print("Float is %f" % myfloat)

if isinstance(myint, int) and myint == 20:
    print("Integer is %d" % myint)
