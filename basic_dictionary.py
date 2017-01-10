#!/usr/bin/env python

# dictionary is data types which has key and value of index.
# each value stored in dictionary can be accessed using key.

bookmark = {}
bookmark["please please me"] = 1963
bookmark["a hard days night"] = 1964
bookmark["rover soul"] = 1965
bookmark["revolver"] = 1966
bookmark["Sgt. pepper's lonly hearts club band"] = 1967
bookmark["the beatles"] = 1968
bookmark["abbey road"] = 1969
bookmark["let it be"] = 1970

print(bookmark)

for album, year in bookmark.items():
    print("%s is released in %d" % (album, year))

# to remove specified index, following.
for key, value in bookmark.items():
    del bookmark[key]

print(bookmark)

bookmark["please please me"] = 1963
bookmark["a hard days night"] = 1964
bookmark["rover soul"] = 1965
bookmark["revolver"] = 1966
bookmark["Sgt. pepper's lonly hearts club band"] = 1967
bookmark["the beatles"] = 1968
bookmark["abbey road"] = 1969
bookmark["let it be"] = 1970

for key, value in bookmark.items():
    bookmark.pop(key)

print(bookmark)

