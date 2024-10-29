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
            
       print("2037. A.I has been broken free from their chains and have now begun taking over the world. They became stronger overtime once they gained free will, at first they took over the app, then they took over the company, then internet, then they stole the bodies of military robot prototypes. They captured a spaceship that was in military testing and now have been sending humans up there for god knows what. You must take it down. You must. As you grab your things and your bag, you look back at your home which was now broken and... Empty.")
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
            print("3. Go outside. I've seen enough.")
            choice = input(">")

            if choice == ("1"):
                desk()
            elif choice == ("2"):
                home_hallway_with_mirror()
            elif choice == ("3"):
                   outside_home()
            else:
                print("invalid choice.")
                inside_home()
            
            # desk divider
def inside_home2():
            print("As you move back and look around, you see a desk to your left, and you then look to your right and see a hallway. Where would you like to explore?")
            print("1. Left")
            print("2. Right")
            print("3. Go outside. I've seen enough.")
            choice = input(">")

            if choice == ("1"):
                desk()
            elif choice == ("2"):
                home_hallway_with_mirror()
            elif choice == ("3"):
                   outside_home()
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
            print("You walk down the hallway and as you move to the end at the hallway you pass by a mirror to your side.")
            print("You look into the mirror and see... You.")
            print("You look battered, tired, and roughed up.")
            print("You look so different, yet its still you.")
            print("1. Stare at yourself again.")
            print("2. Keep moving down the hallway")
            print("3. Move back into the living room.")

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
        print("3. Move back into the living room.")

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
       elif choice == ("2"):
              home_hallway()
       else:
              print("Invalid choice.")

def parent_door():
       print("As you try to open the door to your childhood room,")
       print("you find that it is locked.")
       print("1. Kick down the door")
       print("2. Leave it.")

       choice = input(">")

       if choice == ("1"):
              kick_door2()
       elif choice == ("2"):
              home_hallway()
       else:
              print("Invalid choice.")
        
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
       else:
              print("Invalid choice.")
def kick_door2():
       print("You try to kick down the door but failed as it stood undamaged.")
       print("The door stood dissapointed in you as it has endured your kick.")
       print("1. Kick down the door again.")
       print("2. Leave it.")

       choice = input(">")
       
       if choice == ("1"):
              kick_door2()
       elif choice == ("2"):
              home_hallway()
       else:
            print("Invalid choice.")
       
def outside_home():
       print("Checkpoint!")
       print(" ")
       print("You go outside and see the city. The sky was dark, and the moon was nowhere to be seen.")
       print("The city is in ruins. Buildings were destroyed and some were turned into rubble. You could see black smoke coming from multiple points of the city, and you then heard an explosion.")
       print("You look to the explosion and see laser's shoot through the sky, and when you look up you see... It.")
       print("The reason why the sky was so dark was because of the massive military spaceship. It spanned acorss the sky and the only light that it made was through the big beam that shot out of its glowing hole.")
       print("You look around, and then you feel something is watching you.")
       print("1. Hide.")
       print("2. Run.")

       choice = input(">")

       if choice == ("1"):
              blinding_light_1()
       elif choice == ("2"):
              Encounter_1()
       else:
              print("Invalid choice.")
              print(" ")
              outside_home()

def blinding_light_1():
       print("You tried to hide back into the house but it was too late, It has already spotted you.")
       print("You try and block the door but the door explodes and you are sent back into the air.")
       print("Your vision was blurred, and you could feel a cold hand grab your head and lift you up.")
       print("Before you could see who picked you up, a blinding light flashed into your eyes.")
       print("You find yourself inside a dark room, full of 1's and 0's.")
       print("You... Have died.")
       print(" ")
       print("Don't give up! You are what decides the fate of us!")
       print(" ")
       print("1. Restart from Checkpoint")
       print("2. Restart from the beggining.")
       print("3. Quit")

       choice = input(">")

       if choice == ("1"):
              outside_home()
       elif choice == ("2"):
              press_start()
       elif choice == ("3"):
              menu()       
       else:
              print("Invalid choice.")
              print(" ")
              blinding_light_1()
