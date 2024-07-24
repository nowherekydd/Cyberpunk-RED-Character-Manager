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

########################################################

###################### SKILLS ##########################

## Multi-Option Skills
## (Skills that can be bought more than 1x and must be
## specialized each time)
##
## If you're adding more of these (languages, for ex.),
## don't forget to copy both the skill block here and
## in the skill math block below. You'll see what I
## mean. If your PC doesn't have one of these skills,
## just put null in that skill. You'll see what I mean.

### Language A
langLevelA = 2
langMiscA = 0
langTypeA = "Streetslang"
### Language B
langLevelB = 4
langMiscB = 0
langTypeB = "English"

### Local Expert A
localLevelA = 4
localMiscA = 0
localTypeA = "University District"

### Science
sciLevelA = 0
sciMiscA = 0
sciTypeA = "null"

### Martial Arts
martialLevelA = 0
martialMiscA = 0
martialTypeA = "null"

## Play Instrument
playLevelA = 0
playMiscA = 0
playTypeA = "null"

########################################################

## Awareness
### Concentration
concLevel = 2
concMisc = 0
### Conceal/Reveal Object
conrevLevel = 3
conrevMisc = 0
### Lip Reading
lipLevel = 2
lipMisc = 0
### Perception
percLevel = 2
percMisc = 0
### Tracking
trackLevel = 0
trackMisc = 0

## Body
### Athletics
athLevel = 2
athMisc = 0
### Contortionist
contLevel = 0
contMisc = 0
### Dance
danceLevel = 0
danceMisc = 0
### Endurance
endLevel = 2
endMisc = 0
### Resist Torture/Drugs
resistLevel = 6
resistMisc = 2
### Stealth
sneakLevel = 4
sneakMisc = 0

## Control
### Land Vehicle
landLevel = 0
landMisc = 0
### Air Vehicle
airLevel = 0
airMisc = 0
### Sea Vehicle
seaLevel = 0
seaMisc = 0
### Animal Vehicle
rideLevel = 0
rideMisc = 0

## Education
### Accounting
accLevel = 0
accMisc = 0
### Animal Handling
animLevel = 0
animMisc = 0
### Bureaucracy
bureauLevel = 0
bureauMisc = 0
### Business
busiLevel = 0
busiMisc = 0
### Composition
compLevel = 0
compMisc = 0
### Criminology
crimLevel = 0
crimMisc = 0
### Cryptography
cryptoLevel = 0
cryptoMisc = 0
### Deduction
dedLevel = 0
dedMisc = 0
### Education
eduLevel = 2
eduMisc = 0
### Gambling
gambleLevel = 0
gambleMisc = 0
### Library Search
libLevel = 0
libMisc = 0
### Tactics
tacLevel = 0
tacMisc = 0
### Wilderness Survival
wildLevel = 0
wildMisc = 0

## Melee
### Brawling
brawlLevel = 2
brawlMisc = 0
### Evasion
evadeLevel = 4
evadeMisc = 0
### Melee Weapons
meleeLevel = 6
meleeMisc = 0

## Performance
### Acting
actLevel = 6
actMisc = 0

## Ranged
### Archery
archLevel = 0
archMisc = 0
### Autofire
autoLevel = 0
autoMisc = 0
### Handguns
handLevel = 0
handMisc = 0
### Heavy Weapons
heavyLevel = 0
heavyMisc = 0
### Shoulder Arms
shoulderLevel = 0
shoulderMisc = 0

## Social
### Bribery
bribeLevel = 0
bribeMisc = 0
### Conversation
convLevel = 6
convMisc = 0
### Human Perception
huperLevel = 4
huperMisc = 0
### Interrogation
interLevel = 0
interMisc = 0
### Persuasion
persLevel = 6
persMisc = 0
### Personal Grooming
groomLevel = 6
groomMisc = 2
### Streetwise
streetLevel = 4
streetMisc = 0
### Trading
tradeLevel = 1
tradeMisc = 0
### Wardrobe and Style
styleLevel = 4
styleMisc = 2

