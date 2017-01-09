#!/usr/bin/env python

# Classes are essentially template to create your objects.

class Composition:
    record = "revolver"
    name = "john"

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

