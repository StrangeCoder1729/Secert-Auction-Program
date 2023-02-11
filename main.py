import os
import decision
import auction_art

def details():
    user_name = input("Enter your full name : ")
    bid = int(input("Enter Your bid : $"))
    return user_name,bid


print(auction_art.draw)
database = {}
user_name,bid = details()
database[user_name]=bid

def auction():
    while(True):
    
        other_bids = input("Are there any other bids ? Type 'yes' or 'no' : ").lower()
        if other_bids == 'yes':
            os.system('cls')
            user_name,bid = details()
            database[user_name]=bid

        else:
            winnner_name,winner_price = decision.deciding(database)
            print()
            print(f"Winner Name : {winnner_name}")
            print(f"Bidding Price : ${winner_price}")
            exit()


auction()