## Tech
### Air Vehicle Tech
airtechLevel = 0
airtechMisc = 0
### Basic Tech
basictechLevel = 0
basictechMisc = 0
### Cybertech
cybertechLevel = 0
cybertechMisc = 0
### Demolitions
demotechLevel = 0
demotechMisc = 0
### Electronics/Security Tech
sectechLevel = 0
sectechMisc = 0
### First Aid
firstaidLevel = 2
firstaidMisc = 0
### Forgery
forgeLevel = 0
forgeMisc = 0
### Land Vehicle Tech
landveLevel = 0
landveMisc = 0
### Paint/Draw/Sculpt
paintLevel = 0
paintMisc = 0
### Paramedic
paraLevel = 0
paraMisc = 0
### Photography
photoLevel = 0
photoMisc = 0
### Pick Lock
picklockLevel = 2
picklockMisc = 0
### Pick Pocket
pickpocketLevel = 4
pickpocketMisc = 0
### Sea Vehicle Tech
seaveLevel = 0
seaveMisc = 0
### Weaponstech
weptechLevel = 0
weptechMisc = 0

########################################################

#################### SKILL MATH ########################

## Multi-Opt
langSkillA = ntlScore
langBaseA = langSkillA + langLevelA + langMiscA

langSkillB = ntlScore
langBaseB = langSkillB + langLevelB + langMiscB

localSkillA = ntlScore
localBaseA = localSkillA + localLevelA + localMiscA

sciSkillA = ntlScore
sciBaseA = sciSkillA + sciLevelA + sciMiscA

martialSkillA = dexScore
martialBaseA = martialSkillA + martialLevelA + martialMiscA

playSkillA = techScore
playBaseA = playSkillA + playLevelA + playMiscA

########################################################

## Awareness
concSkill = willScore
concBase = concSkill + concLevel + concMisc

conrevSkill = ntlScore
conrevBase = conrevSkill + conrevLevel + conrevMisc

lipSkill = ntlScore
lipBase = lipSkill + lipLevel + lipMisc

percSkill = ntlScore
percBase = percSkill + percLevel + percMisc

trackSkill = ntlScore
trackBase = trackSkill + trackLevel + trackMisc

## Body
athSkill = dexScore
athBase = athSkill + athLevel + athMisc

contSkill = dexScore
contBase = contSkill + contLevel + contMisc

danceSkill = dexScore
danceBase = danceSkill + danceLevel + danceMisc

endSkill = willScore
endBase = endSkill + endLevel + endMisc

resistSkill = willScore
resistBase = resistSkill + resistLevel + resistMisc

sneakSkill = dexScore
sneakBase = sneakSkill + sneakLevel + sneakMisc

## Control
landSkill = refScore
landBase = landSkill + landLevel + landMisc

airSkill = refScore
airBase = airSkill + airLevel + airMisc

seaSkill = refScore
seaBase = seaSkill + seaLevel + seaMisc

rideSkill = refScore
rideBase = rideSkill + rideLevel + rideMisc

## Education
accSkill = ntlScore
accBase = accSkill + accLevel + accMisc

animSkill = ntlScore
animBase = animSkill + animLevel + animMisc

bureauSkill = ntlScore
bureauBase = bureauSkill + bureauLevel + bureauMisc

busiSkill = ntlScore
busiBase = busiSkill + busiLevel + busiMisc

compSkill = ntlScore
compBase = compSkill + compLevel + compMisc

crimSkill = ntlScore
crimBase = crimSkill + crimLevel + crimMisc

cryptoSkill = ntlScore
cryptoBase = cryptoSkill + cryptoLevel + cryptoMisc

dedSkill = ntlScore
dedBase = dedSkill + dedLevel + dedMisc

eduSkill = ntlScore
eduBase = eduSkill + eduLevel + eduMisc

