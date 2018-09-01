from card_class import Card
from deck_class import Deck
from user_class import User
from solitataire_class import Solitaire
from parse import JParser
from link_json_class import Link
import json

c = Card("A", "Hearts")
u = User("carl")
d = Deck(make_shuffle=True)
s = Solitaire(u, deck=d)
l = Link("game_state.json")


