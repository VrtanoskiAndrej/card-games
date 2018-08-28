from deck_class import Deck
from random import randint


class Person(object):
    def __init__(self, name):
        self.name = name
        self.deck = Deck()
        print("(Initializing PERSON)")

    def show_hand(self, card_amount=4):
        start_point = randint(1, len(self.deck)-(card_amount+1))
        print(self.deck[start_point:start_point+card_amount])

    def get_deck(self):
        return self.deck


p = Person("JOHN")
p.deck.show_all_cards()
