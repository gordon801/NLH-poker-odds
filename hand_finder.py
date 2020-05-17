from nlh.Card import cards2list
from nlh.Comparator import flush_comparison


def combine_hand(a, b1, b2):
    all_cards = []
    for i in a:
        all_cards.append(i)
    all_cards.append(b1)
    all_cards.append(b2)
    return all_cards


# find if there are 5 cards in a row, i.e. a straight, factoring in possibility of an A-high straight (AKQJT)
# output = highest straight from input, or none
def find_straight(cards_input):
    straight_counter = []
    card_indices = []
    card_order = []
    for i in cards_input:
        card_indices.append(i.getIndex())

    straight_next_out = max(card_indices)
    straight_counter.append(straight_next_out)
    card_order.append(card_indices.index(straight_next_out))

    special_case = [12, 11, 10, 1]

    while straight_next_out > 0:
        if len(straight_counter) < 5:
            if straight_next_out == 13 and all(item in card_indices for item in special_case):
                straight_counter.extend(special_case)
                for i in special_case:
                    card_order.append(card_indices.index(i))
                card_order.insert(0, card_order[4])
                card_order.pop(5)
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
        straight_cards = [cards_input[i] for i in card_order]
        return straight_cards


def find_flush(cards_input):
    if find_straight(cards_input) is not None:
        return 1, find_straight(cards_input)
    else:
        indice_order = []
        highest_flush = []
        for i in cards_input:
            indice_order.append(i.getIndex())
        indice_order.sort(reverse=True)
        for i in indice_order[0:5]:
            for j in cards_input:
                if i == j.getIndex():
                    highest_flush.append(j)
        return 0, highest_flush


def find_hand(cards_input):
    # add community cards and hero's hand to all_cards
    all_cards = []
    # suit_counter = [c,d,h,s]
    suit_counter = [0, 0, 0, 0]
    # indice_counter = [1,2,...,13], each index represents each possible card index
    indice_counter = [0] * 13
    card_indices = []
    hand_strength = 10
    quads_index = 0
    fh_trips_index = 0
    fh_trips = []
    fh_pair_index = 0
    fh_pair = []
    best_hand = []


    # hand_strengths = {
    #     1>9: 'Straight Flush',
    #     2>8: 'Quads',
    #     3>7: 'Full House',
    #     4>6: 'Flush',
    #     5>5: 'Straight',
    #     6>4: 'Set',
    #     7>3: 'Two Pair',
    #     8>2: 'One Pair',
    #     9>1: 'High Card'
    # }

    suit_counter_suits = {
        0: 'Clubs',
        1: 'Diamonds',
        2: 'Hearts',
        3: 'Spades'
    }

    for i in cards_input:
        all_cards.append(i)
        card_indices.append(i.getIndex())
        indice_counter[i.getIndex() - 1] += 1
        if i.getSuit() == "Clubs":
            suit_counter[0] += 1
        elif i.getSuit() == "Diamonds":
            suit_counter[1] += 1
        elif i.getSuit() == "Hearts":
            suit_counter[2] += 1
        elif i.getSuit() == "Spades":
            suit_counter[3] += 1

    # look at suit_counter and indice_counter (troubleshooting)
    print("SC:", suit_counter)
    print("IC:", indice_counter)

    # return the highest flush, but also check for straight flush
    flush_hands = []
    sf_hands = []
    if any(i >= 5 for i in suit_counter):
        for k in range(4):
            flush_cards = []
            i = suit_counter[k]
            if i >= 5:
                for j in cards_input:
                    if j.getSuit() == suit_counter_suits[k]:
                        flush_cards.append(j)
                output = find_flush(flush_cards)

                if output[0] == 1:
                    sf_hands.append(output[1])
                else:
                    flush_hands.append(output[1])

        if len(sf_hands) > 0:
            best_hand = flush_comparison(sf_hands)
            # hand_strength = 9
        else:
            best_hand = flush_comparison(flush_hands)
            # hand_strength = 6

        print("Flush", cards2list(best_hand))
        #return hand_strength, best_hand
    hand_strength = 0

    # determine quads, if so find the highest quads on the board and return it with the highest kicker
    if any(i == 4 for i in indice_counter) and hand_strength < 9:
        for e, i in reversed(list(enumerate(indice_counter, start=1))):
            if i == 4:
                quads_index = e
                break
        for i in cards_input:
            if i.getIndex() == quads_index:
                best_hand.append(i)
        #hand_strength = 8
        print("Quads", quads_index, cards2list(best_hand))
        #return hand_strength, best_hand

    # determine full house, and return the highest set+pair on the board
    if any(i >= 3 for i in indice_counter) and any(i >= 2 for i in indice_counter) and hand_strength < 8:
        best_hand = []
        for e, i in reversed(list(enumerate(indice_counter, start=1))):
            if i >= 3 and fh_trips_index == 0:
                fh_trips_index = e
            elif i >= 2 and fh_trips_index != 0 and fh_pair_index == 0:
                fh_pair_index = e
        for i in cards_input:
            if i.getIndex() == fh_trips_index and len(fh_trips) < 3:
                fh_trips.append(i)
            if i.getIndex() == fh_pair_index and len(fh_pair) < 2:
                fh_pair.append(i)
        best_hand.extend(fh_trips)
        best_hand.extend(fh_pair)
        #hand_strength = 7
        print("Full House", "trips", fh_trips_index, "pair", fh_pair_index, cards2list(best_hand))
        #return hand_strength, cards2list(best_hand)

    # determine straight and return the highest straight
    if hand_strength < 6:
        straight_cards = find_straight(cards_input)
        if straight_cards is not None:
            best_hand = straight_cards
            #hand_strength = 5
            print("Straight", cards2list(best_hand))
            #return hand_strength, best_hand

    if any(i == 3 for i in indice_counter) and hand_strength < 5:
        print(1)