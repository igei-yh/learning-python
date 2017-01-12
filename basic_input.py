#!/usr/bin/env python

input_str = raw_input("Input something: ")
print("typed :%s" % input_str)


input_num = input("Input any number: ")
print("typed :%d" % input_num)


input_num = input("Input any natural number: ")
if input_num % 2 == 0:
    print("That's even number. : %d" % input_num)
else:
    print("That's odd number. : %d" % input_num)


num1 = input("Input any natural number : ")
num2 = input("Input more any natural number : ")
if num1 < num2:
    print("fist number is Smaller.")
elif num1 == num2:
    print("each number equal.")
else :
    print("second number is Smaller.")

