from card_class import Card
from random import shuffle

"""
SUITS:
    * Hearts: ♥️     
    * Spades: ♠️
    * Diamonds: ♦️
    * Clubs: ♣️
"""


class Deck(object):
    def __init__(self, make_shuffle=True, card_skin="default"):
        self.cards = []
        self.set_cards(card_skin)

        if make_shuffle:
            self.shuffle_cards()

    def __iter__(self):
        return iter(self.cards)

    def set_cards(self, card_skin):
        for suit in ['Hearts', 'Spades', 'Diamonds', 'Clubs']:
            for value in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
                c = Card(value, suit, skin=card_skin)
                self.cards.append(c)

    def __str__(self):
        return "CARDS: {}".format(self.cards)

    def __repr__(self):
        return "CARDS: {}".format(self.cards)

    def show(self):
        all_cards = []
        for card in self.cards:
            all_cards.append(card)
        return all_cards

    def shuffle_cards(self):
        shuffle(self.cards)

# TODO: improve template design and fix create_graphic_deck function + create exceptions for the number 10!!!

    def create_graphic_deck(self):
        graphical_deck = []
        for card in self.cards:
            graphical_deck.append(self.gen_card(card.value, card.suit))
        return graphical_deck

    @staticmethod
    def gen_card(value, suit):
        template = "/------\ \n| {}{}  |\n|      |\n|      |\n|  {}{} |\n\------/".format(value, suit, suit, value)
        return template

