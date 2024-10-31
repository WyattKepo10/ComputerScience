import random
def drop_item():
    roll = random.randint(0, 100000)
    if roll < 7000: 
        print("NORMAL ITEM")
    elif roll < 9000:
        print("UNCOMMON ITEM")
    elif roll < 9900:
        print("RARE ITEM")
    elif roll < 9990:
        print("LEGENDARY ITEM")
    elif roll <= 10000:
        print("MAXIMUM ITEM")
    
    elif roll > 7000:
        print("Nothing")
    
    if input("Play Again?\n>") == "y":
        drop_item()

drop_item()