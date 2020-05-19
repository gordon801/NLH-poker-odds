from nlh.NLH_run import NLH_run
from nlh.hand_finder import find_hand

from nlh.Card import cards2list
from nlh.Comparator import comparator

from nlh.Card import string2cards
from nlh.Card import Card


def showdown(hand1, hand2):
    # print("Hand 1:", cards2list(hand1))
    # print("Hand 2:", cards2list(hand2))

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

    simulated_board = NLH_run(hand1, hand2)
    # print("Board:", cards2list(simulated_board))

    new_hand1 = []
    new_hand2 = []

    for i in hand1:
        new_hand1.append(i)
    for i in hand2:
        new_hand2.append(i)

    for i in simulated_board:
        new_hand1.append(i)
        new_hand2.append(i)

    best_hand1 = find_hand(new_hand1)
    best_hand2 = find_hand(new_hand2)
    result = comparator(best_hand1, best_hand2)

    if result == best_hand1[1]:
        # print("Hero won with a", hand_strengths[best_hand1[0]], "hand", cards2list(result))
        return 1, best_hand1[0], result
    elif result == best_hand2[1]:
        # print("Villain won with a", hand_strengths[best_hand2[0]], "hand", cards2list(result))
        return 2, best_hand2[0], result
    else:
        # print("Draw! Both players had a", hand_strengths[best_hand1[0]], "hand")
        return 0, best_hand1[0], result


def nlh_sim(hand1, hand2, sim_num):
    hand1_wins = 0
    draws = 0
    for i in range(sim_num):
        result = showdown(hand1, hand2)
        if result[0] == 1:
            hand1_wins += 1
        elif result[0] == 0:
            draws += 1
    print("W:", hand1_wins, "D:", draws, "N:", sim_num)
    return ((hand1_wins + draws) / sim_num) * 100
