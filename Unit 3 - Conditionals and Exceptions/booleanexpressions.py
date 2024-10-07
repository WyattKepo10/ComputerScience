# BooLean Expressions
# Kinda like a mathametical formula
# 14 + 10 = 24      Uses Arithmetic operators
# Arithmetic operators[ + - / * ** % // ] 
# Can only evaluate to True or False
# 5 > 10 = False        Boolean Algebra uses comparison operators
# Comparision Operators [ > < >= <= == != ]

print(14 + 10) # Algebra
print(5 > 10) # Boolean Algebra. Difference is, we are asking IF it is greater/lesser then something. We are aksing, a yes or no question, a true or false question.

x = 5 # SET! x equal to 5, tell it what to be.
print(x == 5)   # GET! x equals to 5, ask a question # == asks, "Are you equal?". = equals to something, == asks if its equal to something.

# This is the PERFECT test question
# What is the difference between = and == ?
# = tells it what it is, == asks if it is.

print(4 >= 2)       #True
print(1993 == 1993)         #False
print(-90 < -99)         #False
print(10 != 10) #   != is asking if their different, it means: Not. #False

# Boolean expressions Quiz!
answer_one = input("Give me an integer that is negative\n>")
answer_one = int(answer_one)
print(answer_one < 0)


answer_two = input("Write the number 5\n")
answer_two = int(answer_two)
print(answer_two == 5)

print("Walrus" + "Walrus") #    WalrusWalrus
print("Walrus" == "Walrus") #   True