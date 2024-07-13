import random
import waynesheet

# Define function to roll a 10-sided die
def d10r():
    return random.randint(1, 10)

# Running loop
while True:
    doRoll = input("Do you want to test this program and roll 1d10? (Y/N): ")
    
    if doRoll.upper() == "Y":
        roll = d10r()
        print(f"Result of 1d10 roll: {roll}. {waynesheet.test}")
    elif doRoll.upper() == "N":
        print("Exiting program.")
        break
    else:
        print("Invalid input. Please enter Y or N.")