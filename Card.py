# Defining classes and functions
class Card:
    def __init__(self, index, suit):
        self.index = index
        self.suit = suit

    def __eq__(self, other):
        return self.index == other.index and self.suit == other.suit

    def getIndex(self):
        return self.index

    def getSuit(self):
        return self.suit

    def printCard(self):
        face_cards_int = {
            1: 'Ace',
            11: 'Jack',
            12: 'Queen',
            13: 'King'
        }
        if self.index > 10 or self.index == 1:
            return str(face_cards_int[self.index]) + " of " + str(self.suit)

        else:
            return str(self.index) + " of " + str(self.suit)


def printCard(a):
    face_cards_int = {
        1: 'Ace',
        11: 'Jack',
        12: 'Queen',
        13: 'King'
    }
    if a.index > 10 or a.index == 1:
        return str(face_cards_int[a.index]) + " of " + str(a.suit)

    else:
        return str(a.index) + " of " + str(a.suit)

# reading hands
# convert string (e.g. Ad to card) (a is in format index+suit) (test As, as, ts, 8s)


def convert2card(a):
    a = a.upper()
    a_card = Card(0, 0)

    suits = {
        "C": "Clubs",
        "D": "Diamonds",
        "H": "Hearts",
        "S": "Spades"
    }

    face_cards_string = {
        "A": 1,
        "T": 10,
        "J": 11,
        "Q": 12,
        "K": 13
    }

    # defining the suit of the card
    a_card.suit = suits[a[-1]]

    # defining the index of the card
    if a[:-1] in face_cards_string:
        a_card.index = int(face_cards_string[a[:-1]])
    else:
        a_card.index = int(a[:-1])

    # returning the card
    return a_card


def string2cards(a):
    card_list = []
    string_list = a.split()
    for i in string_list:
        card_list.append(convert2card(i))
    return card_list


def card2string(a):
    card_string = ""
    face_cards_short = {
        1: 'A',
        11: 'J',
        12: 'Q',
        13: 'K'
    }
    reverse_suits = {
        "Clubs": "c",
        "Diamonds": "d",
        "Hearts": "h",
        "Spades": "s"
    }
    if a.index in face_cards_short:
        card_string += face_cards_short[a.index] + reverse_suits[a.suit]
    else:
        card_string += str(a.index) + reverse_suits[a.suit]
    return card_string
