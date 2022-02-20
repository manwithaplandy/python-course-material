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


while game_on:

    # Check if a player has lost
    if len(player_one.all_cards) == 0:
        print('Player Two wins!')
        game_on = False
        break

    elif len(player_two.all_cards) == 0:
        print('Player One wins!')
        game_on = False
        break

    # Break edge case where deck arrangement results in infinite loop - shuffle player one's deck every 10,000 rounds
    if round_number % 10000 == 0:
        random.shuffle(player_one.all_cards)

    # Count the number of rounds
    round_number += 1
    totnumcards = len(player_one.all_cards) + len(player_two.all_cards)
    print(f'Current round number: {round_number}')
    print(f'Player 1: {len(player_one.all_cards)} Player 2: {len(player_two.all_cards)}')

    # Start a new round
    player_one_card = player_one.remove_one()

    player_two_card = player_two.remove_one()

    table_cards = [player_two_card, player_one_card]

    if player_two_card.value > player_one_card.value:
        player_two.add_cards(table_cards)
    elif player_one_card.value > player_two_card.value:
        player_one.add_cards(table_cards)
    else:
        print('War!')
        at_war = True

    while at_war:
        if len(player_one.all_cards) > 0 and len(player_two.all_cards) > 0:
            for i in range(min(len(player_one.all_cards)-1, 3)):
                table_cards.append(player_one.remove_one())
            for i in range(min(len(player_two.all_cards)-1, 3)):
                table_cards.append(player_two.remove_one())
        else:
            print("winner found during war")
            break

        if len(player_one.all_cards) > 0 and len(player_two.all_cards) > 0:
            player_one_card = player_one.remove_one()
            player_two_card = player_two.remove_one()
        else:
            print("Winner found during war 2")
            break
        if player_two_card.value > player_one_card.value:
            player_two.add_cards(table_cards)
            player_two.add_cards([player_two_card, player_one_card])
            at_war = False
        elif player_one_card.value > player_two_card.value:
            player_one.add_cards(table_cards)
            player_one.add_cards([player_one_card, player_two_card])
            at_war = False
        else:
            print('another war!')
            print(f'Table cards: {len(table_cards)}')
            continue





