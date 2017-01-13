#!/usr/bin/env python

# classes are essentially template to create your objects.
# class has data. class has function.
# class resembles structure.
# class is model. it like a design drawing of object.
class Composition:
    def __init__(self):
        self.record = ""
        self.name = ""

    def singer(self):
        print("%s is my fave one!!" % self.record)
        if self.name == "john":
            print("%s sing 'Im only sleepin', 'She said She said', "
                "'And your Bird can sing' and 'Tommorow Never Knows'" % self.name)
        elif self.name == "paul":
            print("%s sing 'Eleanor gigby', 'Here, There and everywhere', "
                "'Yellow Submarine', 'Good day sunshine', 'For no one', "
                "'Doctor robert' and 'Got to Get You into my life'" % self.name)
        elif self.name == "george":
            print("%s sing 'Taxman', 'Love You to' and 'I want to tell you'" % self.name)
        elif self.name == "ringo":
            print("%s sing 'Yellow Submarine'" % self.name)

# instantiate to use class.
# to create an instance, like this 'instance = <classname>() '
new = Composition()
new.record = "revolver"
new.name = "john"
new.singer()
new.name = "paul"
new.singer()
new.name = "george"
new.singer()
new.name = "ringo"
new.singer()

# '__init__' is special method.
# '__init__' method called when instance is created, it called constructor.
class Printer(object):
    def __init__(self):
        self.name = ""
        self.description = ""
        print("instance initialized !!")

new = Printer()

# def __init__(self): 'self'. what is ?

class selfer(object):
    def __init__(self):
        print("selfs type is " + str(type(self)))
        print("selfs ref is " + str(self))

new = selfer()

