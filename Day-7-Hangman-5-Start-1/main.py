import hangman_words
import random
import hangman_art

print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)
li = list(chosen_word)

turns = 7

#Creating the blank hangman guessing template
for i in range(len(chosen_word)):
  li[i] = "_"

#Checking if game is over
while "_" in li and turns > 0:
  flag = False
  guess = input("Guess a letter: ").lower()

  for i in range(len(chosen_word)):
    if chosen_word[i]==guess:
      li[i]=guess

  if guess not in chosen_word:
    flag = True
  print(' '.join(li))

  if(flag==True):
    turns -=1
    print(hangman_art.stages[turns])

#Checking if user has won or lost
if(turns==0 and "_" in li ):
  print("Sorry, you lost!")
else:
  print("Congrats, you won!")    

