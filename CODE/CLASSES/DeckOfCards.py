import random


class Card(object):
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

        print("(Initializing {} of {})".format(self.number, self.suit))

    def __str__(self):
        return "{} of {}".format(self.number, self.suit)


class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()
        print("(Initializing DECK)")

    def build(self):
        for suit in ['Spades', 'Hearts', 'Diamonds', 'Cloves']:
            print(suit.upper())
            for number in range(1, 14):
                self.cards.append(Card(number, suit))

    def show(self):
        for c in self.cards:
            print(c)

    def shuffle(self):
        random.shuffle(self.cards)

    def __str__(self):
        self.show()

    def __len__(self):
        return len(self.cards)


class Person(object):
    def __init__(self):
        self.deck = Deck()
        print("(Initializing PERSON)")

    def show_hand(self, card_amount=4):
        start_point = random.randint(1, len(self.deck)-(card_amount+1))
        print(self.deck[start_point:start_point+card_amount])

    def get_deck(self):
        return self.deck

"""
c = Card("12", "Clubs")
print(c)

d = Deck()
d.show()
"""

p = Person()
p.deck.shuffle()
p.deck.show()
p.show_hand()
