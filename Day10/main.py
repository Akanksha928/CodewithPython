import art
print(art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1/n2

def modulo(n1, n2):
    return n1 % n2

def operation(num1, num2, symbol):
    for item in operations:
        if symbol == item:
            function = operations[item]
            answer = function(num1, num2)
    return answer

operations = {
 "+": add,
 "-": subtract, 
 "*": multiply, 
 "/": divide,
 "%": modulo,
 }


def calculator():
    num1 = float(input("What's the first number? "))
    for item in operations:
        print(item)
    should_continue = True

    while should_continue == True:
        symbol = input("Enter the operation you would like to perform: ")
        num2 = float(input("What's the second number? "))
        answer = operation(num1, num2, symbol)
        print(f"{num1} {symbol} {num2} = {answer}")

        choice = input(f"Type 'y' if you want to continue operation on {answer} or 'n' to start a new calculation: ")

        if choice == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()

        