gambleSkill = ntlScore
gambleBase = gambleSkill + gambleLevel + gambleMisc

libSkill = ntlScore
libBase = libSkill + libLevel + libMisc

tacSkill = ntlScore
tacBase = tacSkill + tacLevel + tacMisc

wildSkill = ntlScore
wildBase = wildSkill + wildLevel + wildMisc

## Melee
brawlSkill = dexScore
brawlBase = brawlSkill + brawlLevel + brawlMisc

evadeSkill = dexScore
evadeBase = evadeSkill + evadeLevel + evadeMisc

meleeSkill = dexScore
meleeBase = meleeSkill + meleeLevel + meleeMisc

## Performance
actSkill = coolScore
actBase = actSkill + actLevel + actMisc

## Ranged
archSkill = refScore
archBase = archSkill + archLevel + archMisc

autoSkill = refScore
autoBase = autoSkill + autoLevel + autoMisc

handSkill = refScore
handBase = handSkill + handLevel + handMisc

heavySkill = refScore
heavyBase = heavySkill + heavyLevel + heavyMisc

shoulderSkill = refScore
shoulderBase = shoulderSkill + shoulderLevel + shoulderMisc

## Social
bribeSkill = coolScore
bribeBase = bribeSkill + bribeLevel + bribeMisc

convSkill = empScore
convBase = convSkill + convLevel + convMisc

huperSkill = empScore
huperBase = huperSkill + huperLevel + huperMisc

interSkill = coolScore
interBase = interSkill + interLevel + interMisc

persSkill = coolScore
persBase = persSkill + persLevel + persMisc

groomSkill = coolScore
groomBase = groomSkill + groomLevel + groomMisc

streetSkill = coolScore
streetBase = streetSkill + streetLevel + streetMisc

tradeSkill = coolScore
tradeBase = tradeSkill + tradeLevel + tradeMisc

styleSkill = coolScore
styleBase = styleSkill + styleLevel + styleMisc

## Tech
airtechSkill = techScore
airtechBase = airtechSkill + airtechLevel + airtechMisc

basictechSkill = techScore
basictechBase = basictechSkill + basictechLevel + basictechMisc

cybertechSkill = techScore
cybertechBase = cybertechSkill + cybertechLevel + cybertechMisc

demotechSkill = techScore
demotechBase = demotechSkill + demotechLevel + demotechMisc

sectechSkill = techScore
sectechBase = sectechSkill + sectechLevel + sectechMisc

firstaidSkill = techScore
firstaidBase = firstaidSkill + firstaidLevel + firstaidMisc

forgeSkill = techScore
forgeBase = forgeSkill + forgeLevel + forgeMisc

landveSkill = techScore
landveBase = landveSkill + landveLevel + landveMisc

paintSkill = techScore
paintBase = paintSkill + paintLevel + paintMisc

paraSkill = techScore
paraBase = paraSkill + paraLevel + paraMisc

photoSkill = techScore
photoBase = photoSkill + photoLevel + photoMisc

picklockSkill = techScore
picklockBase = picklockSkill + picklockLevel + picklockMisc

pickpocketSkill = techScore
pickpocketBase = pickpocketSkill + pickpocketLevel + pickpocketMisc

seaveSkill = techScore
seaveBase = seaveSkill + seaveLevel + seaveMisc

weptechSkill = techScore
weptechBase = weptechSkill + weptechLevel + weptechMisc

########################################################

#################### SKILL DICT ########################

## Friendly reminder - if you add more Multi-Opt skills,
## add them to this dictionary in the appropriate area.

