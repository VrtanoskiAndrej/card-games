class User(object):
    def __init__(self, name, game):
        self.name = name
        self.game = game
        self.hand = []

    def __str__(self):
        return "PERSON | name: {} , game: {}".format(self.name, self.game)

    def add_hand(self, ext_cards):
        ''' :parameter ext_cards: MUST BE A LIST '''
        for cards in ext_cards:
            self.hand.append(cards)

    def get_hand(self):
        return self.hand


