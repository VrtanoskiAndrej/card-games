from deck_class import Deck
from user_class import User
from parse import JParser
import json


""" ♥️ ♠️ ♦️ ♣️ """


class Solitaire(object):
    def __init__(self, user, game_state, deck=Deck(make_shuffle=True)):
        """
        upon initialization, the game is provided a user object and a deck object, if it has not received a deck object,
        it will automatically generate one.
        :param user:
        :param deck:
        """
        if isinstance(user, User) and isinstance(deck, Deck):
            self.user = user
            self.deck = list(deck)
            print(self.deck)

        else:
            raise TypeError("CLASS names do not match!, use the User or Deck class")

        self.json_file = game_state
        self.stock = []
        self.tableau = [[], [], [], [], [], [], []]
        self.foundation = {'Hearts': [], 'Spades': [], 'Diamonds': [], 'Clubs': []}
        self.waste = []
        self._table = {'stock': self.stock, 'tableau': self.tableau, 'foundation': self.foundation, 'waste': self.waste}
        self.load_template()
        self.jparse = JParser(game_state)

    def __str__(self):
        return "TABLE: {}".format(self._table)

    def setup_tableau(self):
        pointer = 0
        for i in range(0, 7):
            for j in range(i, 7):
                self.tableau[j].append(self.deck[pointer])
                self.jparse.insert("tableau.{}".format(j), self.deck[pointer])
                pointer += 1
        for card in self.deck[pointer:]:
            self.jparse.insert("stock".format(pointer), card)

    def count_total_cards(self):
        total = 0
        total += len(self.stock) + len(self.waste)    # CARDS in stock pile
        for pile in self.tableau:
            total += len(pile)  # CARDS in tableau
        for key in ['Hearts', 'Spades', 'Diamonds', 'Clubs']:
            total += len(self.foundation[key])   # CARDS in the foundation

        return total

    def load_template(self):
        template = {"stock": [], "tableau": [[], [], [], [], [], [], []],
                    "foundation": {"Hearts": [], "Spades": [], "Diamonds": [], "Clubs": []}, "waste": []}
        j = json.dumps(template, indent=4)
        f = open(self.json_file, 'w')
        print(j, file=f)
        f.close()

    def move_card(self, _from, to):
        pass
