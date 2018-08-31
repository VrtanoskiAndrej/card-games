from card_class import Card
from deck_class import Deck
from user_class import User
from solitataire_class import Solitaire
import time

c = Card("A", "Hearts")
u = User("carl")
d = Deck(make_shuffle=True)
s = Solitaire(u, deck=d)


"""
print(s)
print(s.setup_tableau())
print(s)

print(s.count_total_cards())
"""

