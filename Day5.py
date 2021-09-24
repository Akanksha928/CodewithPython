#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy Level - Order not randomised:

#Creating an empty string
easy_pwd = ""

for i in range(nr_letters):
  easy_pwd += random.choice(letters) 

for i in range(nr_symbols):
  easy_pwd += random.choice(symbols) 

for i in range(nr_numbers):
  easy_pwd += random.choice(numbers) 

print(f"Your password of Easy level is {easy_pwd}")

#Hard Level - Order randomised:

#Inputting the easy password into a list
temp = list(easy_pwd)

#Shuffling elements in list
random.shuffle(temp)

#Converting back into string
hard_pwd = ""

for i in temp:
  hard_pwd += i
print(f"Your password of Hard level is {hard_pwd}") 
