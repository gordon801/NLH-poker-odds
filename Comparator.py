# add community cards and hero's hand to all_cards
# Find the best 5 card hand given input hands (a = community cards, b1 b2 = hero's hand)
# order straight flush > quads > FUll house > Flush > straight > set > 2p > p > high card


def combine_hand(a, b1, b2):
    all_cards = []
    for i in a:
        all_cards.append(i)
    all_cards.append(b1)
    all_cards.append(b2)
    return all_cards


# Function find a straight, note that hand strengths will be returned as a string of (ordered) indices
# + a dash + a number indicating the 5-card ranking (e.g. straight = 5)


def find_straight(a):
    # find if there are 5 cards in a row, i.e. a straight, factoring in possibility of a wheel straight (A-5)
    straight_counter = []
    card_indices = []
    card_order = []
    for i in a:
        card_indices.append(i.getIndex())

    straight_next_out = max(card_indices)
    straight_counter.append(straight_next_out)
    card_order.append(card_indices.index(straight_next_out))

    special_case = [10, 11, 12, 1]

    while straight_next_out > 0:
        if len(straight_counter) < 5:
            if straight_next_out == 13 and all(item in card_indices for item in special_case):
                straight_counter.extend(special_case)
                for i in special_case:
                    card_order.append(card_indices.index(i))
            else:
                straight_next_out -= 1
                if straight_next_out in card_indices:
                    straight_counter.append(straight_next_out)
                    card_order.append(card_indices.index(straight_next_out))

                else:
                    straight_counter = []
                    card_order = []
                    continue
        else:
            break

    # i.e. output = the highest straight from the input, no output => no straight
    if len(straight_counter) == 5:
        straight_cards = [a[i] for i in card_order]
        return straight_cards


def find_hand(cards_input):
    # add community cards and hero's hand to all_cards
    all_cards = []
    # suit_counter = [c,d,h,s]
    suit_counter = [0, 0, 0, 0]
    # indice_counter = [1,2,...,13], each index represents each possible card index
    indice_counter = [0] * 13
    card_indices = []
    made_hand = 0
    quads_index = 0
    quads_order = []
    fh_trips = 0
    fh_pair = 0
    fh_order = []

    hand_strengths = {
        1: 'Straight Flush',
        2: 'Quads',
        3: 'Full House',
        4: 'Flush',
        5: 'Straight',
        6: 'Set',
        7: 'Two Pair',
        8: 'One Pair',
        9: 'High Card'
    }

    for i in cards_input:
        all_cards.append(i)
        card_indices.append(i.getIndex())
        indice_counter[i.getIndex() - 1] += 1
        if i.getSuit == "Clubs":
            suit_counter[0] += 1
        elif i.getSuit == "Diamonds":
            suit_counter[1] += 1
        elif i.getSuit == "Hearts":
            suit_counter[2] += 1
        elif i.getSuit == "Spades":
            suit_counter[3] += 1

    # look at suit_counter and indice_counter
    print("SC:", suit_counter)
    print("IC:", indice_counter)

    # settle hand rankings
    if any(i >= 5 for i in suit_counter):
        print("Flush")

    # determine quads, if so find the highest quads on the board and return it with the highest kicker
    if any(i == 4 for i in indice_counter):
        for e, i in reversed(list(enumerate(indice_counter, start=1))):
            if i == 4:
                quads_index = e
                break
        for i in cards_input:
            if i.getIndex() == quads_index:
                quads_order.append(cards_input.index(i))
        print("Quads", quads_index, quads_order)

    # determine full house, if so find the highest set+pair on the board and return it with the highest kicker
    if any(i >= 3 for i in indice_counter) & any(i >= 2 for i in indice_counter):
        for e, i in reversed(list(enumerate(indice_counter, start=1))):
            if i >= 3 and fh_trips == 0:
                fh_trips = e
            elif i >= 2 and fh_trips != 0 and fh_pair == 0:
                fh_pair = e
        for i in cards_input:
            if i.getIndex() == fh_trips:
                fh_order.append(cards_input.index(i))

        print("Full House", "trips", fh_trips, "pair", fh_pair)


