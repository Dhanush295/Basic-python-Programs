import random
from art import logo, vs
from game_data import data
TOTAL = 0


print(logo)

account_a = random.choice(data)
account_b = random.choice(data)

if account_a == account_b:
  account_b = random.choice(data)

account_name = account_a["name"]
account_desc = account_a["description"]
account_country = account_a["country"]

print(f"Compare A : '{account_name}', '{account_desc}', '{account_country}'")

print(vs)

account_name = account_b["name"]
account_desc = account_b["description"]
account_country = account_b["country"]

print(f"Compare B : '{account_name}', '{account_desc}', '{account_country}'")

guess = input("Who has more followers:Type 'A' or 'B' ").lower()


follower_a = account_a["follower_count"]
follower_b = account_b["follower_count"]

if guess == "a":
  if follower_a > follower_b:
    TOTAL +=  1
print(f" you total is {TOTAL}")
  
  