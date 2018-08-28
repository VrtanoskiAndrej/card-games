from card_class import Card
from deck_class import Deck
from user_class import User
from solitataire_class import Solitaire

u = User("carl")
d = Deck(make_shuffle=True)
s = Solitaire(u, d)

#s.setup_tableau()
d.split_deck(2, 3, 444)
print(d.cards)
