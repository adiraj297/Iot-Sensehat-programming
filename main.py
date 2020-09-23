#IoT Assignment 1 - COSC2755
#Created by:
#   Samit Sharma
#   s3752136
#   01/04/2020

#Sense Hat imports
from sense_hat import SenseHat
from time import sleep

#Class imports

from animatedEmoji import AnimatedEmoji
from monitorAndDisplay import Temperature
from electronicDie import ElectronicDie
from game import Game

class Main:

    @staticmethod
    def main():
        sense = SenseHat()
        option = "1"
        sense.clear()
        task1 = AnimatedEmoji()
        task2 = Temperature()
        task3a = ElectronicDie()
        task3b = Game()
        exit = False
        sense.show_message("Menu - Use Joystick")
        sense.show_message("Exit - Hold down joystick")
        while exit==False:
            for event in sense.stick.get_events():
                # Check for when the jostick is pressed
                if event.action == "held":
                    if event.direction == "down":
                        sense.show_message("Exiting system")
                        exit = True
                        return
                
                if event.action == "pressed":
                    sense.clear()
                    # Check the button direction
                    # 1. Left for Task 1
                    if event.direction == "left":
                        option = "1"
                        sense.show_message("1. Emoji")
                    # 2. Up for Task 2
                    elif event.direction == "up":
                        option = "2"
                        sense.show_message("2. Temp")
                    # 3. Right for Task 3.A
                    elif event.direction == "right":
                        option = "3" 
                        sense.show_message("3. Dice")
                    # 4. Down for Task 3.B
                    elif event.direction == "down":
                        option = "4"
                        sense.show_message("4. Game")
                    # Select for the option
                    elif event.direction == "middle":
                        sense.show_letter(option)
                        if option == "1":
                            task1.runEmojis()
                        elif option == "2":
                            task2.execute()
                        elif option == "3":
                            task3a.runDie()
                        elif option == "4":
                            task3b.runGame()
                # Wait a while and then clear the screen
                sleep(0.5)
                sense.clear()

Main.main()