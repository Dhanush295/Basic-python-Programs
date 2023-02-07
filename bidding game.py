print("BIDDING GAME")

bids = {}
start_game = True

def highest_bids(bids_dict):
    highest = 0
    for keys in bids_dict:
        value = bids_dict[keys]
        if value > highest:
            highest = value
            winner = keys
    print(f"The winner is {winner} with amount ${highest}")



while start_game:
    name = input("What's your Name?: ")
    bid_amount = int(input("What's your bid amount?: "))
    bids[name] = bid_amount
    y_n = input("Any other bidders then type 'Yes' else 'No': ").lower()
    if y_n == "no":
        start_game = False
        highest_bids(bids)
    