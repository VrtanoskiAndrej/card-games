from card_class import Card
from random import shuffle


class Deck(object):
    def __init__(self, is_shuffled=False):
        self.cards = []
        self.set_cards()

        if is_shuffled:
            self.shuffle_cards()

    def set_cards(self):
        for suit in ['Hearts', 'Spades', 'Diamonds', 'Cloves']:
            for value in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
                c = Card(value, suit)
                self.cards.append(c)

    def __str__(self):
        self.show_all_cards()

    def show_all_cards(self):
        for card in self.cards:
            print(card)

    def shuffle_cards(self):
        shuffle(self.cards)


