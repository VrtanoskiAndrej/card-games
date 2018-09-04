import tkinter

class UI(object):
    def __init__(self, game):
        self.game = game



    # TODO: improve template design and fix create_graphic_deck function + create exceptions for the number 10!!!

    def create_graphic_deck(self):
        graphical_deck = []
        for card in self.cards:
            graphical_deck.append(self.gen_card(card.value, card.suit))
            print(self.gen_card(card.value, card.suit))
        return graphical_deck

    def gen_card(self, value, suit):
        spades_template = """
    .------.      
    |{}.--. |
    |  /\  |
    | (__) |
    | '--'{}| 
    `------' """
        hearts_template = """
    .------.
    |{}.--. |
    | (\/) |
    |  \/  |
    | '--'{}|
    `------'"""
        clubs_template = """

    .------.
    |{}.--. |
    |  ()  |
    | ()() |
    | '--'{}|
    `------'"""
        diamonds_template = """
    .------.
    |{}.--. |
    |  /\  |
    |  \/  |
    | '--'{}|
    `------'"""

        if suit == "Spades":
            return spades_template.format(value, value)

        elif suit == "Hearts":
            return hearts_template.format(value, value)

        elif suit == "Clubs":
            return clubs_template.format(value, value)

        elif suit == "Diamonds":
            return diamonds_template.format(value, value)

        else:
            return "ERROR"

