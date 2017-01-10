#!/usr/bin/env python

# in python, string is enclosed ' or ".
# ' ' or " " , whitespace is also one character.
string1 = "revolver is best for me!"
print(len(string1))

print(string1.index('e'))

print(string1.count("s"))

# string or lists object can be sliced.
# [startindex:endindex:skip]
print(string1[5:9])

print(string1[2:10:2])

# revers string doing as follow.
print(string1[::-1])

# capitalize letter or lowercase letters.
print(string1.upper())
print(string1.lower())

# also judge start and end letters
# Points are also distinguished between capital letters and small letters
print(string1.startswith('revolver'))
print(string1.endswith('me!'))
print(string1.startswith('Revol'))

# can also split character strings
print(string1.split(" "))