skillDict = {
    "Awareness Skills": {
        "Concentration": concBase,
        "Conceal/Reveal Object": conrevBase,
        "Lip Reading": lipBase,
        "Perception": percBase,
        "Tracking": trackBase,
        },
    "Body Skills": {
        "Athletics": athBase,
        "Contortionist": contBase,
        "Dance": danceBase,
        "Endurance": endBase,
        "Resist Torture/Drugs": resistBase,
        "Stealth": sneakBase,
        },
    "Control Skills": {
        "Drive Land": landBase,
        "Pilot Air": airBase,
        "Pilot Sea": seaBase,
        "Riding": rideBase,
        },
    "Education Skills": {
        "Accounting": accBase,
        "Animal Handling": animBase,
        "Bureaucracy": bureauBase,
        "Business": busiBase,
        "Composition": compBase,
        "Criminology": crimBase,
        "Cryptography": cryptoBase,
        "Deduction": dedBase,
        "Education": eduBase,
        "Gambling": gambleBase,
        f"Language ({langTypeA})": langBaseA,
        f"Language ({langTypeB})": langBaseB,
        "Library Search": libBase,
        f"Local Expert ({localTypeA})": localBaseA,
        "Tactics": tacBase,
        "Wilderness Survival": wildBase,
        },
    "Melee Fighting Skills": {
        "Brawling": brawlBase,
        "Evasion": evadeBase,
        f"Martial Arts ({martialTypeA})": martialBaseA,
        "Melee Weapons": meleeBase,
        },
    "Performance Skills": {
        "Acting": actBase,
        f"Play Instrument ({playTypeA})": playBaseA,
        },
    "Ranged Weapon Skills": {
        "Archery": archBase,
        "Autofire": autoBase,
        "Handguns": handBase,
        "Heavy Weapons": heavyBase,
        "Shoulder Arms": shoulderBase,
        },
    "Social Skills": {
        "Bribery": bribeBase,
        "Conversation": convBase,
        "Human Perception": huperBase,
        "Interrogation": interBase,
        "Persuasion": persBase,
        "Personal Grooming": groomBase,
        "Streetwise": streetBase,
        "Trading": tradeBase,
        "Wardrobe and Style": styleBase,
        },
    "Technique Skills": {
        "Air Vehicle Tech": airtechBase,
        "Basic Tech": basictechBase,
        "Cybertech": cybertechBase,
        "Demolitions": demotechBase,
        "Electronics/Security Tech": sectechBase,
        "First Aid": firstaidBase,
        "Forgery": forgeBase,
        "Land Vehicle Tech": landveBase,
        "Paint/Draw/Sculpt": paintBase,
        "Paramedic": paraBase,
        "Photography/Film": photoBase,
        "Pick Lock": picklockBase,
        "Pick Pocket": pickpocketBase,
        "Sea Vehicle Tech": seaveBase,
        "Weaponstech": weptechBase,
        },
    }

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

charSPACE = center_text(nbsp, 42)
charEND = center_text(nbsp, 43)
charINT = txtfrm.bold(center_text(f"{ntlScore}", 3)) + center_text("INT //", 6)
charREF = txtfrm.bold(center_text(f"{refScore}", 3)) + center_text("REF //", 6)
charDEX = txtfrm.bold(center_text(f"{dexScore}", 3)) + center_text("DEX //", 6)
charTECH = txtfrm.bold(center_text(f"{techScore}", 3)) + center_text("TECH //", 7)
charCOOL = txtfrm.bold(center_text(f"{coolScore}", 3)) + center_text("COOL //", 7)
charWILL = txtfrm.bold(center_text(f"{willScore}", 3)) + center_text("WILL //", 7)
charMOVE = txtfrm.bold(center_text(f"{moveScore}", 3)) + center_text("MOVE //", 7)
charBODY = txtfrm.bold(center_text(f"{bodyScore}", 3)) + center_text("BODY //", 7)
charEMP = txtfrm.bold(center_text(f"{empScore}", 3)) + center_text(f"/ {maxempScore}", 4) + center_text("EMP //", 7)
charLUCK = txtfrm.bold(center_text(f"{luckScore}", 3)) + center_text(f"/ {maxluckScore}", 4) + center_text("LUCK", 7)

def charHead():
    print(center_text(f"{charName} aka", width))
    print(txtfrm.bold(center_text(charHandle, width)))

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