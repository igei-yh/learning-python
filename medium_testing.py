#!/usr/bin/env python

# test is one way to improve quality.
# Perform operation test with small function unit.
# It is better to join parts that passed test.

# assert can be used to determine bool value.
assert(True)

#assert(False)
# error occurs if argument of assert function is false. follow it.
#   AssertionError


# character output can also be made by test.
assert True, 'Hello'

#assert False, 'World'
#   AssertionError: World


# test with assert. follow it.
assert(5 in range(10))

#assert(11 in range(10))
#
#   File "./testing.py", line 24, in <module>
#   assert(11 in range(10))
#   AssertionError


# testing arguments
def int_print(num):
  assert(type(num) == type(5))
  print(num)

int_print(3)

#int_print("number")
#  File "./testing.py", line 34, in int_print
#  assert(type(num) == type(5))
# AssertionError

