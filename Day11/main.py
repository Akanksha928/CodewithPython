############### Blackjack Project #####################
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.

import random
import art
from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

def calculate_score(list = []):

    if len(list) == 2 and sum(list) == 21:
        return 0
    elif 11 in list and sum(list) > 21:
        list[list.index(11)] = 1
        return sum(list)
    else:
        return sum(list)
    
def deal_card():
    card = random.choice(cards)
    return card

def compare(a, b):
    if a == b:
        print("Its a draw!")
    if b == 0:
        print("Computer Wins!")
    if a == 0:
        print("You Win!")
    if a > b:
        if a <= 21:
            print("You Win!")
    if b > a:
        if b <= 21:
            print("You Lose!")
    if a > 21:
        print("You Lose!")
    if b > 21:
        print("You Win!")

 
choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

def blackjack():

    print(art.logo)

    total = []
    dealer_total = []

    for i in range(2):
        total.append(deal_card())
        dealer_total.append(deal_card())

    print(f"Your cards: {total}, current score is {calculate_score(total)}")
    print(f"Computer's first card: {dealer_total[0]}")

    while calculate_score(dealer_total) < 17:
        dealer_total.append(deal_card())
   
    deal_cards = True 


    while calculate_score(total) < 21 and deal_cards == True:

        if calculate_score(total) == 0:
            deal_cards = False
            print("You Win!")
        if calculate_score(dealer_total) == 0:
            deal_cards = False
            print("You Lose!")

        game = input("Type 'y' to get another card, type 'n' to pass: ")
        if game == 'y':
            total.append(deal_card())
            print(f"Your current score is {calculate_score(total)}")
        else:
            deal_cards = False


    print(f"Your final hand is {total}, final score is {calculate_score(total)}")
    
    print(f"Computer's final cards are {dealer_total}, final score: {calculate_score(dealer_total)}")
    

    my_score = calculate_score(total)
    computer_score = calculate_score(dealer_total)

    compare(my_score, computer_score)

if choice == 'y':
    blackjack()

end_of_game = False
while end_of_game == False:
    choice = input("Do you want to play again? Type 'y' to play again or type 'n' to quit: ")
    if choice == 'y':
        clear()
        blackjack()
    else:
        end_of_game = True

