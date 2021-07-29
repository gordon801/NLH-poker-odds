from Card import string2cards
from showdown import nlh_sim

# understanding hands from input
# not allow invalid inputs (copied cards i.e. reuse 7s)
print("Valid inputs for Card Index = 2-9, T, J, K, Q, A")
print("Valid inputs for Card Suit = d, c, h, s")
HH = input("Enter your first hand in the format \"Ad 7s\": ")
HH_card = string2cards(HH)

VH = input("Enter your second hand in the format \"Ad 7s\": ")
VH_card = string2cards(VH)

nlh_sim_results = nlh_sim(HH_card, VH_card, 50000)

print(f'{HH} wins {nlh_sim_results[0]}% of the time and draws {nlh_sim_results[1]}% of '
      f'the time over {nlh_sim_results[2]} simulations.')