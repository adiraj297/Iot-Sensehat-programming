from sense_hat import SenseHat
import time
import json

class Temperature:
    blue = (0, 0, 255)
    nothing = (0, 0, 0)
    green = (0, 255, 0)
    red = (255, 0 , 0)

    def __init__(self):
        super().__init__()
        with open('config.json', 'r') as f:
            dev = json.load(f)
            self.cold_max = dev['cold_max']
            self.comfortable_min = dev['comfortable_min']
            self.comfortable_max = dev['comfortable_max']
            self.hot_min = dev['hot_min']

    def weather(self):
        self.temp = self.sense.get_temperature()
         
    def cold(self):
        b = self.blue
        o = self.nothing
        self.sense.show_message('Temp: {0:0.1f} *c'.format(self.temp), text_colour = b, back_colour = o, scroll_speed=0.075)
       
        
    def comfortable(self):
        g = self.green
        o = self.nothing
        self.sense.show_message('Temp: {0:0.1f} *c'.format(self.temp), text_colour = g, back_colour = o, scroll_speed=0.075)
        

    def hot(self):
        r = self.red
        o = self.nothing
        self.sense.show_message('Temp: {0:0.1f} *c'.format(self.temp), text_colour = r, back_colour = o, scroll_speed=0.075)
            
    def execute(self):
        self.sense = SenseHat()
        exit = False;
        while exit==False:
            for event in self.sense.stick.get_events():
                # Check for when the jostick is pressed
                if event.action == "pressed":
                    if event.direction == "up":
                        exit = True;
                        self.sense.show_message("Back to menu")
                        return
            
            self.weather()
            if self.temp < self.cold_max:
             self.cold()
            elif self.temp > self.comfortable_min and self.temp <= self.comfortable_max:
             self.comfortable()
            elif self.temp > self.hot_min:
             self.hot()
            time.sleep(10)