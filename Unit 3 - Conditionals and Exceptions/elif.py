# The if statement has two buddies
# The first little buddy is the else statement

x = 10

if x > 0:   # not every if needs an else
    print("x is a positive number.")

# The second buddy is the elif statment (short for: else if)
elif x < 0:
    print("x is a negative number")

else:    # else always needs an if
    print("x is zero")



light = input("What color is light?\n>")

if light.lower() == "green":
    print("GO!")

elif light.lower() == "yellow":
    print("STOP IF IT'S SAFE TO DO SO!")

elif light.lower() == "red":
    print("STOP! YOU SCUM!")

else:
    print("NOT VALID! TRY AGAIN!")



x = 10

if x > 5:
    print("x is greter than 5")

if x > 8:
    print("x is greater than 8")

###########################################
if x > 5:
    print("x is greater than 5")
elif x > 8:
    print("x is greater than 8")
