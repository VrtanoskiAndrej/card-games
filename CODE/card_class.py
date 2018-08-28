class Card(object):
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return "CARD | {} of {}".format(self.value, self.suit)