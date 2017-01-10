#!/usr/bin/env python

# generator is repeatable object.
# Generator is used to create iterator.
def lottery1():
    for i in range(6):
        print(i)


lottery1()


# if "yield" is included function becomes a generator. follow it.
def lottery2():
    print("before yield")
    yield 1
    print("yielded 1")
    yield 2
    print("yielded 2")
    yield 3
    print("yielded 3")
# get value of generator using 'next()'.
# next(<generator>) or <generator>.next()
yl = lottery2()
print(yl.next())
print(yl.next())
print(next(yl))

for i in lottery2():
    print(i)


# function which become generator can be used in loop.
def lottery3():
    for i in range(10):
        yield i

for i in lottery3():
    print(i)

