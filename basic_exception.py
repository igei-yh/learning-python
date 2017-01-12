#!/usr/bin/env python

# Exception are inherent in programs.
# In python, exception handling can be written as...
try:
    print(5/0)
except:
    print("ZeroDivisionError Occurred !!")


try:
    print(6/2)
except:
    print("ZeroDivisionError Occurred !!")


# 'Exception' is a class for exception handling.
# Exception has various inherited classes.

try:
    print(5/0)
except Exception:
    print("ZeroDivisionError Occurred !!")

# write multiple Exception.
try:
    f = open('helloworld.txt', 'r')
except IOError:
    print("IO Error is Occurred !!")
except Exception:
    print("Something Happen !!")

# try/except/else
# else will be exec if there are no exceptions.
# finally is handled with or without exception.

try:
    f = open('helloworld.txt', 'r')
    for line in f:
        print(line)
except:
    print("Something Happen !!")
else:
    print("No Error !!")
finally:
#    f.close()
    print("Sound Goods !!")

# capture errors
# exception can be stored in variables.
try:
    5/0
except Exception, e: # also write like this 'except Exception as e:'
    print(type(e))
    print(e)

