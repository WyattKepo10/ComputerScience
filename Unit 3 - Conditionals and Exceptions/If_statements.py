# If statements evaluate boolean expressions
# They make decisions about which code to run next

# Take a temperature
# Print "<temperature> is hot"
# Otherwise, print "temperature is not hot"
temp = input("Whats the temperature in F?\n>")
temp = int(temp)

# if <boolean expression>:
# This should remind me of writing a function
# def <name>():
if temp >= 80:
    print(str(temp) + " fahrenheit is hot!")

# if temp < 80:
    # print(str(temp) + "o is not hot...")

else:   # Otherwise...
    print(str(temp) + " fahrenheit is not hot...")

# Not all if statements need an else. in fact NONE of them NEED and else statement
# Else statements are an option, they are optional
#But, ALL else statements must have corresponding if statement
# Else statements cannot exist alone
# An if statement can only have one else

# Create a program taht asks for a password
# IF the password is correct, print ACCESS GRANTED
# Otherwise, print ACCESS DENIED
# The password is skibidi68.9

#What i did
#v
#v
#v

password = input("Please enter the password\n>")
if password == "skibidi68.9":
    print("ACCESS GRANTED!")
else:
    print("ACCESS DENIED. Try again.")

#What Mr. Osowski did
#v
#v
#v

real_pass = "skibidi68"
input_pass = input("Whats the password?\n>")

if input_pass == real_pass:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")



# Activity 2, electric boogaloo
# Create a five question quiz that prints your score at the emd
# Choose any five questions
# EZ

Q1 = input("Is Elden Ring the best game known to mankind? Yes or No?\n>")
