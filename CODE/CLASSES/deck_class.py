from card_class import Card
from random import shuffle


class Deck(object):
    def __init__(self, shuffle=False):
        self.cards = []
        self.set_cards()

        if shuffle:
            self.shuffle_cards()

    def set_cards(self):
        for suit in ['Hearts', 'Spades', 'Diamonds', 'Cloves']:
            for value in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
                c = Card(value, suit)
                self.cards.append(c)

    def __str__(self):
        self.show()

    def show(self):
        for card in self.cards:
            print(card)

    def shuffle_cards(self):
        shuffle(self.cards)

    def split_deck(self, *args):
        pass


