from Comparator import flush_comparison


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
        if 1 in indice_order:
            indice_order.insert(0,indice_order.pop(indice_order.index(1)))
        for i in indice_order[0:5]:
            for j in cards_input:
                if i == j.getIndex():
                    highest_flush.append(j)
        return 0, highest_flush


# from input, returns (hand_strength, best_hand)
def find_hand(cards_input):
    # add community cards and hero's hand to all_cards
    all_cards = []
    # suit_counter = [c,d,h,s]
    suit_counter = [0, 0, 0, 0]
    # indice_counter = [1,2,...,13], each index represents each possible card index
    indice_counter = [0] * 13
    card_indices = []

    hand_strengths = {
        9: 'Straight Flush',
        8: 'Quads',
        7: 'Full House',
        6: 'Flush',
        5: 'Straight',
        4: 'Three of a Kind',
        3: 'Two Pair',
        2: 'One Pair',
        1: 'High Card'
    }

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

    # move Ace (index 1) to the end, giving it index 14 (13 (K) + 1)
    # need to insert in every function that if it include this index, will need to change it back to 1
    indice_counter.append(indice_counter.pop(0))

    # print suit_counter and indice_counter
    #print("SC:", suit_counter)
    #print("IC:", indice_counter)

    hand_strength = 0
    best_hand = []

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
            hand_strength = 9
        else:
            best_hand = flush_comparison(flush_hands)
            hand_strength = 6

        # print(hand_strengths[hand_strength], cards2list(best_hand))
        return hand_strength, best_hand

    # determine quads, if so find the highest quads on the board and return it with the highest kicker
    if any(i == 4 for i in indice_counter) and hand_strength < 9:
        kicker_index = 0
        quads_index = 0
        for e, i in reversed(list(enumerate(indice_counter, start=2))):
            if i == 4 and quads_index == 0:
                quads_index = e
            if i > 0 and e != quads_index and kicker_index == 0:
                kicker_index = e

        if quads_index == 14:
            quads_index = 1
        if kicker_index == 14:
            kicker_index = 1

        for i in cards_input:
            if i.getIndex() == quads_index:
                best_hand.append(i)
        for i in cards_input:
            if i.getIndex() == kicker_index:
                best_hand.append(i)
                break
        hand_strength = 8
        # print(hand_strengths[hand_strength], cards2list(best_hand))
        return hand_strength, best_hand

    # determine full house, and return the highest set+pair on the board
    # Logic: If there's 3 of one index and at least 2 indices with 2 of each index (inc. the 3)
    if any(i >= 3 for i in indice_counter) and sum(i >= 2 for i in indice_counter) >= 2 and hand_strength < 8:
        fh_trips_index = 0
        fh_trips = []
        fh_pair_index = 0
        fh_pair = []
        for e, i in reversed(list(enumerate(indice_counter, start=2))):
            if i >= 3 and fh_trips_index == 0:
                fh_trips_index = e
            elif i >= 2 and fh_trips_index != e and fh_pair_index == 0:
                fh_pair_index = e

        if fh_trips_index == 14:
            fh_trips_index = 1
        if fh_pair_index == 14:
            fh_pair_index = 1

        for i in cards_input:
            if i.getIndex() == fh_trips_index and len(fh_trips) < 3:
                fh_trips.append(i)
            if i.getIndex() == fh_pair_index and len(fh_pair) < 2:
                fh_pair.append(i)
        best_hand.extend(fh_trips)
        best_hand.extend(fh_pair)
        hand_strength = 7
        # print(hand_strengths[hand_strength], cards2list(best_hand))
        return hand_strength, best_hand

    # determine straight and return the highest straight
    if hand_strength < 6:
        straight_cards = find_straight(cards_input)
        if straight_cards is not None:
            best_hand = straight_cards
            hand_strength = 5
            # print(hand_strengths[hand_strength], cards2list(best_hand))
            return hand_strength, best_hand

    # determine trips and return the highest trips and kickers
    if any(i == 3 for i in indice_counter) and hand_strength < 5:
        trip_kickers = []
        trips_index = 0
        trip_kickers_counter = 2
        for e, i in reversed(list(enumerate(indice_counter, start=2))):
            if i == 3 and trips_index == 0:
                trips_index = e
            if i > 0 and trip_kickers_counter > 0 and e != trips_index:
                trip_kickers.append(e)
                trip_kickers_counter -= i

        if trips_index == 14:
            trips_index = 1
        for i in trip_kickers:
            if i == 14:
                trip_kickers[trip_kickers.index(i)] = 1

        for i in cards_input:
            if i.getIndex() == trips_index:
                best_hand.append(i)
        for i in trip_kickers:
            for j in cards_input:
                if j.getIndex() == i:
                    best_hand.append(j)

        hand_strength = 4
        # print(hand_strengths[hand_strength], cards2list(best_hand))
        return hand_strength, best_hand

    # determine top two pair and return the highest top two pair and kicker
    if sum(i >= 2 for i in indice_counter) >= 2 and hand_strength < 4:
        top_two_pair_index = 0
        bot_two_pair_index = 0
        two_pair_kicker = 0
        for e, i in reversed(list(enumerate(indice_counter, start=2))):
            if i == 2 and top_two_pair_index == 0:
                top_two_pair_index = e
            elif i == 2 and bot_two_pair_index == 0:
                bot_two_pair_index = e
            elif (i > 0, top_two_pair_index != e, bot_two_pair_index != e, two_pair_kicker == 0) == (True, True, True, True):
                two_pair_kicker = e

        if top_two_pair_index == 14:
            top_two_pair_index = 1
        if bot_two_pair_index == 14:
            bot_two_pair_index = 1
        if two_pair_kicker == 14:
            two_pair_kicker = 1

        for i in cards_input:
            if i.getIndex() == top_two_pair_index:
                best_hand.append(i)
        for i in cards_input:
            if i.getIndex() == bot_two_pair_index:
                best_hand.append(i)
        for i in cards_input:
            if i.getIndex() == two_pair_kicker:
                best_hand.append(i)
                break

        hand_strength = 3
        # print(hand_strengths[hand_strength], cards2list(best_hand))
        return hand_strength, best_hand

    # determine pair and return the highest pair and kickers
    if any(i == 2 for i in indice_counter) and hand_strength < 3:
        pair_kickers = []
        pair_index = 0
        pair_kickers_counter = 3
        for e, i in reversed(list(enumerate(indice_counter, start=2))):
            if i == 2 and pair_index == 0:
                pair_index = e
            if i > 0 and pair_kickers_counter > 0 and e != pair_index:
                pair_kickers.append(e)
                pair_kickers_counter -= i

        if pair_index == 14:
            pair_index = 1
        for i in pair_kickers:
            if i == 14:
                pair_kickers[pair_kickers.index(i)] = 1

        for i in cards_input:
            if i.getIndex() == pair_index:
                best_hand.append(i)
        for i in pair_kickers:
            for j in cards_input:
                if j.getIndex() == i:
                    best_hand.append(j)

        hand_strength = 2
        # print(hand_strengths[hand_strength], cards2list(best_hand))
        return hand_strength, best_hand

        # determine and return the highest 5 cards
    if hand_strength < 2:
        high_cards = []
        high_card_counter = 5
        for e, i in reversed(list(enumerate(indice_counter, start=2))):
            if i > 0 and high_card_counter > 0:
                high_cards.append(e)
                high_card_counter -= i

        for i in high_cards:
            if i == 14:
                high_cards[high_cards.index(i)] = 1

        for i in high_cards:
            for j in cards_input:
                if j.getIndex() == i:
                    best_hand.append(j)

        hand_strength = 1
        # print(hand_strengths[hand_strength], cards2list(best_hand))
        return hand_strength, best_hand
