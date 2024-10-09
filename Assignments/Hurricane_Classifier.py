hurricane_mph = input("Enter in a a hurricanes wind speed in MPH and I will tell you it's category,\n>")
hurricane_mph = int(hurricane_mph)
if hurricane_mph < 74:
    print("It is Tropical Storm")
elif hurricane_mph < 96:
    print("It is a Category 1 Hurricane.")
elif hurricane_mph < 111:
    print("It is a Category 2 Hurricane.")
elif hurricane_mph < 130:
    print("It is a Category 3 Hurricane.")

elif hurricane_mph < 157: 
    print("IT is a Category 4 Hurricane.")

elif hurricane_mph >= 157:
    print("It is a Category 5 Hurricane.")
else:
    print("Unindentified.")
    