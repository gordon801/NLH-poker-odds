from nlh.Card import convert2card
from nlh.Card import string2cards
from nlh.Card import Card
from nlh.hand_finder import find_straight
from nlh.hand_finder import find_hand
from nlh.hand_finder import find_flush
from nlh.NLH_run import NLH_run
from nlh.Card import cards2list
from nlh.showdown import showdown
from nlh.showdown import nlh_sim


# understanding hands from input
# not allow invalid inputs (copied cards i.e. reuse 7s)
print("Valid inputs for Card Index = 2-9, T, J, K, Q, A")
print("Valid inputs for Card Suit = d, c, h, s")
#HH = input("Enter your first hand in the format \"Ad 7s\": ")
HH = "Ts 9s"
print(HH)
HH = string2cards(HH)

#VH = input("Enter your second hand in the format \"Ad 7s\": ")
VH = "Ac 2c"
print(VH)
VH = string2cards(VH)
# showdown(HH, VH)


print(nlh_sim(HH, VH, 5000), "%")

# print("The hero's hand is:", printCard(HH1) + ", " + printCard(HH2))

#first_run = NLH_run(HH1,HH2)
#hero_cards = combine_hand(first_run,HH1,HH2)
#find_hand(hero_cards)


test3 = "Ah Ts 9s Kh As Js Qh 8s Jh 7s Th 2s 2c 2d 2h Kc Jc Tc Td Jd 4c 9c Qd Ad Ac"
test4 = "5s 2s"
test5 = "Ac Tc Jc 9c 2c 5c 4c 7c"
test6 = "9d 7c Jd 9h Js 9s 8s"
test7 = "Ah Kc Qs Ts 9c"
test8 = "9s 8s Js 9h As 6c Jd"

#print(test6)
#find_hand(string2cards(test6))

#print(test5)
#find_flush(string2cards(test5))

