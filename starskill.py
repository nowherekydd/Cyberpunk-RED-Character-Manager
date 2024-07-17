#   _____ _____   _____ _      _____ 
#  / ____|  __ \ / ____| |    |_   _|
# | |    | |__) | |    | |      | |  
# | |    |  _  /| |    | |      | |  
# | |____| | \ \| |____| |____ _| |_ 
#  \_____|_|  \_\\_____|______|_____|
#
# Cyberpunk: RED CLI Character Manager
# by nowherekydd // v0d
# Skillsheet - maybe roll into main character sheet later?

# Import modules.
import starscore

# Awareness Skills
concSkill = starscore.willScore
concLevel = 2
concMisc = 0
concBase = concSkill + concLevel + concMisc

conrevSkill = starscore.ntlScore
conrevLevel = 3
conrevMisc = 0
conrevBase = conrevSkill + conrevLevel + conrevMisc

lipSkill = starscore.ntlScore
lipLevel = 2
lipMisc = 0
lipBase = lipSkill + lipLevel + lipMisc

percSkill = starscore.ntlScore
percLevel = 2
percMisc = 0
percBase = percSkill + percLevel + percMisc

trackSkill = starscore.ntlScore
trackLevel = 0
trackMisc = 0
trackBase = trackSkill + trackLevel + trackMisc

# Body Skills
athSkill = starscore.dexScore
athLevel = 2
athMisc = 0
athBase = athSkill + athLevel + athMisc

contSkill = starscore.dexScore
contLevel = 0
contMisc = 0
contBase = contSkill + contLevel + contMisc

danceSkill = starscore.dexScore
danceLevel = 0
danceMisc = 0
danceBase = danceSkill + danceLevel + danceMisc

endSkill = starscore.willScore
endLevel = 2
endMisc = 0
endBase = endSkill + endLevel + endMisc

resistSkill = starscore.willScore
resistLevel = 6
resistMisc = 2
resistBase = resistSkill + resistLevel + resistMisc

sneakSkill = starscore.dexScore
sneakLevel = 4
sneakMisc = 0
sneakBase = sneakSkill + sneakLevel + sneakMisc

# Control Skills
landSkill = starscore.refScore
landLevel = 0
landMisc = 0
landBase = landSkill + landLevel + landMisc

airSkill = starscore.refScore
airLevel = 0
airMisc = 0
airBase = airSkill + airLevel + airMisc

seaSkill = starscore.refScore
seaLevel = 0
seaMisc = 0
seaBase = seaSkill + seaLevel + seaMisc

rideSkill = starscore.refScore
rideLevel = 0
rideMisc = 0
rideBase = rideSkill + rideLevel + rideMisc

# Education Skills
accSkill = starscore.ntlScore
accLevel = 0
accMisc = 0
accBase = accSkill + accLevel + accMisc

animSkill = starscore.ntlScore
animLevel = 0
animMisc = 0
animBase = animSkill + animLevel + animMisc

bureauSkill = starscore.ntlScore
bureauLevel = 0
bureauMisc = 0
bureauBase = bureauSkill + bureauLevel + bureauMisc

busiSkill = starscore.ntlScore
busiLevel = 0
busiMisc = 0
busiBase = busiSkill + busiLevel + busiMisc

compSkill = starscore.ntlScore
compLevel = 0
compMisc = 0
compBase = compSkill + compLevel + compMisc

crimSkill = starscore.ntlScore
crimLevel = 0
crimMisc = 0
crimBase = crimSkill + crimLevel + crimMisc

cryptoSkill = starscore.ntlScore
cryptoLevel = 0
cryptoMisc = 0
cryptoBase = cryptoSkill + cryptoLevel + cryptoMisc

dedSkill = starscore.ntlScore
dedLevel = 0
dedMisc = 0
dedBase = dedSkill + dedLevel + dedMisc

eduSkill = starscore.ntlScore
eduLevel = 2
eduMisc = 0
eduBase = eduSkill + eduLevel + eduMisc

gambleSkill = starscore.ntlScore
gambleLevel = 0
gambleMisc = 0
gambleBase = gambleSkill + gambleLevel + gambleMisc

libSkill = starscore.ntlScore
libLevel = 0
libMisc = 0
libBase = libSkill + libLevel + libMisc

tacSkill = starscore.ntlScore
tacLevel = 0
tacMisc = 0
tacBase = tacSkill + tacLevel + tacMisc

wildSkill = starscore.ntlScore
wildLevel = 0
wildMisc = 0
wildBase = wildSkill + wildLevel + wildMisc

# Melee Fighting Skills
brawlSkill = starscore.dexScore
brawlLevel = 2
brawlMisc = 0
brawlBase = brawlSkill + brawlLevel + brawlMisc

evadeSkill = starscore.dexScore
evadeLevel = 4
evadeMisc = 0
evadeBase = evadeSkill + evadeLevel + evadeMisc

meleeSkill = starscore.dexScore
meleeLevel = 6
meleeMisc = 0
meleeBase = meleeSkill + meleeLevel + meleeMisc

# Performance Skills
actSkill = starscore.coolScore
actLevel = 6
actMisc = 0
actBase = actSkill + actLevel + actMisc

# Ranged Weapon Skills
archSkill = starscore.refScore
archLevel = 0
archMisc = 0
archBase = archSkill + archLevel + archMisc

autoSkill = starscore.refScore
autoLevel = 0
autoMisc = 0
autoBase = autoSkill + autoLevel + autoMisc