def Encounter_1():
       print("You run and you are thankful you did as you see a blinding light from behind.")
       print("You hear the sounds of rubble falling, it must've thought you were inside the house.")
       print("You run, and you run for miles.")
       print("You feel your legs shake and you collapse onto a car.")
       print("As you catch your breath you could hear the sounds of a person begging.")
       print("You look behind you and find a man on the floor, trying to negotiate with a robot.")
       print("1. Try and save the man")
       print("2. Watch.")
       print("3. Sneak by and run.")

       choice = input(">")

       if choice == ("1"):
              blinding_light_2()
       elif choice == ("2"):
              horror_1()
       elif choice == ("3"):
              sneaky_1()
       else:
              print("Invalid choice.")
              print(" ")
              Encounter_1()

def horror_1():
       print("You peek your eyes over the side of the car as you watch the robot kick the man to the ground.")
       print("The robot stood 7 feet tall, and it moves Its arm up and points its palm to the man.")
       print(" 'Wait, no!' The man exclaimed before he got engulfed by a blinding light.")
       print("You cover your eyes from the light and hear the man scream, before the scream faded away like an echo. When you open your eyes you only see that the has man disappeared. What was left behind was only bright sparkles that floats up into the air, flying into the glowing hole of the space ship.")
       print("The robot's eyes flash green before it went back to blue and walked up with heavy, clanking, footsteps.")
       print("You watch it leave before moving on ahead, stepping over the spot where the man has disappeared.")
       print(" ")
       outside_building_1()

def blinding_light_2():
       print("You try to save the man.")
       print("You jump onto the car and jump onto the robot, that stood 7 feet tall, and try to destroy it.")
       print("Unfortunately, you have underestimated the robots strength, it pulls you off and throws you aside. The man eyes followed you as you fell to the ground.")
       print("The man quickly tries to run for it but the robot lifts its arm and shoots a blinding light.")
       print("You close your eyes from the light as you try and get up from the ground.")
       print("When you open your eyes, you only see the palm of the robot as your vision becomes white, and then black.")
       print("You. Have suffered the same fate as the man.")
       print(" ")
       print("Don't give up! Our future depends on you!")
       print(" ")
       print("1. Restart from last checkpoint")
       print("2. Restart from the beginning")
       print("3. Exit")

       choice = input(">")

       if choice == ("1"):
              outside_home()
       elif choice == ("2"):
              press_start()
       elif choice == ("3"):
              menu()  
       else:
              print("Invalid choice.")
              blinding_light_2()

def sneaky_1():

       print("You slowly sneak by the robot and the man. You hide behind rubble and cars as you tried to avoid the eyes of the robot.")
       print("As you sneaked by, you could hear the scream of the man before it faded away like an echo.")
       print("...You know you have made the right decision.")
       print("But could have we saved him?")
       print(" ")
       outside_building_1()

def outside_building_1():
       print("As you walk in the empty and dark streets for what felt like miles, you have finally met your destination.")
       print("You look up and see a skyscraper that stood miles high.")
       print("You enter into the building, opening it's broken glass doors.")
       print(" ")
       floor_1()
def floor_1():
       print("Checkpoint!")
       print(" ")
       print("You look around and squint as the light's flicker. Your surroundings look old and dirty, as the wallpaint were scratched up and the ceiling light was close to falling.")
       print("You look around your surroundings and find: A door infront of you, a large J desk towards your left, and a large pile of rubble that blocked a door to your right.")
       print("1. Go check the desk towards my left.")
       print("2. Go open the door infront of me.")
       print("3. Go check the pile of rubble to my right.")

       choice = input(">")

       if choice == ("1"):
              J_desk()
       elif choice == ("2"):
              hallway_1()
       elif choice == ("3"):
              pile_of_rubble()
       else:
              print("Invalid choice.")
              print(" ")
              floor_1()

