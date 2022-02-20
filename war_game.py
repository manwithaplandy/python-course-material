"""
Card game of War.

Rules are simple - two players split a deck of cards. Each turn, both players will draw the top card from their deck.
The winner of each round is the player with the highest card value.
If the card values are tied, it kicks off a "war", where both players will place 3 cards face down from
the top of the deck, and show a fourth. Who ever wins based on the value of the fourth card wins all cards placed
on the table that round.
The winner is determined when one player runs out of cards.
"""

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


class Card:

    # A card object contains a suit, a rank, and a points value to determine the winner of each round.

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:

    # A deck is a list of Card objects

    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        # Note this doesn't return anything
        random.shuffle(self.all_cards)

    def deal_one(self):
        # Note we remove one card from the list of all_cards
        return self.all_cards.pop()


class Player:

    # A player has a hand (all_cards), which is a list of Card objects.

    def __init__(self, name):
        self.name = name
        # A new player has no cards
        self.all_cards = []

    def remove_one(self):
        # Remove one card from the deck. all_cards[0] is considered the 'top' of the deck.
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            # use extend method if multiple cards being added
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'


# Game set-up

player_one = Player('One')
player_two = Player('Two')
round_number = 0

main_deck = Deck()
main_deck.shuffle()

for i in range(26):
    player_one.add_cards(main_deck.deal_one())
    player_two.add_cards(main_deck.deal_one())

game_on = True
at_war = False


def check_win():
    global game_on
    if len(player_one.all_cards) == 0:
        game_on = False
        print('Player Two wins!')
    elif len(player_two.all_cards) == 0:
        game_on = False
        print('Player One wins!')


while game_on:

    global game_on
    global at_war
    # Count the number of rounds
    round_number += 1
    print(f'Current round number: {round_number}')

    # Check if a player has lost
    check_win()

    # Start a new round
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_one_cards.append(player_one.remove_one())

    table_cards = [player_two_cards[0], player_one_cards[0]]

    if player_two_cards[0] > player_one_cards[0]:
        player_two.add_cards(table_cards)
    elif player_one_cards[0] > player_two_cards[0]:
        player_one.add_cards(table_cards)
    else:
        at_war = True

    while at_war:
        table_cards.extend([player_one.remove_one(), player_one.remove_one(), player_one.remove_one(), player_two.remove_one(), player_two.remove_one(), player_two.remove_one()])
        player_one_cards = [player_one.remove_one()]
        player_two_cards = [player_two.remove_one()]
        if player_two_cards[0] > player_one_cards[0]:
            player_two.add_cards(table_cards)
            at_war = False
        elif player_one_cards[0] > player_two_cards[0]:
            player_one.add_cards(table_cards)
            at_war = False
        else:
            continue





