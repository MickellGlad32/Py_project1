# two to four players on the board at a time
# There is a defined number of spaces to complete around the track 
# each player rolls a dice to see who goes first (the highest number goes first)
# the number on the dice determines how many spaces can be moved in a given turn
# If a player lands on an occupied space they bump the other player back two spaces
# whomever reaches the finish line first wins

import random

class Board:
    def __init__(self):
        self.places = []
        count = 1
        self.players = []
        while len(self.places) < 20:
            self.places.append(Place(count))
            count += 1

    def winner(self):
        if self.places[-1].player != None:
            return self.places[-1].player
        else:
            return False

    def show(self):
        print('Current cyclist position. ')
        for player in self.players:
            player_on_board = False

            for place in self.places:
                if place.player == player:
                    print(f"{place.player.name} is on position {place.position}")

                    player_on_board = True

            if not player_on_board:
                print(f"{player.name} is not on the board yet.")
            
        

    def add_player(self, player):
        self.players.append(player)
        

    def move_player(self, player, distance):
        current_position = 0
        index = 0
        for place in self.places:
            if place.player == player:
                current_position = index

            index += 1
        new_position = current_position + distance
        if new_position >= len(self.places) -1:
            new_position = len(self.places) -1
        if self.places[new_position].player != None:
            pass
        else:
            self.places[current_position].remove_player()
            self.places[new_position].add_player(player)


class Place:
    def __init__(self, position=0):
        self.position = position
        self.player = None

    def add_player(self, player):
        self.player = player
        

    def remove_player(self):
        self.player = None

class Player:
    def __init__(self,name):
        self.position = 0
        self.name = name
        self.places = []
        
        print(f"Welcome to Crit Racing {name}")

    def __str__(self):
        return self.name
        

    def turn(self, player):
       while player is True:
        print(f"It's {player}'\s' turn to roll.")
        dice_roll  = random.randint(1, 12)
        print(dice_roll)
        board.move_player(player1, dice_roll)
        board.show()
        roll += 1


        print(f"It's {self.name} Turn to go")
        print("2) Roll Dice")

        choice = input(": ")
        print(choice)

        if int(choice) == 1:
            for player in self.places:
                print(f"You have landed on {player.name}")

                
            

