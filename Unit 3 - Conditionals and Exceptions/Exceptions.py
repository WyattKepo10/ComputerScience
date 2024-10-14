# Exception Handling
# Write a program that asks for two numbers and divides them.

# Exception means handling the unexpected.

# if    =   try    = this could fail
# elif  =    except with error type
# else  =   except
def divide_two_numbers():
    try:    # We always enter the try block, there is no condition.
        x = int(input("What is the first number?\n>"))
        y = int(input("What is the second number?\n>"))
        print(x / y)

    except ZeroDivisionError:
        print("CANNOT DIVIDE BY ZERO, TRY AGAIN.")
        divide_two_numbers()

    except ValueError:
        print("PLEASE ENTER A VALID NUMBERICAL SYMBOL, TRY AGAIN.")
        divide_two_numbers()

    except:     # If anything in the try block causes an error, 
                # The try block stops immediately, and the except is ran instead.
                # The rest of the try block nevr finishes running, its skipped,
                # If the try block executes without an error, the except is skipped,
                # The only way to get into the except, is to "throw" an error.
        print("INVALID INPUT, TRY AGAIN.")
        divide_two_numbers()    # Tells the functiont to run again.

divide_two_numbers()
