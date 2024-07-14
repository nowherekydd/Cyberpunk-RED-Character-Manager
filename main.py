import random
from wayneskill import skillDict

def debugmenu():
    print("Skill Dictionary:")
    for category, skills in skillDict.items():
        print(f"{category}:")
        for skill, description in skills.items():
            print(f"  {skill}: {description}")

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

def main():
    debug_choice = input("Print skillsheet for debugging? (Y/N) ").strip().lower()
    if debug_choice == 'y':
        debugmenu()

    chosen_category = prompt_user_for_category()
    chosen_skill = prompt_user_for_skill(chosen_category)
    
    # Retrieve skill modifier from skillDict
    if chosen_skill in skillDict[chosen_category]:
        skill_modifier = skillDict[chosen_category][chosen_skill]
    else:
        skill_modifier = 0  # Default modifier if not found

    roll, _, total = roll_skill(skill_modifier)
    
    print(f"Rolling for {chosen_skill} in category {chosen_category}...")
    print(f"Roll: {roll}")
    print(f"Skill Modifier: {skill_modifier}")
    print(f"Total: {total}")

if __name__ == "__main__":
    main()
