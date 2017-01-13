#!/usr/bin/env python

input_num = input("Input number of values: ")
output_num = 0
counter = 0


while counter < input_num:
    counter += 1
    output_num += input("Input value #%d: " % counter)

print("sum of value is : %d" % output_num)

