#IoT Assignment 1 - COSC2755
#Created by:
#   Samit Sharma
#   s3730562
#   01/04/2020

from sense_hat import SenseHat
from random import randint
import time

class ElectronicDie:

    dieFaces = []
    
    def __init__(self):
        super().__init__()
        SenseHat().low_light = True
        self.dieFaces.append(self.die1())
        self.dieFaces.append(self.die2())
        self.dieFaces.append(self.die3())
        self.dieFaces.append(self.die4())
        self.dieFaces.append(self.die5())
        self.dieFaces.append(self.die6())

    #Method call for just using the Dice only
    def runDie(self):
        sense = SenseHat()
        faces = self.dieFaces.copy()
        exit = False
        while exit==False:
            for event in sense.stick.get_events():
                # Check for when the jostick is pressed
                if event.action == "pressed":
                    if event.direction == "right":
                        exit = True;
                        sense.show_message("Back to menu")
                        return
        
            acceleration = sense.get_accelerometer_raw()
            x = acceleration['x']
            y = acceleration['y']
            z = acceleration['z']

            x = abs(x)
            y = abs(y)
            z = abs(z)

            if x > 3 or y > 3 or z > 3:
                opt = randint(1,6)
                sense.set_pixels(faces[opt-1])
                time.sleep(3)
                sense.clear()
            else:
                sense.clear()
                #time.sleep(3)

    #Method call for game.py to use Dice
    def gameDie(self):
        sense = SenseHat()
        faces = self.dieFaces.copy()
        exit = False
        while exit==False:
            acceleration = sense.get_accelerometer_raw()
            x = acceleration['x']
            y = acceleration['y']
            z = acceleration['z']

            x = abs(x)
            y = abs(y)
            z = abs(z)

            if x > 3 or y > 3 or z > 3:
                opt = randint(1,6)
                sense.set_pixels(faces[opt-1])
                time.sleep(3)
                sense.clear()
                exit = True
                return opt
            else:
                sense.clear()
    
    def die1(self):
        w = (255, 255, 255)
        o = (0, 0, 0)
        display = [
            o, o, o, o, o, o, o, o,
            o, o, o, o, o, o, o, o,
            o, o, o, o, o, o, o, o,
            o, o, o, w, w, o, o, o,
            o, o, o, w, w, o, o, o,
            o, o, o, o, o, o, o, o,
            o, o, o, o, o, o, o, o,
            o, o, o, o, o, o, o, o
        ]
        return display

    def die2(self):
        w = (255, 255, 255)
        o = (0, 0, 0)
        display = [
            o, o, o, o, o, o, o, o,
            o, o, o, o, o, w, w, o,
            o, o, o, o, o, w, w, o,
            o, o, o, o, o, o, o, o,
            o, o, o, o, o, o, o, o,
            o, w, w, o, o, o, o, o,
            o, w, w, o, o, o, o, o,
            o, o, o, o, o, o, o, o
        ]
        return display
    
    def die3(self):
        w = (255, 255, 255)
        o = (0, 0, 0)
        display = [
            o, o, o, o, o, o, w, w,
            o, o, o, o, o, o, w, w,
            o, o, o, o, o, o, o, o,
            o, o, o, w, w, o, o, o,
            o, o, o, w, w, o, o, o,
            o, o, o, o, o, o, o, o,
            w, w, o, o, o, o, o, o,
            w, w, o, o, o, o, o, o
        ]
        return display
    def die4(self):
        w = (255, 255, 255)
        o = (0, 0, 0)
        display = [
            o, o, o, o, o, o, o, o,
            o, w, w, o, o, w, w, o,
            o, w, w, o, o, w, w, o,
            o, o, o, o, o, o, o, o,
            o, o, o, o, o, o, o, o,
            o, w, w, o, o, w, w, o,
            o, w, w, o, o, w, w, o,
            o, o, o, o, o, o, o, o
        ]
        return display

    def die5(self):
        w = (255, 255, 255)
        o = (0, 0, 0)
        display = [
            o, w, w, o, o, w, w, o,
            o, w, w, o, o, w, w, o,
            o, o, o, o, o, o, o, o,
            o, o, o, w, w, o, o, o,
            o, o, o, w, w, o, o, o,
            o, o, o, o, o, o, o, o,
            o, w, w, o, o, w, w, o,
            o, w, w, o, o, w, w, o
        ]
        return display

    def die6(self):
        w = (255, 255, 255)
        o = (0, 0, 0)
        display = [
            o, w, w, o, o, w, w, o,
            o, w, w, o, o, w, w, o,
            o, o, o, o, o, o, o, o,
            o, w, w, o, o, w, w, o,
            o, w, w, o, o, w, w, o,
            o, o, o, o, o, o, o, o,
            o, w, w, o, o, w, w, o,
            o, w, w, o, o, w, w, o
        ]
        return display
