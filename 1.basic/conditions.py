#!/usr/bin/env python

# boolean values True and False returned when expression is compared or evaluated. 
x = 1969
print(x == 1969)
print(x == 1996)
print(x < 1970)

# boolean operator
# "and" and "or" boolean operators allow building complex boolean expressions.
name = "paul"
year = 1963
if name == "paul" and year == 1963:
    print("Love me do !!")
if name == "john" or name == "paul":
    print("Misery !!")

# in operator
# check if object exists within container.
name = "john"
member = ["john", "paul", "george", "ringo"]
if name in member:
    print("It's been a hard day's night")

# is operator
# "==" compare values.
# "is" compare is same thing.
list1 = ["john", "paul"]
list2 = ["john", "paul"]
print(list1 == list2)
print(list1 is list2)

# not operator
# not inverts it
print(not False)
print((not False) == (False))

