#!/usr/bin/env python

x = object()
y = object()

x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contain %d" % len(x_list))
print("y_list contain %d" % len(y_list))
print("big_list contain %d" % len(big_list))

if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("MR.moonlight !!")
if big_list.count(x) == 10 and y_list.count(y) == 10:
    print("Words of Python !!")