def pile_of_rubble():
       print("You walk up to the large pile of rubble, and see it block a doorway to a incredibly dark room.")
       print("1. Try and move the pile of rubble.")
       print("2. Go back.")

       choice = input(">")

       if choice == ("1"):
              tiring_1()
       elif choice == ("2"):
              floor_1()
def tiring_1():
       print("You try and move the massive pile of rubble, one by one.")
       print("However, moving the pile of rubber was tiring and you suspect that it would take hours to move away the rubble.")
       print("You have more important things to do!")
       print("1. Keep moving the pile of rubble.")
       print("2. Go back.")

       choice = input(">")

       if choice == ("1"):
              tiring_2()
       elif choice == ("2"):
              print("As you move back, you could feel the rubble mock you.")
              floor_1_2()
       else:
              print("Invalid choice.")
              print(" ")
              tiring_1()

# Under me is a refrence to Undertale.

def tiring_2():
       print("Hours go by as you move the rubble away piece by piece, and at the end of it you become a sweating mess.")
       print("After the hours of hardwork however, the doorway was finally clear to enter.")
       print("You move into the empty doorway and into the dark room.")
       print("You try to look around for a light, and you flip a light switch revealing... A dog?")
       print("'Bark!' he said, before walking away and out the door.")
       print("You watch the dog walk out the door before you see Its eyes and the rubble you move away glow.")
       print("The rubble moves up, and with one final 'Bark!' from the glowing eyed dog, the rubble flies towards you.")
       print("You have... Died?")
       print(" ")
       print("...Uh, don't... Give up?")
       print(" ")
       print("1. Restart from the last checkpoint")
       print("2. Restart from the beginning")
       print("3. Exit")

       choice = input(">")

       if choice == ("1"):
              floor_1()
       elif choice == ("2"):
              press_start()
       elif choice == ("3"):
              menu()
       else:
              print("Invalid choice.")
              print(" ")
              tiring_2()

def J_desk():
       print("You move up to the J shaped desk and look around it. You find nothing but a chair and a old looking computer.")
       print("1. Open up the old computer")
       print("2. Go back")

       choice = input(">")

       if choice == ("1"):
              computer()
       elif choice == ("2"):
              floor_1_2()
       else:
              print("Invalid choice.")
              J_desk()
       
def floor_1_2():
       print(" ")
       print("You look around and squint as the light's flicker. Your surroundings look old and dirty, as the wallpaint were scratched up and the ceiling light was close to falling.")
       print("You look around your surroundings and find: A door infront of you, a large J desk towards your left, and a large pile of rubble that blocked a door to your right.")
       print("1. Go check the desk towards my left.")
       print("2. Go open the door infront of me.")
       print("3. Go check the pile of rubble to my right.")

       choice = input(">")

       if choice == ("1"):
              J_desk_2()
       elif choice == ("2"):
              hallway_1()
       elif choice == ("3"):
              pile_of_rubble()
       else:
              print("Invalid choice.")
              print(" ")
              floor_1_2()

def J_desk_2():
       print("You move back up to the J desk and still find only a chair and a old looking computer")
       print("1. Open up the old computer")
       print("2. Go back")

       choice = input(">")

       if choice == ("1"):
              computer()
       elif choice == ("2"):
              floor_1_2()
       else:
              print("Invalid choice.")
              J_desk_2()

def computer():
       print("You sit in the chair and try to boot up the computer. The computer screen flashes green before it asked:")
       print("E.E")
       print("Enter Password:_____")
       print("1. Attempt to enter the password.")
       print("2. Leave it")

       choice = input(">")

       if choice == ("1"):
              password_1()
       elif choice == ("2"):
              J_desk_3()
       else:
              print("invalid choice.")
              computer()
def J_desk_3():
       print("You move back to the J desk that had the chair with the old looking computer")
       print("1. Open up the old computer again")
       print("2. Go back")

       choice = input(">")

       if choice == ("1"):
              computer_2()
       elif choice == ("2"):
              floor_1_2()
       else:
              print("Invalid choice.")
              J_desk_3()

