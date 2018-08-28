from user_class import User
from deck_class import Deck
from solitataire_class import Solitaire

u = User("carl", "f")
d = Deck(shuffle=True)
s = Solitaire(u, d)

s.setup_tableau()
d.split_deck(2,3,444)
print(d.cards)