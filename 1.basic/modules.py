#!/usr/bin/env python

# two functions "dir" and "help" when exploring modules in python. 

import urllib

# function are implemented in each module by using dir function.
dir(urllib)

# read about module more using help function.
help(urllib.urlopen)


import re

find_members = []
for member in dir(re):
    if "find" in member:
        find_members.append(member)

print(sorted(find_members))

