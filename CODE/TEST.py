from card_class import Card
from deck_class import Deck
from user_class import User
from solitataire_class import Solitaire
import time

c = Card("A", "Hearts", skin="character")
u = User("carl")
d = Deck(make_shuffle=True, card_skin="emoji")
s = Solitaire(u, deck=d)


print(d)
for card in d.create_graphic_deck():
    print(card)
    print("")
"""
print(s)
print(s.setup_tableau())
print(s)

print(s.count_total_cards())
"""