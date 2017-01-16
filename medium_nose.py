#!/usr/bin/env python

def add(num1, num2):
    if num1 is None:
        raise RuntimeError('Argument is missing !!')

    return num1 + num2


from nose.tools import with_setup, raises

# user assert to evaluate execution result of function.
def test_add_nums():
    actual = add(1, 10)
    assert actual == 11

'''
# function to execute before test.
def setup_func():
    pass

# function to execute after test.
def teardown_func():
    pass

@with_setup(setup_func, teardown_func)
def test_addNumbers():
    actual = add(-1, 1)
    assert actual == 0

@raises(RuntimeError)
def test_invalid_arg1():
    actual = add(None, 1)
'''
