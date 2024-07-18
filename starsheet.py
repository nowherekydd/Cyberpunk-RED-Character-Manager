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
import starscore
import starskill
import asciiart
import txtfrm

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


width = get_terminal_width()

nbsp = "\u00A0"

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

# Charsheet funsies.

charSPACE = txtfrm.rollerheader(center_text(nbsp, 42))
charEND = txtfrm.rollerheader(center_text(nbsp, 43))
charINT = txtfrm.rollermenu(txtfrm.bold(center_text(f"{starscore.ntlScore}", 3))) + txtfrm.rollermenu(center_text("INT //", 6))
charREF = txtfrm.rollermenu(txtfrm.bold(center_text(f"{starscore.refScore}", 3))) + txtfrm.rollermenu(center_text("REF //", 6))
charDEX = txtfrm.rollermenu(txtfrm.bold(center_text(f"{starscore.dexScore}", 3))) + txtfrm.rollermenu(center_text("DEX //", 6))
charTECH = txtfrm.rollermenu(txtfrm.bold(center_text(f"{starscore.techScore}", 3))) + txtfrm.rollermenu(center_text("TECH //", 7))
charCOOL = txtfrm.rollermenu(txtfrm.bold(center_text(f"{starscore.coolScore}", 3))) + txtfrm.rollermenu(center_text("COOL //", 7))
charWILL = txtfrm.rollermenu(txtfrm.bold(center_text(f"{starscore.willScore}", 3))) + txtfrm.rollermenu(center_text("WILL //", 7))
charMOVE = txtfrm.rollermenu(txtfrm.bold(center_text(f"{starscore.moveScore}", 3))) + txtfrm.rollermenu(center_text("MOVE //", 7))
charBODY = txtfrm.rollermenu(txtfrm.bold(center_text(f"{starscore.bodyScore}", 3))) + txtfrm.rollermenu(center_text("BODY //", 7))
charEMP = txtfrm.rollermenu(txtfrm.bold(center_text(f"{starscore.empScore}", 3))) + txtfrm.rollermenu(center_text(f"/ {starscore.maxempScore}", 4)) + txtfrm.rollermenu(center_text("EMP //", 7))
charLUCK = txtfrm.rollermenu(txtfrm.bold(center_text(f"{starscore.luckScore}", 3))) + txtfrm.rollermenu(center_text(f"/ {starscore.maxluckScore}", 4)) + txtfrm.rollermenu(center_text("LUCK", 7))

def charHead():
    width = get_terminal_width()
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
# charDisplay()