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
import starscore
import starskill
import asciiart
import txtfrm

# Basic char info.

charName = "Astarion Ancunin"
charHandle = "Starboy"
charRole = "Rockerboy"
roleAbility = "Charismatic Impact"

#####################################

# Define derived scores.
## HP = 10 + (5 * ((BODY+WILL)/2, round up))
## HUM = EMP * 10 - max is reduced by 2 per cyber

# HP
maxHP = 10 + (5 * math.ceil((starscore.bodyScore + starscore.willScore)/2))
sevWound = math.ceil(maxHP / 2)
deathSave = starscore.bodyScore

# Humanity [includes current EMP because based on that]
# Max HUM Penalty
cyberCount = 4
maxHUMPenalty = cyberCount * 2

maxHUM = (10 * starscore.maxempScore) - maxHUMPenalty
humLoss = 37 # Temp mathn't until I get around to it.
humScore = maxHUM - humLoss
empScore = math.floor(humScore / 10)

# Charsheet extras.

charHeader = f"{charName} aka " + txtfrm.bold(f"{charHandle}")

charhCenter = charHeader.center(85)

# Charsheet format here.

def charDisplay():
    asciiart.charsheetheader()
    asciiart.charsheetdiv()
    print(charhCenter)
    asciiart.charsheetdiv()
    txtfrm.linebreak()
    
# Prints out charsheet on run for debug/testing.

charDisplay()