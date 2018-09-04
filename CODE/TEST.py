from card_class import Card
from deck_class import Deck
from user_class import User
from solitataire_class import Solitaire
import sys
from parse import JParser
import json

c = Card("A", "Hearts")
u = User("carl")
d = Deck(make_shuffle=False)
s = Solitaire(u, "game_state.json", deck=d)

s.setup_tableau()
s.jparse.iter_through()




def window():
    app = QtGui.QApplication(sys.argv)
    w = QtGui.QWidget()
    b = QtGui.QLabel(w)
    b.setText("Hello World!")
    w.setGeometry(100, 100, 200, 50)
    b.move(50, 20)
    w.setWindowTitle(“PyQt”)
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()