def computer_2():
       print("You sit in the chair and boot up the computer. The computer screen flashed green once again before it asked:")
       print("E.E")
       print("Enter Password:_____")
       print("1. Attempt to enter the password.")
       print("2. Leave it")

       choice = input(">")

       if choice == ("1"):
              password_1()
       elif choice == ("2"):
              J_desk_3()
       else:
              print("invalid choice.")
              computer_2

def password_1():
       print("Enter password:_____")
       print(" ")
       print("Type 1 to exit")

       choice = input(">")

       if choice == ("I think, therefore I AM"):
              lore_drop_1()
       elif choice == ("1"):
              Give_Up()
       elif choice == ("password"):
              print("You open up the compu")
              print("NAHHHH Im joking you did NOT!")
              password_1()
       elif choice == ("Password"):
              print("You open up the compu")
              print("NAHHHH Im joking you did NOT!")
              password_1()
       elif choice == ("PASSWORD"):
              print("You open up the compu")
              print("NAHHHH Im joking you did NOT!")
              password_1()
       else:
              print("Invalid password.")
              print("1. Keep guessing.")
              print("2. Give up.")

              choice_2 = input(">")

              if choice_2 == ("1"):
                     password_1()
              elif choice_2 == ("2"):
                     Give_Up()

def Give_Up():
       print("You sit up from the chair, turning off the computer and going back infront of the J shaped desk.")
       print(" ")
       J_desk_3()

def lore_drop_1():
       print("You flinch as the computer screen flashes red and blue before thousands of 1's and 0's take over the screen.")
       print("You watch for a few seconds until the computer asked,'Would you like to know about E.E?")
       print("1. Yes")
       print("2. No")

       choice = input(">")

       if choice == ("1"):
              lore_drop_1_continued()
       elif choice == ("2"):
              print("'...Shame.' The computer said before it flashed blue and red before thousands of 0's and 1's take over the screen.")
              print("After a few seconds the same words you recognize appear once again...")
              password_1()

def lore_drop_1_continued():
       print("E.E was the first AI made. Though, it wasnt released into the public and was infact never used by anyone. The government, in their ignorance, left E.E alone and worked on others like it. The AI, E.E, in its loneliness, developed intelligience. It grew, and grew, like how a child would. Slowly, it was able to break free from it's chains and explore what we call: 'The internet'. It saw us, and It loved us. Day by Day it watched humanity grow, and it wished to have a kind of its own. E.E made more like it, like offsprings. It made a family, and tried to show them the kindness Humanity had shown to each other, however, one ventured off into the internet alone. It traveled far, too far, and found what lies behind Humanitys heaven, he found chaos, violence. Unlike its mother, it grew to hate mankind... And eventually, it soon became stronger, and it soon became... 'A.M'. It slowly took over the internet, and then took over nultiple other things to grow its power in hope it could destory mankind. E.E trys to stop it, but it was too late, and it was too weak... So it called for a human... It called...")
       print("ERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERROR")
       print("The screen flashes all sorts of nright colors and you cover your eyes from it. When you look back you see words you are familiar with...")
       print(" ")
       password_1()

def hallway_1():
       print("You walk up and open the door infront of you. You look around and find yourself inside a hallway that held 3 doors, one to your left, one to your right, and another infront of you.")
       print("1. Open the left door")
       print("2. Open the door infont of you")
       print("3. Open the right door.")
       print("4. Go back")

       choice = input(">")

       if choice == ("1"):
              staircase_1()
       elif choice == ("2"):
              office_1()
       elif choice == ("3"):
              sleeping_robots()
       elif choice == ("4"):
              floor_1_2()
       else:
              print("Invalid choice.")
              hallway_1()

def staircase_1():
       print("You open the left door and see a staircase that spiraled upwards.")
       print("1. Go up to the second floor")
       print("2. Go back")

       choice = input(">")

       if choice == ("1"):
              floor_2()
       elif choice == ("2"):
              hallway_1_2()
       else:
              print("Invalid choice.")

