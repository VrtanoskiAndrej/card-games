from error_classes import TypeClassError


class Solitaire(object):
    def __init__(self, user, deck):
        if user.__class__.__name__ == "User" and deck.__class__.__name__ == "Deck":
            self.user = user
            self.deck = list(deck)
        else:
            raise TypeClassError("CLASS names do not match!, use the User or Deck class")

        self.stock = []
        self.tableau = [[], [], [], [], [], [], []]
        self.foundation = {'Hearts': [], 'Spades': [], 'Diamonds': [], 'Cloves': []}
        self.waste = []

    def setup_tableau(self):
        pointer = 0
        for i in range(0, 7):
            for j in range(0, (7 - i)):
                print(self.deck[0][pointer], end=" ")
                pointer += 1
            print("PAUSE")

    def split_deck(self, *args):
        new_cards, total = [], 0
        for amount in args:
            sub_list = self.deck[total:total+amount]
            new_cards.append(sub_list)
            total += amount
        self.deck = new_cards
