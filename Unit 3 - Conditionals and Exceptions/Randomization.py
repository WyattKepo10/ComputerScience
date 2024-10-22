import random # What it does is it says "Hey, this is a tool i wanna use and random is the tool i wanna use

r = random.randrange(0, 10) # Randrange is a tool that you give a range too and the range gives you a number
print(r)

print("You have a 25 perccent chance to win!")
p = random.random()
# random.random generates a random float betweeen 0 and 1
print(p)
if p <= 1/8000:
    print("YOU WIN!!")
else:
    print("You LOSE!!")