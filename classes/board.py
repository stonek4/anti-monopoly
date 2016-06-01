from square import SQUARE
from square import PROPERTY
from square import CM
from square import INCOME_TAX
from square import UTILITY
from square import TRANSPORT
from square import AMF
from square import GOTO
from square import PROPERTY_TAX

class BOARD:
    def get_board(self):
        return self.board
    def __init__(self):
        self.board = []
        self.board.append(SQUARE("start","start"))
        self.board.append(PROPERTY("basin st.","new orleans",60,50,6,6,5,10))
        self.board.append(CM("competitor or monopolist"))
        self.board.append(PROPERTY("french quarter","new orleans",60,50,6,6,5,10))
        self.board.append(INCOME_TAX("income tax"))
        self.board.append(TRANSPORT("u.s. railroad"))
        self.board.append(PROPERTY("sunset blvd.","los angeles",100,50,10,10,5,10))
        self.board.append(CM("competitor or monopolist"))
        self.board.append(PROPERTY("wilshire blvd.","los angeles",100,50,10,10,5,10))
        self.board.append(PROPERTY("hollywood blvd.","los angeles",120,66,12,12,5,10))
        self.board.append(SQUARE("sightseeing tour","sightseeing tour"))
        self.board.append(PROPERTY("rush st.","chicago",140,100,14,14,10,20))
        self.board.append(UTILITY("u.s. electric company"))
        self.board.append(PROPERTY("state st.","chicago",140,100,14,14,10,20))
        self.board.append(PROPERTY("michigan ave.","chicago",160,100,16,16,10,20))
        self.board.append(TRANSPORT("u.s. bus company"))
        self.board.append(PROPERTY("locust st.","philadelphia",180,100,18,18,10,20))
        self.board.append(CM("competitor or monopolist"))
        self.board.append(PROPERTY("chesnut st.","philadelphia",180,100,18,18,10,20))
        self.board.append(PROPERTY("walnut st.","philadelphia",200,100,20,20,10,20))
        self.board.append(AMF("anti-monopoly foundation"))
        self.board.append(PROPERTY("brattle st.","boston",220,150,22,22,15,30))
        self.board.append(CM("competitor or monopolist"))
        self.board.append(PROPERTY("harvard square","boston",220,150,22,22,15,30))
        self.board.append(PROPERTY("beacon st.","boston",240,150,24,24,15,30))
        self.board.append(TRANSPORT("u.s. air line"))
        self.board.append(PROPERTY("georgetown","washington",260,150,26,26,15,30))
        self.board.append(PROPERTY("constitution ave.","washington",260,150,26,26,15,30))
        self.board.append(UTILITY("u.s. gas company"))
        self.board.append(PROPERTY("pennsylvania ave.","washington",280,150,28,28,15,30))
        self.board.append(GOTO("go to"))
        self.board.append(PROPERTY("fisherman's wharf","san francisco",300,200,30,30,20,40))
        self.board.append(PROPERTY("union square","san francisco",300,200,30,30,20,40))
        self.board.append(CM("competitor or monopolist"))
        self.board.append(PROPERTY("nob hill","san francisco",320,200,32,32,20,40))
        self.board.append(TRANSPORT("u.s. trucking company"))
        self.board.append(CM("competitor or monopolist"))
        self.board.append(PROPERTY("fifth ave.","new york",350,200,35,35,20,40))
        self.board.append(PROPERTY_TAX("property tax"))
        self.board.append(PROPERTY("wall st.","new york",400,200,40,40,20,40))
