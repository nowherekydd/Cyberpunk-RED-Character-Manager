#   _____ _____   _____ _      _____ 
#  / ____|  __ \ / ____| |    |_   _|
# | |    | |__) | |    | |      | |  
# | |    |  _  /| |    | |      | |  
# | |____| | \ \| |____| |____ _| |_ 
#  \_____|_|  \_\\_____|______|_____|
#
# Cyberpunk: RED CLI Character Manager
# by nowherekydd // v0d
# Main Program

################### Non-Custom Modules #######################
import random # For dice rolling
import time # For time delay between end and console clearing
import os # To get console width
##############################################################
import asciiart # To print out relevant ASCII
import starsheet # Character sheet
import txtfrm # Because I'm a fucking idiot and forgot this
##############################################################

# Clears console
clear = lambda: print("\033c", end="", flush=True)

# Grabs terminal width
def get_terminal_width():
    try:
        return os.get_terminal_size().columns
    except OSError:
        # Default to 80 if getting terminal size fails
        return 80

# Defines invalid choice. Note - does not include returning to main. Keep that in the menu thing.

def invalid():
    width = get_terminal_width()
    clear()
    asciiart.headerDiv()
    print(txtfrm.rollermenu(center_text("Invalid choice. Returning to main menu in 3...", width)))
    asciiart.headerDiv()
    time.sleep(1)
    clear()
    asciiart.headerDiv()
    print(txtfrm.rollermenu(center_text("Invalid choice. Returning to main menu in 2...", width)))
    asciiart.headerDiv()
    time.sleep(1)
    clear()
    asciiart.headerDiv()
    print(txtfrm.rollermenu(center_text("Invalid choice. Returning to main menu in 1...", width)))
    asciiart.headerDiv()
    time.sleep(1)

# Defines end prog

def endprog():
    width = get_terminal_width()
    clear()
    asciiart.headerDiv()
    print(txtfrm.rollermenu(center_text("Exiting program in 3...", width)))
    asciiart.headerDiv()
    time.sleep(1)
    clear()
    asciiart.headerDiv()
    print(txtfrm.rollermenu(center_text("Exiting program in 2...", width)))
    asciiart.headerDiv()
    time.sleep(1)
    clear()
    asciiart.headerDiv()
    print(txtfrm.rollermenu(center_text("Exiting program in 1...", width)))
    asciiart.headerDiv()
    time.sleep(1)
    clear()

# Centers text

def center_text(text, width):
    return text.center(width)

# Menu McMenuface

def debugmenu():
    clear()
    print("Skill Dictionary:")
    for category, skills in starsheet.skillDict.items():
        print(f"{category}:")
        for skill, description in skills.items():
            print(f"  {skill}: {description}")
    input("Press Enter to continue...")

def prompt_user_for_category():
    width = get_terminal_width()
    clear()
    categories = list(starsheet.skillDict.keys())

    asciiart.headerDiv()
    print(txtfrm.rollermenu(center_text(f"Choose a category.", width)))
    asciiart.headerDiv()

    for i, category in enumerate(categories, start=1):
        print(txtfrm.rollermenu(center_text(f"{i}. {category}", width)))

    asciiart.headerDiv()

    choice = int(input())

def prompt_user_for_skill(category):
    clear()
    width = get_terminal_width()
    asciiart.headerDiv()
    print(txtfrm.rollermenu(center_text(f"Choose a skill from {category}.", width)))
    asciiart.headerDiv()
    skill_list = list(starsheet.skillDict[category].keys())
    for i, skill in enumerate(skill_list, start=1):
        print(txtfrm.rollermenu(center_text(f"{i}. {skill}", width)))
    

    asciiart.headerDiv()

    choice = int(input())

def roll_skill(skill_modifier):
    roll = random.randint(1, 10)
    total = roll + skill_modifier
    return roll, skill_modifier, total

def skillroller():
    while True:
        width = get_terminal_width()
        chosen_category = prompt_user_for_category()
        chosen_skill = prompt_user_for_skill(chosen_category)
        if chosen_skill in starsheet.skillDict[chosen_category]:
            skill_modifier = starsheet.skillDict[chosen_category][chosen_skill]
        else:
            skill_modifier = 0

        rerollCount = 0
        
        while True:
            roll, _, total = roll_skill(skill_modifier)

            rollResult = [
                f"Rolling for {chosen_skill} in category {chosen_category}...",
                f"Roll: {roll}",
                f"Skill Modifier: {skill_modifier}",
            ]

            clear()
            asciiart.headerDiv()

            for line in rollResult:
                print(txtfrm.rollermenu(center_text(line, width)))
                asciiart.headerDiv()
            
            print(txtfrm.rollermenu(txtfrm.bold(center_text(f"Total: {total}", width))))
            asciiart.headerDiv()

            print(txtfrm.rollermenu(center_text(f"Choose next action: Roll [a]gain for the same skill (rerolled {rerollCount} time(s)), [D]ifferent skill, or [M]ain menu", width)))

            asciiart.headerDiv()

            nextAction = input().strip().upper()

            if nextAction == "A":
                rerollCount += 1
                continue  # Roll again for the same skill
            elif nextAction == "M":
                return  # Return to main menu
            elif nextAction == "D":
                break  # Prompt for different skill
            else:
                invalid()
                return

def main_menu():
    width = get_terminal_width()

    print(txtfrm.rollermenu(center_text("Main Menu:", width)))
    print(txtfrm.rollermenu(center_text(r"[R]oll for a Skill // [V]iew Character Sheet // [D]ebug // [E]xit", width)))
    asciiart.headerDiv()
    print(txtfrm.rollermenu(center_text("Enter your choice below.", width)))
    asciiart.headerDiv()

    choice = input()

    return choice

def main():
    while True:
        clear()
        asciiart.mainHeader()
        choice = main_menu().upper()

        if choice == "E":
            endprog()
            break
        elif choice == "R":
            clear()
            skillroller()
        elif choice == "V":
            width = get_terminal_width()
            clear()
            starsheet.charDisplay()
            print(txtfrm.rollermenu(center_text("Press Enter to return to the main menu...", width)))
            asciiart.headerDiv()
            input()
            clear()
        elif choice == "D":
            clear()
            debugmenu()
        else:
            invalid()
            continue

if __name__ == "__main__":
    main()