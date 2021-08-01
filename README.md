# NLH Poker Odds Calculator

This program calculates the probability of a certain (No Limit Texas Hold'em) poker hand winning against another hand.

The results have been checked against a 3rd party program (https://www.pokerstrategy.com/poker-software-tools/equilab-holdem/) and determined to be reasonably correct. I've highlighted the relevant probabilities in the screenshots below (Draw % (program) ≈ tie % * 2 (equilab))).

**Note: there is some variance in the python calculator's results due to a relatively low simulation number (50,000), which can be increased for less variance in result.**

**NB: Program logic and structure is scheduled to be refactored in the near future.**

## Program Structure
* Card.py: Class "Card" definitions and related functions.
* NLH_run.py: Generates one simulation of the board for two given hands.
* hand_finder.py: Algorithm to find the best 5-card hand from the board.
* Comparator.py: Function to compare two 5-card hands to determine the best hand.
* showdown.py: Generates all the simulations and keeps track of the number of wins and draws.
* run.py: Wrapper script that calls the other .py scripts and outputs the result.

## Example 1: Ad 7s vs As 7h
![image](https://user-images.githubusercontent.com/62014067/127465151-9524d137-9a4b-4b8a-8706-85016a8518c8.png)

![image](https://user-images.githubusercontent.com/62014067/127757530-d8a15998-4f91-4816-b209-ef6998802f96.png)

## Example 2: As Kh vs Td 6c
![image](https://user-images.githubusercontent.com/62014067/127466808-e19cb406-acdf-4b26-9eea-f55c2ccff13b.png)

![image](https://user-images.githubusercontent.com/62014067/127757595-408d1d13-9f01-4f03-b2c6-e7a2e675e8e2.png)

## Example 3: Ad As vs Kh Kc
![image](https://user-images.githubusercontent.com/62014067/127467232-6d9c5c8b-c895-4d78-b6fe-64810ef7c665.png)

![image](https://user-images.githubusercontent.com/62014067/127757610-874bf7ea-6ed0-4002-8426-fb2417355ba4.png)
