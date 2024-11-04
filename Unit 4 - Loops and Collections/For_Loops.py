# For Loops
# This is a BIG deal
# For Loops allow the programmer to REPEAT, or what we call LOOP

# Write a program that prints the numbers 1 through 10
# Each on a new line

fav_foods = ["Eggs Bennies", "Fried Chickie", "Mac n Cheese"]

# for <var> in <list>

for i in range(90, 101):
    print(i)

for food in fav_foods:
    print(food)
    # Runs all of the lines inside the for loop
    # When it reaches the bottom of the list, it runs again
    # And moves on to the next item in the list
    # It ends when there's no list items left




for i in range(10, 0, -1): # START, STOP, STEP
    print(i)

# Sum of a list
numbers = [60, 70, 419, 421, 665]
sum = 0
for n in numbers:
    sum = sum + n
print(sum)

# Square of Each Number

ints = [3, 2, 5, 4, 1]
newlist = []

for i in ints:
    newlist.append(i*i)
print(newlist)

# Character Count

stringy = input("Please enter a string\n>")
numvowels = 0
for s in stringy:

    if s.lower() == ["a", "e", "i", "o", "u"]:
        numvowels = numvowels + 1

print(numvowels)

# Print Multiplication Table

try:
    multi = int(input("Gimme an int yo! swag!\n>"))
except:
    print("womp womp")

for i in range(0, multi+1):
    print(str(multi) + " x " + str(i) + " = " + str(multi * i))

# List of names
names = ["Peter", "John", "Paul", "Luke"]
for names in names:
    print("Hello, " + names + "!")