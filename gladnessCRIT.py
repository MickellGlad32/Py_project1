# two to four players on the board at a time
# There is a defined number of spaces to complete around the track 
# each player rolls a dice to see who goes first (the highest number goes first)
# the number on the dice determines how many spaces can be moved in a given turn
# If a player lands on an occupied space they bump the other player back two spaces
# whomever reaches the finish line first wins

import random

board = []
players = []

class Place:
    def __init__(self,cyclist_name):
        self.cyclist_name = cyclist_name
        self.position = len(board)

    def show(self):
        on = []
        for p in players:
            if p.position == self.position:
                on.append(p.cyclist_name)
        print(self.cyclist_name + str(on), end = "\t")

class Player:
    def __init__(self):
        self.position = 0
        self.cyclist_name = "P" + str(len(players))
        self.places = []
        players.append(self)

        

