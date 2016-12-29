#!/usr/bin/env python

string = "Baby, You can drive my car."

print("lengs of string is %d " % len(string))

print("a appear %d " % string.count('a'))

print("first five string is %s " % string[:5])

print("next five string is %s" % string[5:10])

print("string with odd index are %s " % string[1::2])

print("last five string are %s " % string[-5:])

print("string in uppercase %s " % string.upper())

print("string in lowercase %s " % string.lower())

if string.endswith('car.'):
    print("Yes, I'm gonna be a star!!")

print("split words of string %s " % string.split(" "))

