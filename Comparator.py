# add community cards and hero's hand to all_cards
# Find the best 5 card hand given input hands (a = community cards, b1 b2 = hero's hand)
# order straight flush > quads > FUll house > Flush > straight > set > 2p > p > high card


# returns the highest flush,
def flush_comparison(flushes):
    highest_flush = flushes[0]

    for i in range(1,len(flushes)): 
        flush_check = flushes[i]
        for j in range(5):
            base_index = highest_flush[j].getIndex()
            comparison_index = flush_check[j].getIndex()
            if base_index == 1:
                base_index = 14
            if comparison_index == 1:
                comparison_index = 14
            if comparison_index > base_index:
                highest_flush = flushes[i]
                break

    return highest_flush

def comparator(hand1, hand2):
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

    comp_hand1 = hand1[1]
    comp_hand2 = hand2[1]

    if hand1[0] > hand2[0]:
        return comp_hand1

    elif hand2[0] > hand1[0]:
        return comp_hand2

    else:
        for i in range(5):
            if comp_hand1[i].getIndex() > comp_hand2[i].getIndex():
                return comp_hand1
            elif comp_hand2[i].getIndex() > comp_hand1[i].getIndex():
                return comp_hand2

        #print("Draw")
        return "Draw"

