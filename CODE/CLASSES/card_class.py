from error_classes import InvalidInputError


class Card(object):

    """
    CARD SKINS:
        * Default:
        * Emoji: ♥️ ♠️ ♦️ ♣️
        * Character: ♥ ♠ ♦ ♣
    """

    def __init__(self, value, suit):
        self.suit = suit
        self.value = value

    def __str__(self):
        return "({}, {})".format(self.value, self.suit)

    def __repr__(self):
        return "({}, {})".format(self.value, self.suit)

