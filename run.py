from nlh.Card import convert2card
from nlh.Card import printCard
from nlh.Card import card2string
from nlh.Card import string2cards
from nlh.Card import Card
from nlh.Comparator import find_straight
from nlh.Comparator import combine_hand
from nlh.Comparator import find_hand
from nlh.NLH_run import NLH_run


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

a = "9s 8s 7s 5d 6h 4s Jc 8c 7c"
b = "9s 9c 9d 9h 8c 8d 8h 8s 7s 6h 5c"


#find_hand(string2cards(a))
find_hand(string2cards(b))



# comparing 2 5-card hands, i.e. compare result from find_hand(hero) vs find_hand(villain)


def showdown(a,b):
    print(2)