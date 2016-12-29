#!/usr/bin/env python

# List is like an array.
# list is included in the type of any variable.
list1 = []
list1.append(1)
list1.append(2)
list1.append(3)
print(list1[0])
print(list1[1])

for x in list1:
    print(x)

# if it does not exist, it becomes exception.
list2 = [1,2,3,4,5]
print(list2[8])
