import game_data
import art
import random
from replit import clear


def generate_celeb():
    """Generates a random celebrity from the given data"""
    random_num = random.randint(0,49)
    random_celeb = game_data.data[random_num]
    return random_celeb

def get_name(dict = {}):
    """Returns name of the celebrity"""
    return dict["name"]

def get_description(dict = {}):
    """Returns description of the celebrity"""
    return dict["description"]

def get_followers(dict = {}):
    """Returns number of followers of the celebrity"""
    return dict["follower_count"]

def get_country(dict = {}):
    """Returns country name of the celebrity"""
    return dict["country"]

game_continue = True
score = 0

while game_continue == True:
    
    print(art.logo)

    celeb1 = generate_celeb()
    celeb2 = generate_celeb()
    if celeb1 == celeb2:
        celeb2 = generate_celeb()

    print(f"Compare A: {get_name(celeb1)}, a {get_description(celeb1)}, from {get_country(celeb1)} ")

    print(art.vs)

    print(f"Against B: {get_name(celeb2)}, a {get_description(celeb2)}, from {get_country(celeb2)} ")

    choice = input("Type A or B: ").upper()

    if choice == 'A' and get_followers(celeb1) > get_followers(celeb2):
        score +=1
        game_continue = True
        clear()

    elif choice == 'B' and get_followers(celeb2) > get_followers(celeb1):
        score +=1
        game_continue = True
        clear()

    else:
        game_continue = False

print(f"Sorry, that's wrong. Final score is {score}")