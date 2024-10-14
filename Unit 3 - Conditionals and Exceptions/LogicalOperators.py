# Logical Operators
# Types of  Operators
#   Arithmetic Operators +  - * / // ** %
#   Comparison Operators > < >= <= ==
#   Logical operators and or ! (! = Not)
# AND menas that BOTH conditions must be true.
# OR menas that at least one condition must be true
# ! (not) means the inverse, ex.    ! = (not equal to)


def check_elegibility(age, experience):
# What we did before    
#   if age >= 18 and experience >= 1: # Both conditions must be true.
#   if age >= 18 or experience >= 1: # One must be true
#   if age >= 18 and age <= 22:  # You need a fulll Boolean expression on both sides of the Operators.
    if age >= 18 and experience >= 1:
        print("YOU ARE ELIGIBLE")

    else:
        print("YOU ARE NOT ELIGIBLE")












check_elegibility()