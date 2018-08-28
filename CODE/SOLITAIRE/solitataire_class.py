from error_classes import TypeClassError


class Solitaire(object):
    def __init__(self, user, deck):
        if user.__class__.__name__ == "User" and deck.__class__.__name__ == "Deck":
            self.user = user
            self.deck = deck
        else:
            raise TypeClassError("CLASS names do not match!, use the User or Deck class")

        self.stock = []
        self.tableau = [[], [], [], [], [], [], []]
        self.foundation = {'Hearts': [], 'Spades': [], 'Diamonds': [], 'Cloves': []}
        self.waste = []

    def setup_tableau(self):
        for i in range(0, 7):
            for j in range(0, (7 - i)):
                print(" * ")
            print("PAUSE")
