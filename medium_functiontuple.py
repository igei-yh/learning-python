#!/usr/bin/env python

import random


def get_min_max(a):
    mi = a[0]
    mx = a[0]
    for i in a:
        if i < mi:
            mi = i
        if i > mx:
            mx = i
    return (mi, mx)


a = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(a)
print("random num :" + str(a))
(mi, mx) = get_min_max(a)
print("min num :" + str(mi))
print("max num :" + str(mx))
