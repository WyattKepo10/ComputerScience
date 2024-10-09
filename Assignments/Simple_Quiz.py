# String functions
# String functions are a group of functions that modify string
# .lower()
# .lower() changes the string to be all lowercase
# .upper() changes  the sring to be uppercase

# .captialize() changes the entire string to lowercase, then captilizes the first letter
# "Hello World!" > "Hello world"

# .title() changes the entire string to a titlecase (Capital first letter on each word)
# "hello word" > "Hellow World"

# .swapcase() inverts the capitalization on each character
# "Hello World1" > "hELLO wORLD!"
print("Use no capitalization")
print("Use no capitalization")
print("Use no capitalization")
print("Use no capitalization")
Question_1 = input("Is Elden Ring the best game ever? Yes or No\n>")

Q2 = input("Is Mr. Ososwki the best techer in STMA High school? Yes or No\n>")

Q3 = input("What is 9 times 9 plus 3?\n>")
Q3= int(Q3)

Q4 = input("What year was the anime, Pokemon , released?\n>")

Q5 = input("How much wood could a woodchuck chuck If a woodchuck could chuck wood?")

def tally_score():
    score = 0
    if (Question_1 == "yes"):
        score = score = 1
    if (Q2=="yes"):
        score = score + 1
    if (Q3 == 84):
            score = score + 1
    if (Q4==1997):
                score = score + 1
    if (Q5 == "as much wood as a woodchuck could chuck if a woodchuck could chuck wood"):
        score = score + 1
    print("your score is " + str(score) + " out of 5")
                    
tally_score()