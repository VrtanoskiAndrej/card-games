from error_classes import InvalidInputError


class Card(object):

    """
    CARD SKINS:
        * Default:
        * Emoji: ♥️ ♠️ ♦️ ♣️
        * Character: ♥ ♠ ♦ ♣
    """

    def __init__(self, value, suit, skin="default"):
        if skin == "default":
            self.suit = suit

        elif skin == "emoji":
            suit_emojies = {'Hearts': "♥️", 'Spades': "♠️", 'Diamonds': "♦️", 'Clubs': "♣️"}
            self.suit = suit_emojies[suit]

        elif skin == "character":
            suit_characters = {'Hearts': "♥", 'Spades': "♠", 'Diamonds': "️♦", 'Clubs': "♣"}
            self.suit = suit_characters[suit]

        else:
            raise InvalidInputError("Input for 'skin' do not match!")

        self.value = value

    def __str__(self):
        return "({}, {})".format(self.value, self.suit)

    def __repr__(self):
        return "({}, {})".format(self.value, self.suit)