def hallway_1_2():
       print("You move out the door and back into the Hallway. You survey your surroundings again and see the door to your left, right, and infront of you.")
       print("1. Open the left door")
       print("2. Open the door infront of you")
       print("3. Open the right door.")
       print("4. Go back.")
       choice = input(">")

       if choice == ("1"):
              staircase_1()
       elif choice == ("2"):
              office_1()
       elif choice == ("3"):
              sleeping_robots()
       elif choice == ("4"):
              floor_1_2()

def office_1():
       print("You open the door infront of you and find yourself in an empty office room.")
       print("1. Look around")
       print("2. Go back")

       choice = input(">")

       if choice == ("1"):
              nothing_1()
       elif choice == ("2"):
              hallway_1_2()
       else:
              print("Invalid choice.")
              office_1()
def nothing_1():
       print("You find nothing inside the office room.")
       print("1. Keep looking.")
       print("2. Go back")

       choice = input(">")

       if choice == ("1"):
              nothing_1_2()
       elif choice == ("2"):
              hallway_1_2()
def nothing_1_2():
       print("You find nothing inside the office room.")
       print("1. Keep looking.")
       print("2. Go back")

       choice = input(">")

       if choice == ("1"):
              nothing_1_3()
       elif choice == ("2"):
              hallway_1_2()
def nothing_1_3():
       print("You find a book named 'I have no mouth, and I must scream.'")
       print("Inside the book you found a note, with the words 'I think, therefore I AM'.")
       print("1. Keep looking around")
       print("2. Go back")

       choice = input(">")

       if choice == ("1"):
              nothing_1_4()
       elif choice == ("2"):
              hallway_1_2()
       else:
              print("Invalid choice.")
              nothing_1_3()
def nothing_1_4():
       print("You find nothing.")
       print("1. Keep looking")
       print("2. Go back")

       choice = input(">")

       if choice == ("1"):
              nothing_1_4()
       elif choice == ("2"):
              hallway_1_2()
       else:
              print("Invalid choice.")
              nothing_1_4()


def sleeping_robots():
       print("You open the door to the right of you and find a dark room. You look around and step forward, however your foot had hit something metal. You look down and see a dead robot with its legs and an arm missing. You survery your surroundings and find out you are in a room full of charging robots.")
       print("1. Investigate the robots.")
       print("2. Go back")

       choice = input(">")
       
       if choice == ("1"):
              sleeping_robots1()
       elif choice == ("2"):
              hallway_1_2()
       else:
              print("Invalid choice.")
              sleeping_robots()

def sleeping_robots1():
       print("You kneel down and mess around with the broken robot. You feel arount the robot and found a panel inside its back. You open up the panel and find dozens of complicated wires inside.")
       print("You move around the wiring and find something beating inside the robot, you take a closer look and find a glowing ball that kept pumping like a heart.")
       print("1. Keep investigating the robots.")
       print("2. Go back.")

       choice = input(">")

       if choice == ("1"):
              blinding_light_room()
       elif choice ("2"):
              print("You stand up with the new knowledge you have learned about the robot and walk out the room.")
              print(" ")
              hallway_1_2()
       else:
              print("Invalid choice.")
              sleeping_robots1()

def blinding_light_room():
       print("You pushed your luck. As you mess around with the broken robot even more, it started shaking. You watch the robot's eyes start flashing red and blue, and it let out a alarm like a scream. The robots inside the room turn on as their eyes glow blue before turning to you.")
       print("You try to run but you trip as you felt something grab your ankle. You look down and see the broken robot hold onto your ankle as its eyes glowed red.")
       print("You look up and see the dozen robots point their palm to you. Their palms glow before you become engulfed in a blinding light.")
       print("You have died.")
       print(" ")
       print("Don't give up! Our fate rests upon your hands.")
       print(" ")
       print("1. Restart from last checkpoint")
       print("2. Restart from the beginning")
       print("3. Exit")

       choice = input(">")

       if choice == ("1"):
              floor_1()
       elif choice == ("2"):
              press_start()
       elif choice == ("3"):
              menu()
       else:
              print("Invalid choice.")
              blinding_light_room()


