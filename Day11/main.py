############### Blackjack Project #####################y
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
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


##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

