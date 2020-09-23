#IoT Assignment 1 - COSC2755
#Created by:
#   Aditya Raj/Samit Sharma
#   s3730562/s3752136
#   29/03/2020

from sense_hat import SenseHat
import time

class AnimatedEmoji:

    nothing = (0,0,0)
    white = (255, 255, 255)
    yellow = (255, 255, 0)
    orange = (255, 165, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    red = (255, 0, 0)
    purple = (160, 32, 240)
    magenta = (255, 0, 255)
    cyan = (0, 255, 255)
    navy = (0,0, 128)
    images = []

    def __init__(self):
        super().__init__()
        SenseHat().low_light = True
        self.images.append(self.ysmiley())
        self.images.append(self.asmiley())
        self.images.append(self.rsmiley())

    
    def runEmojis(self):
        #print (self.images)
        sense = SenseHat()
        imgs = self.images.copy()
        count = 0
        exit = False;

        while exit==False:
            sense.set_pixels(imgs[count % len(imgs)])
            time.sleep(3)
            count += 1

            for event in sense.stick.get_events():
                # Check for when the jostick is pressed
                if event.action == "pressed":
                    if event.direction == "left":
                        exit = True;
                        sense.show_message("Back to menu")
                        return
    
    def ysmiley(self):
        y = self.yellow 
        g = self.white
        p = self.purple
        display = [
            y, y, y, y, y, y, y, y,
            y, y, y, y, y, y, y, y,
            y, g, g, y, y, g, g, y,
            y, g, g, y, y, g, g, y,
            y, y, y, y, y, y, y, y,
            y, p, p, y, y, p, p, y,
            y, y, y, p, p, y, y, y,
            y, y, y, y, y, y, y, y
        ]
        return display
    
    def asmiley(self):
        r = self.red 
        O = self.orange
        m = self.magenta
        display = [
            r, r, r, r, r, r, r, r,
            r, r, r, r, r, r, r, r,
            r, O, O, r, r, O, O, r,
            r, O, O, r, r, O, O, r,
            r, r, r, r, r, r, r, r,
            r, r, r, m, m, r, r, r,
            r, r, m, r, r, m, r, r,
            r, m, r, r, r, r, m, r
        ]
        return display

    
    def rsmiley(self):
        b = self.blue
        c = self.cyan
        n = self.red

        display = [
            b, b, b, b, b, b, b, b,
            b, b, b, b, b, b, b, b,
            b, c, c, b, b, c, c, b,
            b, c, c, b, b, c, c, b,
            b, b, b, b, b, b, b, b,
            b, b, b, n, n, b, b, b,
            b, n, b, b, b, b, n, b,
            b, b, b, b, b, b, b, b
        ]
        return display