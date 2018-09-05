from solitataire_class import Solitaire


class UI(object):
    def __init__(self, game):
        assert isinstance(game, Solitaire)
        self.game = game

    # TODO: improve template design and fix create_graphic_deck function + create exceptions for the number 10!!!

    def show_board(self, card_width=20):
        for i in range(0, 7):
            print(" " * card_width * i, end="")
            for j in range(i, 7):
                print(self.pad(20, self.game.tableau[j][i]), end="")
            print("")

    def pad(self, length, text):
        new_text = ""
        extra = length - len(text)

        if extra % 2 == 0:
            return "{}{}{}".format(int(extra / 2) * " ", text, int(extra / 2) * " ")
        else:
            return "{}{}{}".format((extra // 2 + 1) * " ", text, (extra // 2) * " ")


