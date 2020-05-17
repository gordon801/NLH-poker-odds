from nlh.Card import convert2card
from nlh.Card import string2cards
from nlh.Card import Card
from nlh.hand_finder import find_straight
from nlh.hand_finder import combine_hand
from nlh.hand_finder import find_hand
from nlh.hand_finder import find_flush
from nlh.NLH_run import NLH_run
from nlh.Card import cards2list


# understanding hands from input
# not allow invalid inputs (copied cards i.e. reuse 7s)
print("Valid inputs for Card Index = 2-10, J, K, Q, A")
print("Valid inputs for Card Suit = d, c, h, s")
# HH = input("Enter your first hand in the format \"Ad 7s\": ")
HH = "9s 8s"
HH1, HH2 = HH.split()
HH1 = convert2card(HH1)
HH2 = convert2card(HH2)

# print("The hero's hand is:", printCard(HH1) + ", " + printCard(HH2))
# VH = input("Enter your second hand in the format \"Ad 7s\": ")
#first_run = NLH_run(HH1,HH2)
#hero_cards = combine_hand(first_run,HH1,HH2)
#find_hand(hero_cards)


test3 = "Ah Ts 9s Kh As Js Qh 8s Jh 7s Th 2s 2c 2d 2h Kc Jc Tc Td Jd 4c 9c Qd"
test4 = "5s 2s"
test5 = "Ac Tc Jc 9c 2c 5c 4c 7c"
test6 = "Ah Kh Qh Jh Th"
test7 = "4s Ah Kh Qh Jh Th"
test8 = "Ah Kh Qh Jh Th 9h 8h 7h 6h 5h 4h 3h 2h"

print(test3)
find_hand(string2cards(test3))

#print(test5)
#find_flush(string2cards(test5))


# comparing 2 5-card hands, i.e. compare result from find_hand(hero) vs find_hand(villain)


def showdown(a,b):
    print(2)