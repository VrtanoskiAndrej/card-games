from error_classes import TypeClassError
from deck_class import Deck

""" ♥️ ♠️ ♦️ ♣️ """


class Solitaire(object):
    def __init__(self, user, deck=Deck()):
        """
        upon initialization, the game is provided a user object and a deck object, if it has not received a deck object,
        it will automatically generate one.
        :param user:
        :param deck:
        """
        if user.__class__.__name__ == "User" and deck.__class__.__name__ == "Deck":
            self.user = user
            self.deck = list(deck)

        else:
            raise TypeClassError("CLASS names do not match!, use the User or Deck class")

        self.stock = []
        self.tableau = [[], [], [], [], [], [], []]
        self.foundation = {'Hearts': [], 'Spades': [], 'Diamonds': [], 'Clubs': []}
        self.waste = []
        self._table = {'stock': self.stock, 'tableau': self.tableau, 'foundation': self.foundation, 'waste': self.waste}

    def __str__(self):
        return "TABLE: {}".format(self._table)

    def setup_tableau(self):
        pointer = 0
        for i in range(0, 7):
            for j in range(0, (7 - i)):
                print(self.deck[pointer], end=" ")
                self.tableau[i].append(self.deck[pointer])
                pointer += 1
            print("")

    def move_card(self, from_, to, card):
        if from_ and to in ['stock', 'tableau', 'foundation', 'waste']:
            try:
                pass
            except TypeError:
                pass

    def split_deck(self, *args):
        new_cards, total = [], 0
        for amount in args:
            sub_list = self.deck[total:total + amount]
            new_cards.append(sub_list)
            total += amount
        self.deck = new_cards

    def count_total_cards(self):
        total = 0
        total += len(self.stock) + len(self.waste)    # CARDS in stock pile
        for pile in self.tableau:
            total += len(pile)  # CARDS in tableau
        for key in ['Hearts', 'Spades', 'Diamonds', 'Clubs']:
            total += len(self.foundation[key])   # CARDS in the foundation

        return total


