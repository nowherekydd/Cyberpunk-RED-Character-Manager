#   _____ _____   _____ _      _____ 
#  / ____|  __ \ / ____| |    |_   _|
# | |    | |__) | |    | |      | |  
# | |    |  _  /| |    | |      | |  
# | |____| | \ \| |____| |____ _| |_ 
#  \_____|_|  \_\\_____|______|_____|
#
# Cyberpunk: RED CLI Character Manager
# by nowherekydd // v0d
# Character Sheet

# Import modules.

import math
import waynescore
import wayneskill

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

# Charsheet format here.

def charDisplay:
    print("Test successful.")