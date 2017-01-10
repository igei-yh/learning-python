#!/usr/bin/env python

# two loop types , in python.
# for loop iterate given sequence.
sequence1 = [1, 2, 3, 4, 5]
for seq in sequence1:
    print(seq)

sequence2 = ["john", "paul", "george", "ringo"]
for seq in sequence2:
    print(seq)

# iterate using "range" and "xrange" function.
for x in range(10):
    print(x)

for x in xrange(10):
    print(x)

# range function return created list.
# xrange function return list object. it's memory saving!
print(range(3))
print(xrange(3))

# while lpop repeat as long as certain boolean condition is met.
count = 1960
while count < 1970:
    print("i still can recall")
    count += 1

# break is used to exit loop.
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

for x in xrange(10):
    if x % 2 == 0:
        continue
    print(x)

# when loop condition fails else is executed.
count=0
while(count<5):
    print(count)
    count += 1
else:
    print("Shakin' in the Sixties!!")

for i in xrange(1, 10):
    if (i%5==0):
        break
    print(i)
else:
    print("Jazz Piano Song!")

