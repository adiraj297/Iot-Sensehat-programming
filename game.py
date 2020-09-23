from sense_hat import SenseHat
import time
import csv
import datetime

#Class imports

from electronicDie import ElectronicDie

class Game:
    p1 = 0
    p2 = 0
    turn = ""

    def __init__(self):
        super().__init__()
        self.p1 = 0
        self.p2 = 0
        self.turn = "1"
    
    #Run the game via this method call
    def runGame(self):
        sense = SenseHat()
        dice = ElectronicDie()
        self.displayInstruction()
        exit = False
        while exit==False:
            for event in sense.stick.get_events():
                # Check for when the jostick is pressed to exit game
                if event.action == "pressed":
                    if event.direction == "down":
                        exit = True
                        sense.show_message("Back to menu")
                        return
            
            #Check if any of the players has won
            if(self.turn == "1"):
                if(self.p2 > 30):
                    self.displayWinner("2", self.p2)
                    exit = True
                    return
                elif(self.p1 > 30):
                    self.displayWinner("1", self.p1)
                    exit = True
                    return
            elif(self.turn == "2"):
                if(self.p1 > 30):
                    self.displayWinner("1", self.p1)
                    exit = True
                    return
                elif(self.p2 > 30):
                    self.displayWinner("2", self.p2)
                    exit = True
                    return

            #Display message for player turn
            msg = "Player {}'s turn".format(self.turn)
            sense.show_message(msg)
            score = dice.gameDie()

            #display player points after shaking
            if(self.turn == "1"):
                self.p1 += score
                sense.show_message("Player {}: {}".format(self.turn, self.p1))
                self.turn = "2"
            else:
                self.p2 += score
                sense.show_message("Player {}: {}".format(self.turn, self.p2))
                self.turn = "1"

    def displayInstruction(self):
        sense = SenseHat()
        sense.show_message("Welcome to the Game")
        sense.show_message("Pass between players and shake. First above 30 wins!")

    #Method call to display and write winner to winner.csv
    def displayWinner(self, player, points):
        sense = SenseHat()
        sense.show_message("Player {} won: {}".format(player, points))
        with open('winner.csv', mode='a') as winner:
            winner_wrt = csv.writer(winner, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            x = datetime.datetime.now()
            row = ["Player {}".format(player), "{}".format(points), "{} {}".format(x.strftime("%x"), x.strftime("%X")) ]
            winner_wrt.writerow(row)
        sense.show_message("Game over")
        sense.show_message("Back to menu")
