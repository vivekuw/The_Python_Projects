from replit import clear
from logo import logo

print(logo)
bids = {}
bid_finished: bool = False

def find_highest_bidder(bid_record):
    highest_bid = 0
    bid = ""
    for bidder in bid_record:
        bid_amount = bid_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            bid = bidder
    print(f"the winner is {bid} wit bidding price is {highest_bid}")


while not bid_finished:
    name = input("Your Name :- ")
    price = int(input("your bid price :- "))
    bids[name] = price
    should_finished = input("Auction there is more bid person. Type 'Yes' to continue or 'No' to not continue:- ").lower()
    if should_finished == 'no':
        bid_finished = True
        find_highest_bidder(bids)
    elif should_finished == 'yes':
        clear()  # the clear function is not working in this pycharm
