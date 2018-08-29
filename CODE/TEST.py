from card_class import Card
from deck_class import Deck
from user_class import User
from solitataire_class import Solitaire
import time

u = User("carl")
d = Deck(make_shuffle=True)
s = Solitaire(u, d)


s.split_deck(28, 24)
s.setup_tableau()

