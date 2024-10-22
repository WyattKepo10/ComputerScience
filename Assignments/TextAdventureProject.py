# Sci fi text adventure project
# FYI I COULDVE MADE SOMETHING BETTER BUT I MUST LIMIT MYSELF FOR THE E RATING

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
                print(" ")
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
                print("Invalid choice.")
                press_start()
        # Inside home divider

def inside_home():
            print("As you look inside your home, you look to your left and see a desk, and you then look to your right and see a hallway.. Where would you like to explore?")
            print("1. Left")
            print("2. Right")
            choice = input(">")

            if choice == ("1"):
                desk()
            elif choice == ("2"):
                home_hallway()
            else:
                print("invalid choice.")
                inside_home()
            
            # desk divider
def inside_home2():
            print("As you move back and look around, you see a desk to your left, and you then look to your right and see a hallway. Where would you like to explore?")
            print("1. Left")
            print("2. Right")
            choice = input(">")

            if choice == ("1"):
                desk()
            elif choice == ("2"):
                home_hallway()
            else:
                print("Invalid choice.")
                inside_home2()


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
            else:
                  print("Invalid choice.")
                  desk3()
                

        # Home Hallway Divider

def home_hallway_with_mirror():
            print("You walk down the hallway to your right and as you move to the end at the hallway you pass by a mirror.")
            print("You look into the mirror and see... You.")
            print("You look battered, tired, and roughed up.")
            print("You look so different, yet its still you.")
            print("1. Stare at yourself again.")
            print("2. Keep moving down the hallway")
            print("3. Go back.")

            choice = input(">")

            if choice == ("1"):
                  home_hallway_with_mirror2()
            elif choice == ("2"):
                  home_hallway()
            elif choice == ("3"):
                  inside_home2()
            else:
                   print("Invalid choice.")
                   home_hallway_with_mirror()
# divider
def home_hallway_with_mirror2():
        print("You look into the mirror and see... You.")
        print("You look battered, tired, and roughed up.")
        print("You look so different, yet its still you.")
        print("1. Stare at yourself again.")
        print("2. Keep moving down the hallway")
        print("3. Go back.")

        choice = input(">")

        if choice == ("1"):
                  home_hallway_with_mirror2()
        elif choice == ("2"):
                  home_hallway()
        elif choice == ("3"):
                  inside_home2()
        else:
               print("Invalid choice.")
               home_hallway_with_mirror2
# divider

def home_hallway():
    print("You keep moving the down the hallway and find yourself in between two doors.")
    print("You look to your left and see the closed door that belongs to your childhood room.")
    print("You then look to your right and find the closed door that belongs to your parents room.")
    print("1. Open the door to your childhood room.")
    print("2. Open the door to your parents room.")
    print("3. Go back")

    choice = input(">")

    if choice == ("1"):
           childhood_door()
    elif choice == ("2"):
           parent_door()
    elif choice == ("3"):
           home_hallway_with_mirror()
def childhood_door():
       print("As you try to open the door to your childhood room,")
       print("you find that it is locked.")
       print("1. Kick down the door")
       print("2. Leave it.")

       choice = input(">")

       if choice == ("1"):
              kick_door1()
       if choice == ("2"):
              home_hallway()

def parent_door():
       print("As you try to open the door to your childhood room,")
       print("you find that it is locked.")
       print("1. Kick down the door")
       print("2. Leave it.")

       choice = input(">")

       if choice == ("1"):
              kick_door2()
       if choice == ("2"):
              home_hallway()
        
def kick_door1():
       print("You try to kick down the door but failed as it stood undamaged.")
       print("The door stands proud as it has endured your kick.")
       print("1. Kick down the door again.")
       print("2. Leave it")

       choice = input(">")
       
       if choice == ("1"):
              kick_door1()
       elif choice == ("2"):
              home_hallway()
def kick_door2():
       print("You try to kick down the door but failed as it stood undamaged.")
       print("The door stood dissapointed in you as it has endured your kick.")
       print("1. Kick down the door again.")
       print("2. Leave it.")

       choice = input(">")
       
       if choice == ("1"):
              kick_door2()
       if choice == ("2"):
              home_hallway()
       


       


menu()
