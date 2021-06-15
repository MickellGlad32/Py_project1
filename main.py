from gladnessCRIT import Player, Board
import random
import time

board = Board()

player1_name = input("Player1 enter your name: ")
player1 = Player(player1_name)

player2_name = input("Player2 enter your name: ")
player2 = Player(player2_name)

board.add_player(player1)
board.add_player(player2)
board.show()

# Each player rolls the dice, and the higher number gets the first chance to go.
print("Players, roll the dice, and let's see who goes first. ")

time.sleep(1)
player1_first_roll = random.randint(1, 12)
print(player1_first_roll)

print("It would only be fair if we let the other player roll as well.")
print("Next player your turn to roll. ")
player2_first_roll = random.randint(1,12)
print(player2_first_roll)

time.sleep(3)

if player1_first_roll > player2_first_roll:
    print(f"{player1} let's see if you can hold on to this lead. ")
    print(f"{player1} roll again. Don't let them catch your wheel!")
    player1_second_roll = random.randint(1, 12)
    board.move_player(player1, player1_second_roll)
    board.show()
    current_player = player2


else:
    print(f"{player2}, it seems that luck favors you. Let's hope that your legs are up to the challenge.")
    print(f"{player2} roll again and set the pace. ")
    player2_second_roll = random.randint(1, 12)
    board.move_player(player2, player2_second_roll)
    board.show()
    current_player = player1
    
while not board.winner(): 

    time.sleep(2)

    
    print(f"It's {current_player}'\s' turn to roll.")
    dice_roll  = random.randint(1, 12)
    print(dice_roll)
    board.move_player(current_player, dice_roll)
    board.show()
    if current_player == player1:
        current_player = player2
    else:
        current_player = player1

print(f"{board.winner().name} is the winner!!! ")