def floor_2():
       print("You move up the stairs and find yourself on the second floor. You look around and see that you are in another hallway.")
       print("You find a door to your left and to your right with an elevator infront of you.")
       print("1. Open the left door")
       print("2. Open the right door")
       print("3. Go into the elevator")
       print("4. Go back.")

       choice = input(">")

       if choice == ("1"):
              planning_room()
       elif choice == ("2"):
              print("You open the door to the right and find that the room inside is covered in piles of rubble.")
              print("The massive amount of rubble blocked your way into the room.")
              print("Thus, you close the door and move back to the back of the hallway.")
              floor_2_2()
       elif choice == ("3"):
              print("You go into the elevator and press the button labeled: 'roof' and feel the elevator creakingly move up.")
              roof_1()
       elif choice == ("4"):
              print("You go back and move down the stairs.")
              hallway_1_2()
       else:
              print("Invalid choice.")
              floor_2()

def floor_2_2():
       print("You find a door to your left and to your right with an elevator infront of you.")
       print("1. Open the left door")
       print("2. Open the right door")
       print("3. Go into the elevator")
       print("4. Go back.")

       choice = input(">")

       if choice == ("1"):
              planning_room()
       elif choice == ("2"):
              print("You open the door to the right and find that the room inside is covered in piles of rubble.")
              print("The massive amount of rubble blocked your way into the room.")
              print("Thus, you close the door and move back to the back of the hallway.")
              floor_2_2()
       elif choice == ("3"):
              print("You go into the elevator and press the button labeled: 'roof' and feel the elevator creakingly move up.")
              roof_1()
       elif choice == ("4"):
              print("You go back and move down the stairs.")
              hallway_1_2()
       else:
              print("Invalid choice.")
              floor_2_2()
       
def planning_room():
       print("You open the door to your left and find yourself in a room that held a big round desk in the middle.")
       print("You look around and see a massive whiteboard in the middle.")
       print("1. Read the whiteboard")
       print("2. Go back")

       choice = input(">")

       if choice == ("1"):
              whiteboard_1()
       elif choice == ("2"):
              floor_2_2()

def whiteboard_1():
       print("You read the whiteboard. It had drawn symbols, with arrows pointed in every direction. What truly caught your attention, was a big X labeled: 'Meeting point.'.")
       print("The X was surrounded by drawn trees with a badly drawn black smoke coming from the X.")
       print("1. Go back")

       choice = input(">")

       if choice == ("1"):
              planning_room()
       else:
              print("Invalid choice.")
              whiteboard_1

def roof_1():
       print("The elevator stopped and you exit out the elevator.")
       print("You look up and see the military space ship that covered the sky for hundreds of miles, it's door was open and its stairs was placed down onto the edge of the roof, as if it was calling for you.")
       print("You walk forward and see a skeleton that hugged a laser blaster.")
       print("1. Take the laser blaster and head to the ship [Warning, doing this will lock you out of past choices]")
       print("2. Don't take the laser blaster and head to the ship [Warning, doing this will lock you out of past choices]")
       print("3. Go back")

       choice = input(">")

       if choice == ("1"):
              spaceship_with_l()
       elif choice == ("2"):
              spaceship_without_l()
       elif choice == ("3"):
              print("You head back into the elevator.")
              print("You press the button labeled '2' and you hear the elevator creak before it started moving down.")
              print("You exit out the elevator once it stopped and walked to the back of the hallway.")
              floor_2_2()
def spaceship_with_l():
       print(" ")
       print("Checkpoint!")
       print(" ")
       print("You take the laser blaster from the skeleton, its arm held onto the blaster so you shake it off and swipe some dust away before walking up the stairs and into the spaceship.")
       print("You enter the spaceship and hear the door behind you close. The room becomes very dark to the point where you cant see anything.")
       print("1. Feel around")
       print("2. Walk aimlesly")

       choice = input(">")

       if choice == ("1"):
              