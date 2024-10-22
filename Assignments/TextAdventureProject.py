# Sci fi text adventure project
# FYI I COULDVE MADE SOMETHING BETTER BUT I MUST LIMIT MYSELF FOR THE E RATING


c = choice = input(">")
invalid = print("Invalid choice.")

def menu():
    print("E.E")
    print(" ")
    print("1. Start")
    print("2. Exit")
    
    choice = input(">")

    if choice == ("1"):
        press_start()
    elif choice == ("2"):
        exited_program()
    else:
        print("Invalid choice.")
        menu()

def exited_program():
    print("You have exited E.E")
    print("Would you like to re-enter E.E?")
    print("1. Yes")
    print("2. No")
    
    choice = input(">")

    if choice == ("1"):
        menu()
    elif choice == ("2"):
       print("ERROR")
       print("ERROR")
       print("ERROR")
       print("ERROR")
       print("ERROR")
       print("ERROR")
       print("ERROR")
       print("ERROR")
       print("ERROR")
       print("ERROR")
       print("ERROR")
       print("ERROR")
       print("ERROR")
       print("ERROR")
       print("ERROR")
       print("ERROR")
       print("ERROR")
       print("ERROR")
       menu()
    else:
        print("Invalid choice, try again.")
        exited_program()

def press_start(): 
    print("2099. A.I has been broken free from their chains and have now begun taking over the world. They captured a spaceship that was in military testing and now have been sending humans up there for god knows what. You must take it down. You must. As you grab your things and your bag, you look back at your home which was now broken and... Empty.")
    print("Would you like to take a look around your house... One final time?")
    print("1. No, I don't have enough time.")
    print("2. Yes, I would like to look through the memories of my childhood one last time.")

    choice = input(">")

    if choice == ("1"):
        outside_home()
    elif choice == ("2"):
        inside_home()
    else:
        press_start()
# Inside home divider

def inside_home():
    print("As you look inside your home, you look to your left and see a desk, you look to your right and see a hallway, and when you looked towards the front you see a kitchen. Where would you like to explore?")
    print("1. Left")
    print("2. Right")
    print("3. Forward")
    choice = input(">")

    if choice == ("1"):
        desk()
    elif choice == ("2"):
        home_hallway()
    elif choice == ("3"):
        home_kitchen()
    else:
        print("invalid choice.")
        inside_home()
    
    # desk divider
def inside_home2():
    print("As you move back and look around, you see a desk to your left, you then look to your right and see a hallway, and when you looked towards the front you see a kitchen. Where would you like to explore?")
    print("1. Left")
    print("2. Right")
    print("3. Forward")
    choice = input(">")

    if choice == ("1"):
        desk()
    elif choice == ("2"):
        home_hallway()
    elif choice == ("3"):
        home_kitchen()
    else:
        print("Invalid choice.")


def desk():
    print("As you move up to the desk to your left, you spot a picture frame sitting ontop of the desk.")
    print("You pick it up and see a photo of your family, back before the AI takeover.")
    print("You all were so... Happy.")
    print("You gain a even bigger resentment against robots.")
    print("You have finished looking at the desk.")
    print("1. Look at it again.")
    print("2. Go back.")

    choice = input(">")

    if choice == ("1"):
        desk2()
    elif choice == ("2"):
        inside_home2()
    else:
        print("Invalid choice.")
        desk()

def desk2():
    print("As you look at your desk again, you open it and find nothing.")
    print("How unfortunate.")
    print("1. Look at it.. Again.")
    print("2. Go back")

    choice = input(">")

    if choice == ("1"):
        desk3()
    elif choice == ("2"):
        inside_home2()
    else:
        print("Invalid choice.")
        desk2()

def desk3():
    print("You find nothing.")
    print("1. Look again")
    print("2. Go back")

    choice = input(">")

    if choice == ("1"):
        desk3()
    elif choice == ("2"):
        inside_home2()

# Divider

def home_hallway():

def home_kitchen():

menu()