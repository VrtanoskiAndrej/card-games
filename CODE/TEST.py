from card_class import Card
from deck_class import Deck
from user_class import User
from solitataire_class import Solitaire
from ui_class import UI
import sys



c = Card("A", "Hearts")
us = User("carl")
d = Deck(make_shuffle=True)
s = Solitaire(us, "game_state.json", deck=d)
ui = UI(s)

s.setup_tableau()
ui.show_board()

