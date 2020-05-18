from nlh.NLH_run import NLH_run
from nlh.hand_finder import find_hand
from nlh.Card import cards2list
from nlh.Comparator import comparator


def showdown(hand1, hand2):
    # print("Hand 1:", cards2list(hand1))
    # print("Hand 2:", cards2list(hand2))

    simulated_board = NLH_run(hand1, hand2)
    # print("Board:", cards2list(simulated_board))

    for i in simulated_board:
        hand1.append(i)
        hand2.append(i)

    best_hand1 = find_hand(hand1)

    best_hand2 = find_hand(hand2)

    result = comparator(best_hand1, best_hand2)

    print(find_hand.hand_strengths[1])

    if result == best_hand1[1]:
        print("Hero won with a", best_hand1[0], cards2list(result))
        return 1, best_hand1[0], result
    elif result == best_hand2[1]:
        print("Villain won with a", best_hand2[0], cards2list(result))
        return 2, best_hand2[0], result
    else:
        print("Draw! Both players had a", best_hand1[0])
        return 0, best_hand1[0], result

