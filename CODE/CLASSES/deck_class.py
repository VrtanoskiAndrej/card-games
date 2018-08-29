from card_class import Card
from random import shuffle


class Deck(object):
    def __init__(self, make_shuffle=False):
        self.cards = []
        self.set_cards()

        if make_shuffle:
            self.shuffle_cards()

    def __iter__(self):
        return iter(self.cards)

    def set_cards(self):
        for suit in ['Hearts', 'Spades', 'Diamonds', 'Cloves']:
            for value in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
                c = Card(value, suit)
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