handSkill = starscore.refScore
handLevel = 0
handMisc = 0
handBase = handSkill + handLevel + handMisc

heavySkill = starscore.refScore
heavyLevel = 0
heavyMisc = 0
heavyBase = heavySkill + heavyLevel + heavyMisc

shoulderSkill = starscore.refScore
shoulderLevel = 0
shoulderMisc = 0
shoulderBase = shoulderSkill + shoulderLevel + shoulderMisc

# Social Skills
bribeSkill = starscore.coolScore
bribeLevel = 0
bribeMisc = 0
bribeBase = bribeSkill + bribeLevel + bribeMisc

convSkill = starscore.empScore
convLevel = 6
convMisc = 0
convBase = convSkill + convLevel + convMisc

huperSkill = starscore.empScore
huperLevel = 4
huperMisc = 0
huperBase = huperSkill + huperLevel + huperMisc

interSkill = starscore.coolScore
interLevel = 0
interMisc = 0
interBase = interSkill + interLevel + interMisc

persSkill = starscore.coolScore
persLevel = 6
persMisc = 0
persBase = persSkill + persLevel + persMisc

groomSkill = starscore.coolScore
groomLevel = 6
groomMisc = 2
groomBase = groomSkill + groomLevel + groomMisc

streetSkill = starscore.coolScore
streetLevel = 4
streetMisc = 0
streetBase = streetSkill + streetLevel + streetMisc

tradeSkill = starscore.coolScore
tradeLevel = 1
tradeMisc = 0
tradeBase = tradeSkill + tradeLevel + tradeMisc

styleSkill = starscore.coolScore
styleLevel = 4
styleMisc = 2
styleBase = styleSkill + styleLevel + styleMisc

# Tech Skills
airtechSkill = starscore.techScore
airtechLevel = 0
airtechMisc = 0
airtechBase = airtechSkill + airtechLevel + airtechMisc

basictechSkill = starscore.techScore
basictechLevel = 0
basictechMisc = 0
basictechBase = basictechSkill + basictechLevel + basictechMisc

cybertechSkill = starscore.techScore
cybertechLevel = 0
cybertechMisc = 0
cybertechBase = cybertechSkill + cybertechLevel + cybertechMisc

demotechSkill = starscore.techScore
demotechLevel = 0
demotechMisc = 0
demotechBase = demotechSkill + demotechLevel + demotechMisc

sectechSkill = starscore.techScore
sectechLevel = 0
sectechMisc = 0
sectechBase = sectechSkill + sectechLevel + sectechMisc

firstaidSkill = starscore.techScore
firstaidLevel = 2
firstaidMisc = 0
firstaidBase = firstaidSkill + firstaidLevel + firstaidMisc

forgeSkill = starscore.techScore
forgeLevel = 0
forgeMisc = 0
forgeBase = forgeSkill + forgeLevel + forgeMisc

landveSkill = starscore.techScore
landveLevel = 0
landveMisc = 0
landveBase = landveSkill + landveLevel + landveMisc

paintSkill = starscore.techScore
paintLevel = 0
paintMisc = 0
paintBase = paintSkill + paintLevel + paintMisc

paraSkill = starscore.techScore
paraLevel = 0
paraMisc = 0
paraBase = paraSkill + paraLevel + paraMisc

photoSkill = starscore.techScore
photoLevel = 0
photoMisc = 0
photoBase = photoSkill + photoLevel + photoMisc

picklockSkill = starscore.techScore
picklockLevel = 2
picklockMisc = 0
picklockBase = picklockSkill + picklockLevel + picklockMisc

pickpocketSkill = starscore.techScore
pickpocketLevel = 4
pickpocketMisc = 0
pickpocketBase = pickpocketSkill + pickpocketLevel + pickpocketMisc

seaveSkill = starscore.techScore
seaveLevel = 0
seaveMisc = 0
seaveBase = seaveSkill + seaveLevel + seaveMisc

weptechSkill = starscore.techScore
weptechLevel = 0
weptechMisc = 0
weptechBase = weptechSkill + weptechLevel + weptechMisc

###################################################

# Multi-Option Skills
# (Skills that can be bought more than 1x
# and must be specialized each time)

## Language Skills
langSkillA = starscore.ntlScore
langLevelA = 2
langMiscA = 0
langBaseA = langSkillA + langLevelA + langMiscA
langTypeA = "Streetslang"

langSkillB = starscore.ntlScore
langLevelB = 4
langMiscB = 0
langBaseB = langSkillB + langLevelB + langMiscB
langTypeB = "English"

## Local Expert Skills
localSkillA = starscore.ntlScore
localLevelA = 4
localMiscA = 0
localBaseA = localSkillA + localLevelA + localMiscA
localTypeA = "University District"

## Science Skills
sciSkillA = starscore.ntlScore
sciLevelA = 0
sciMiscA = 0
sciBaseA = sciSkillA + sciLevelA + sciMiscA
sciTypeA = "null"

## Martial Arts Skills
martialSkillA = starscore.dexScore
martialLevelA = 0
martialMiscA = 0
martialBaseA = martialSkillA + martialLevelA + martialMiscA
martialTypeA = "null"

## Instrument Skills
playSkillA = starscore.techScore
playLevelA = 0
playMiscA = 0
playBaseA = playSkillA + playLevelA + playMiscA
playTypeA = "null"

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