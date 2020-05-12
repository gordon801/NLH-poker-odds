import random

from nlh.Card import Card


# Creating the board (i.e. produce 5 cards from a deck excluding input hands)
# Function: Draw 5 random cards from a deck, excluding hero and villains hands
# (if applicable) - need to ensure the if applicable part
# Returns the community cards (i.e. the cards on the board from that run)


def NLH_run(a1, a2):  # , b1 = None, b2 = None
    # generate deck
    deck = []
    community_cards = []
    for i in range(1, 14):
        cards_clubs = Card(i, "Clubs")
        cards_diamonds = Card(i, "Diamonds")
        cards_hearts = Card(i, "Hearts")
        cards_spades = Card(i, "Spades")
        deck.append(cards_clubs)
        deck.append(cards_diamonds)
        deck.append(cards_hearts)
        deck.append(cards_spades)

    # remove given cards (hero and villain's hands)
    deck.remove(a1)
    deck.remove(a2)
    # deck.remove(b1)
    # deck.remove(b2)

    # generates and returns the flop, turn, and river
    flop = random.sample(deck, k=3)

    for i in flop:
        deck.remove(i)
        community_cards.append(i)

    turn = random.choice(deck)
    deck.remove(turn)
    community_cards.append(turn)

    river = random.choice(deck)
    community_cards.append(river)

    return community_cards




