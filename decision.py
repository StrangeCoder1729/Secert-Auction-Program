


def deciding(database):

   
    lst_bids = []
    for bids in database.values():
        lst_bids.append(bids)
    
  
    winner = max(lst_bids)
    
    winner_name = []
    for names in database:
        if database[names]== winner:
            winner_name.append(names)
    if(len(winner_name) == 1):
        name_winner = winner_name[0]
        return name_winner,winner
    else:
        print()
        print("There is a tie bidding")
        print(f"There are {len(winner_name)} who made a high bidding price !")
        print("People :-")
        for name in winner_name:
            print(name)
        
         
         
        exit()
