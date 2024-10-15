#  Create a function called free_shipping,
#  That tells you if you qualify for free shipping, or not.
#  You only get free shipping if,
#  You are a Prime member OR order is at least $25,
#  And you are atleast 18 years old OR have parents consent.
#  Your function should take four parameters
#  prime (boolean), cost (float), age (int), consent (bool).
#  MASSIVE HINT! 
#  You can use more than one logical operator in a Condition
#  Use parenthesis to group if needed 



def free_shipping(prime, cost, age, consent):
    if (prime == True or cost >= 25) and (age >= 18 or consent == True):
        print("YOU NOW HAVE FREE SHIPPING! CONGRATULATIONS!")
    else:
        print("YOU CANNOT HAVE FREE SHIPPING! SORRY!")






free_shipping(True, 25.00, 18, True)