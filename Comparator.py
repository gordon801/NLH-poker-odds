# add community cards and hero's hand to all_cards
# Find the best 5 card hand given input hands (a = community cards, b1 b2 = hero's hand)
# order straight flush > quads > FUll house > Flush > straight > set > 2p > p > high card

# a = list input
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



def straight_comparison(straight1, straight2):
    print(1)