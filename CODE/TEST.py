from card_class import Card
from deck_class import Deck
from user_class import User

u = User("John", 'solitare')
c1 = Card("5", "Hearts")
c2 = Card("4", "Diamonds")
print(u.get_hand())
u.add_hand([c1, c2])
print(u.hand)