import random
#   Python has four types of collections. 
# 1. Tuple
# 2. Set
# 4. List [<What we're focusing on]
# 4. Dictionary [<What we're focusing on]


# Today, we are going to focus on listssstssttstsss
# listssstssttstsss, order is important. 
# 0 is 1, 1 is 2, for rankings, for lists.
# a listssstssttstsss is a way to store more than one value in single variable
# The values in the lsit are called ITEMS   
# Items can be access by their INDEX (position in the list) indices
# Indisces                  0                       1           2               3               4
best_elden_ring_weapons = ["Blasphemous Blade", "Moonviel", "Rivers of Blood", "Iron Ball", "Bloodhound's Fang"]
best_years = [1776, 1985, 1994, 1957, 2016]
myint = 3

print(len(best_elden_ring_weapons)) # Tells you the amount of index's in the list

print(best_years[myint])

print(best_years[0])
print(best_elden_ring_weapons[0])   # Print the first item
print(best_elden_ring_weapons[len(best_elden_ring_weapons)-1])   

# You want it to be responsive

# List items can be changed!!
best_elden_ring_weapons[3] = "Spiked Fist"
print(best_elden_ring_weapons)

# list functions!
# 1. .pop()
# ^^^Removes an item/index at a given position
best_elden_ring_weapons.pop(1) # Remove Moonveil  from the game
# 2. .remove()
# ^^^ Removes an item/index by value- removes the first instance of the value
best_elden_ring_weapons.remove("Blasphemous Blade") # If value exist, it erros :{

# 3. .append()
# ^^^ Adds the value as a new item at the end of the list
best_elden_ring_weapons.append("Death's Poker")


numbers = [random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100)]

# 4. .sort()
# ^^^ Sorts the numbers from smallest to greatest
numbers.sort()
print(numbers)

# 5. max()
# ^^^ Prints the largest number in the list!
print(max(numbers))

# 6. min()
# ^^^ Prints the smallest number in the list
print(min(numbers))

# Tea from Mr. Osowski: "Strings... are just... lists of characters :[]"
print(len("Osowski"))







