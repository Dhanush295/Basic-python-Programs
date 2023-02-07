def add(n1,n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def multi(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

caluculate = {
    "+": add,
    "-": sub,
    "*": multi,
    "/": divide
}

print("  online Calculator ")
num1 = int(input(" Whats the number: "))
   
for keys in caluculate:
    print(keys)

start_game = True
while start_game:

    operation = input(" Which opertaion you like to perform: ")
    num2 = int(input(" Whats the Next number: "))
    
    functions_call = caluculate[operation]
    answer = functions_call(num1, num2)
    print(f"The answer is: {answer}")

    y_n = input("like to calculate again then type 'yes' or to stop type 'no': ").lower()
    if y_n == "yes":
        num1 = answer
    else:
        start_game = False

        