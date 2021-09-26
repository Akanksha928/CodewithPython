alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

import art
print(art.logo)

def quit():
  choice = input("Type 'yes' to go again or 'no' to quit\n").lower()
  if choice == "yes":
    intro()

def intro():
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt or 'exit' to exit: \n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(text1 = text, shift1 = shift, direction1 = direction)

def caesar(text1,shift1,direction1):
  cipher = ""
  for i in text1:
    if direction1 == "encode":
      if i in alphabet:
        new_position = (alphabet.index(i)) + shift1%25
      else:
        cipher+=i
    else:
      new_position = (alphabet.index(i)) - shift1%25
    cipher += alphabet[new_position]
  print(f"The {direction1}d text is {cipher}")
  quit()

intro()
