#!/usr/bin/env python

# object?
# instance is generated from class.
# however, object can not explained enough by its meaning.
# object is like follow it.
# role each plays is clealy decided.
# cooperate objects to create whole image.

import time


class Car:
    def __init__(self):
        self.handle = Handle()
        print("ride in car !!")
        self.record = DriveRecorder()

    def turn_to_right(self):
        result = self.handle.right()
        print(result)
        time.sleep(5)
        self.record.write_drive_log(result)

    def turn_to_left(self):
        result = self.handle.left()
        print(result)
        time.sleep(5)
        self.record.write_drive_log(result)

    def check_record(self):
        print(self.record.get_log())


class Handle:
    def right(self):
        return "turned right !!"

    def left(self):
        return "turned left !!"


class DriveRecorder:
    def __init__(self):
        self.log = []

    def write_drive_log(self, text):
        self.log.append(time.ctime() + ':' + text)

    def get_log(self):
        return '\n'.join(self.log)


drive_my_car = Car()
drive_my_car.turn_to_right()
drive_my_car.check_record()
drive_my_car.turn_to_left()
drive_my_car.check_record()


