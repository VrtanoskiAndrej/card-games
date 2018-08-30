class User(object):
    """
    generates a user class
    """
    def __init__(self, name):
        """
        upon initialization, the user object is given a name and a hand (for holding card objects)
        :param name:
        """
        self.name = name
        self.hand = []

    def __str__(self):
        return "PERSON | name: {} , game: {}".format(self.name, self.game)

    def add_hand(self, ext_cards):
        '''
        the function will add additional cards to the users 'hand'
        :parameter ext_cards:
        '''
        if ext_cards.__class__.__name__ == "list":
            for cards in ext_cards:
                self.hand.append(cards)
        else:
            self.hand.append(ext_cards)

    def get_hand(self):
        return self.hand


