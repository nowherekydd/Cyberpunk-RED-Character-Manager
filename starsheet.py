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
import os
import starskill
import asciiart
import txtfrm

#################################################################################################
# Here is where you would put in your character's information. I haven't tested this with any   #
# character other than Starboy, so if something breaks... gods help us all.                     #
#################################################################################################

################# BASIC INFORMATION ####################

charName = "Astarion Ancunin"
charHandle = "Starboy"
charRole = "Rockerboy"
roleAbility = "Charismatic Impact"

########################################################

################# CHARACTER SCORES #####################

ntlScore = 5
refScore = 7
dexScore = 6
techScore = 6
coolScore = 8
willScore = 8
moveScore = 5
bodyScore = 5
maxempScore = 7
maxluckScore = 5

########################################################

################# DERIVED SCORES #######################
## HP = 10 + (5 * ((BODY+WILL)/2, round up))
maxHP = 10 + (5 * math.ceil((bodyScore + willScore)/2))
sevWound = math.ceil(maxHP / 2)
deathSave = bodyScore

# Max Luck
luckScore = maxluckScore - 0

# HUM = EMP * 10 - max is reduced by 2 per cyber. Some values are manual at this time.
cyberCount = 4
maxHUMPenalty = cyberCount * 2
maxHUM = (10 * maxempScore) - maxHUMPenalty
humLoss = 37 # Temp mathn't until I get around to it.
humScore = maxHUM - humLoss
empScore = math.floor(humScore / 10)

#################################################################################################
# Formatting beyond this point. It's not rec'd that you edit anything pas there. If you do, you #
# do so at your own risk.                                                                       #
#################################################################################################

# Clears console
clear = lambda: print("\033c", end="", flush=True)

# Grabs terminal width
def get_terminal_width():
    try:
        return os.get_terminal_size().columns
    except OSError:
        # Default to 80 if getting terminal size fails
        return 80

def center_text(text, width):
    # Center the text and fill the remaining space with non-breaking spaces
    padding = (width - len(text)) // 2
    centered_text = " " * padding + text + " " * padding
    # Ensure the length matches the terminal width
    if len(centered_text) < width:
        centered_text += " " * (width - len(centered_text))
    return centered_text


width = get_terminal_width() # Centering operator

nbsp = "\u00A0" # Spacer

# Defines score display so that charScores isn't ball-bustingly long

charSPACE = txtfrm.rollerheader(center_text(nbsp, 42))
charEND = txtfrm.rollerheader(center_text(nbsp, 43))
charINT = txtfrm.rollermenu(txtfrm.bold(center_text(f"{ntlScore}", 3))) + txtfrm.rollermenu(center_text("INT //", 6))
charREF = txtfrm.rollermenu(txtfrm.bold(center_text(f"{refScore}", 3))) + txtfrm.rollermenu(center_text("REF //", 6))
charDEX = txtfrm.rollermenu(txtfrm.bold(center_text(f"{dexScore}", 3))) + txtfrm.rollermenu(center_text("DEX //", 6))
charTECH = txtfrm.rollermenu(txtfrm.bold(center_text(f"{techScore}", 3))) + txtfrm.rollermenu(center_text("TECH //", 7))
charCOOL = txtfrm.rollermenu(txtfrm.bold(center_text(f"{coolScore}", 3))) + txtfrm.rollermenu(center_text("COOL //", 7))
charWILL = txtfrm.rollermenu(txtfrm.bold(center_text(f"{willScore}", 3))) + txtfrm.rollermenu(center_text("WILL //", 7))
charMOVE = txtfrm.rollermenu(txtfrm.bold(center_text(f"{moveScore}", 3))) + txtfrm.rollermenu(center_text("MOVE //", 7))
charBODY = txtfrm.rollermenu(txtfrm.bold(center_text(f"{bodyScore}", 3))) + txtfrm.rollermenu(center_text("BODY //", 7))
charEMP = txtfrm.rollermenu(txtfrm.bold(center_text(f"{empScore}", 3))) + txtfrm.rollermenu(center_text(f"/ {maxempScore}", 4)) + txtfrm.rollermenu(center_text("EMP //", 7))
charLUCK = txtfrm.rollermenu(txtfrm.bold(center_text(f"{luckScore}", 3))) + txtfrm.rollermenu(center_text(f"/ {maxluckScore}", 4)) + txtfrm.rollermenu(center_text("LUCK", 7))

def charHead():
    print(txtfrm.rollermenu(center_text(f"{charName} aka", width)))
    print(txtfrm.bold(txtfrm.rollermenu(center_text(charHandle, width))))

def charScores():
    print(charSPACE + charINT + charREF + charDEX + charTECH + charCOOL + charWILL + charMOVE + charBODY + charEMP + charLUCK + charEND)

# Testing

# Charsheet format here.

def charDisplay():
    clear()
    asciiart.charsheetheader()
    charHead()
    asciiart.headerDiv()
    charScores()
    asciiart.headerDiv()

    
# Prints out charsheet on run for debug/testing. Comment out when not in use.
charDisplay()