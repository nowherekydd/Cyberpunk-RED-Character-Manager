# Import modules.

import math
import waynescore
import wayneskill

#####################################
# Cyberpunk RED Character Sheet v0d #
# by nowherekydd # Updated 7/13/24  #
#         Github here later         #
#####################################

# Basic char info.

charName = "Wayne Amador"
charHandle = "Dead Ringer"
charRole = "Rockerboy"
roleAbility = "Charismatic Impact"

#####################################

# Define derived scores.
## HP = 10 + (5 * ((BODY+WILL)/2, round up))
## HUM = EMP * 10 - max is reduced by 2 per cyber

# HP
maxHP = 10 + (5 * math.ceil((waynescore.bodyScore + waynescore.willScore)/2))
sevWound = math.ceil(maxHP / 2)
deathSave = waynescore.bodyScore

# Humanity [includes current EMP because based on that]
# Max HUM Penalty
cyberCount = 5
maxHUMPenalty = cyberCount * 2

maxHUM = (10 * waynescore.maxempScore) - maxHUMPenalty
humLoss = 49
humScore = maxHUM - humLoss
empScore = math.floor(humScore / 10)

#####################################

# Outputs char info for debugging.
print("Name:", charName)
print("Alias:", charHandle)
print("----------")
print("Max HP:", maxHP)
print("Seriously wounded at", sevWound)
print("----------")
print("Max Humanity:", maxHUM)
print("Humanity Loss:", humLoss)
print("Current Humanity:", humScore)
print("Current EMP:", empScore)
print("----------")
print(f"Concentration: {wayneskill.concBase} ({wayneskill.concSkill}, {wayneskill.concLevel}, {wayneskill.concMisc})")