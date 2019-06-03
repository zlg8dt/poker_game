# Zak Gelfond
# computing ID: zlg8dt

import random
from random import shuffle
import sys

num_of_players = input("How many players are you? ")
while int(num_of_players) > 10:
    num_of_players = input("How many players are you? You can only have 10 players: ")



class Cards():
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)

cards = {2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, "J": 11, "Q": 12, "K": 13, "A": 14}
deck = [Cards(value) for value in cards for suit in range(4)]


class Game():


    def __init__(self):
        self.players = {}
    def __repr__(self):
        return str(self.players)

    def dict(self):
        return self.players

    def deal(self, num_of_players):
        global deck
        n_player = 0
        while n_player < num_of_players:
            player = Player()
            player.hand = deck[n_player:5*num_of_players:num_of_players]
            n_player +=1
            self.players[player] = player.hand
            print(player.hand)

    def compare(self):

        for hand in self.players.values():
            high_card = 0
            winner = ""
            for card in hand:
                if card=='J':
                    card = 11
                elif card == 'Q':
                    card = 12
                elif card == 'K':
                    card = 13
                elif card == 'A':
                    card = 14
                if card > high_card:
                    high_card = card
                    winner = hand
            print("This hand wins: "+str(winner))





class Player():
    def __init__(self):
        self.name = input("What is your name? ")
        self.hand = {}

random.shuffle(deck)

game = Game()
game.deal(num_of_players = int(num_of_players))
game.compare()
print(game.dict())
# deck.shuffle()
# first_input = int(sys.argv[1]) #here we use int() to convert the string input into an integer
#
# # now we can use first_input
# print(first_input)
#

# for i in range(int(first_input)):
#     x = input("What is player "+str(i+1)+"'s name? ")
#     players.append(x)
