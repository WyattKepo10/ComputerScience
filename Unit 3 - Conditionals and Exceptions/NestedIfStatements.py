# You can put a if inside of an if
# This is called a nested if statement
# Not the best to practice USUALLY!, though it still works

prime = True
cost = 20
age = 17
consent = False

# if (prime ==Ture or cost >= 25) and (age >= 18 or  consent == True):

if prime:
    if age>= 18:
        print("FREE SHIPPING APPLIED!")
    elif consent:
        print("FREE SHIPPING APPLIED!")
    else:
        print("NO FREE SHIPPING FOR YOU! HAHAHA!")

elif cost >= 25:
     if age>= 18:
        print("FREE SHIPPING APPLIED!")
     elif consent:
        print("FREE SHIPPING APPLIED!")
     else:
        print("NO FREE SHIPPING FOR YOU! HAHAHA!") 

else:
    print("NO FREE SHIPPING FOR YOU! HAHAHA!")

 # Example for best practice

# Decide if we need an umbrella
# You need an umbrella if its raining AND you are going outside that day

raining = input("Is it raining outside?\n>")
# outside = input("Do you plan on going outside?\n>")

if raining.upper == "Yes":
    outside = input("Do you plan on going outside?\n>") 
    if outside.upper("yes"):
        print("BRING AN UMBERELLA DUMBI!")
    else:
        print("DO NOT BRING AN UMBERELLA DUMBI!")
else:
    print("DO NOT BRING AN UMBERELLA YOU DUMBI!")


#  In a situation where if the first option matters for the second option, then this is practical