from replit import clear
import art

def bidding():

    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    dictionary = {}
    dictionary[name] = bid
    choice = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
    if choice == 'yes':
        clear()
        bidding()
    else:
        findLargest(dictionary)

def findLargest(dictionary = {}):
    #Converting dictionary values and keys into two lists
    v = list(dictionary.values())

    k = list(dictionary.keys())
    #Finding max key and value through lists
    print(f"The winner is {k[v.index(max(v))]} with a bid of ${max(v)}!")

print(art.logo)
print("Welcome to the secret auction program!")
bidding()

#HINT: You can call clear() to clear the output in the console.