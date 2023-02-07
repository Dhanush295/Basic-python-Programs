print("Welcome to tip calculator.")
bill=input("What was the total bill? ")
percent=input("What percentage tip would you like to give? 10, 12, or15,?")
split=input("How many people to split the bill? ")

# print(type(bill))
b=float(bill)
p=int(percent)
s=int(split)
after_split=b+p*(1+1/100)
total_pay=after_split/s
final_amount=round(total_pay, 2)
print(f"Each person should pay: ${final_amount}")



# print("Love Calculator")
# name1=input("Enter Yours name: ")
# name2=input("Enter loved ones name: ")

# nam=name1 + name2
# lowcase=nam.lower()

# t=nam.count("t")
# r=nam.count("r")
# u=nam.count("u")
# e=nam.count("e")

# true=t+r+u+e

# l=nam.count("l")
# o=nam.count("o")
# v=nam.count("v")
# e=nam.count("e")

# love=l+o+v+e

# score=int(str(true)+str(love))

# print(f"Your love score is: {score}.")
