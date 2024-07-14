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

import random # For dice rolling
import asciiart # To print out relevant ASCII
import waynesheet # Character sheet.
from wayneskill import skillDict # For skill dictionary. Maybe find a way to make it more generic for future plugin?

def debugmenu():
    print("Skill Dictionary:")
    for category, skills in skillDict.items():
        print(f"{category}:")
        for skill, description in skills.items():
            print(f"  {skill}: {description}")
    input("Press Enter to continue...")

def prompt_user_for_category():
    print("Choose a category of skills:")
    categories = list(skillDict.keys())
    for i, category in enumerate(categories, start=1):
        print(f"{i}. {category}")

    choice = int(input("Enter the number of the category: "))
    chosen_category = categories[choice - 1]
    return chosen_category

def prompt_user_for_skill(category):
    print(f"Choose a skill from the category '{category}':")
    skill_list = list(skillDict[category].keys())
    for i, skill in enumerate(skill_list, start=1):
        print(f"{i}. {skill}")

    choice = int(input("Enter the number of the skill: "))
    chosen_skill = skill_list[choice - 1]
    return chosen_skill

def roll_skill(skill_modifier):
    roll = random.randint(1, 10)
    total = roll + skill_modifier
    return roll, skill_modifier, total

def skillroller():
    while True:
        chosen_category = prompt_user_for_category()
        chosen_skill = prompt_user_for_skill(chosen_category)
        if chosen_skill in skillDict[chosen_category]:
            skill_modifier = skillDict[chosen_category][chosen_skill]
        else:
            skill_modifier = 0

        while True:
            roll, _, total = roll_skill(skill_modifier)
            print(f"Rolling for {chosen_skill} in category {chosen_category}...")
            print(f"Roll: {roll}")
            print(f"Skill Modifier: {skill_modifier}")
            print(f"Total: {total}")
            next_action = input("Choose next action: Roll [a]gain for the same skill, [D]ifferent skill, or [M]ain menu: ").strip().upper()

            if next_action == "A":
                continue  # Roll again for the same skill
            elif next_action == "M":
                return  # Return to main menu
            elif next_action == "D":
                break  # Prompt for different skill
            else:
                print("Invalid choice. Returning to main menu...")
                return

def main_menu():
    print("\nMain Menu:")
    print("[R]oll for a Skill")
    print("[V]iew Character Sheet")
    print("[D]ebug Menu")
    print("[E]xit")
    choice = input("Enter your choice: ")
    return choice

def main():
    asciiart.mainheader()
    while True:
        choice = main_menu().upper()

        if choice == "E":
            print("Exiting program...")
            break
        elif choice == "R":
            skillroller()
        elif choice == "V":
            asciiart.charsheetheader()
            view_character_sheet()
            input("Press Enter to continue...")
        elif choice == "D":
            debugmenu()
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()