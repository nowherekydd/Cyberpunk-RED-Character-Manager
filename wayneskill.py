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
import waynescore

# Awareness Skills
concSkill = waynescore.willScore
concLevel = 2
concMisc = 0
concBase = concSkill + concLevel + concMisc

conrevSkill = waynescore.ntlScore
conrevLevel = 3
conrevMisc = 0
conrevBase = conrevSkill + conrevLevel + conrevMisc

lipSkill = waynescore.ntlScore
lipLevel = 0
lipMisc = 0
lipBase = lipSkill + lipLevel + lipMisc

percSkill = waynescore.ntlScore
percLevel = 2
percMisc = 0
percBase = percSkill + percLevel + percMisc

trackSkill = waynescore.ntlScore
trackLevel = 0
trackMisc = 0
trackBase = trackSkill + trackLevel + trackMisc

# Body Skills
athSkill = waynescore.dexScore
athLevel = 2
athMisc = 0
athBase = athSkill + athLevel + athMisc

contSkill = waynescore.dexScore
contLevel = 0
contMisc = 0
contBase = contSkill + contLevel + contMisc

danceSkill = waynescore.dexScore
danceLevel = 0
danceMisc = 0
danceBase = danceSkill + danceLevel + danceMisc

endSkill = waynescore.willScore
endLevel = 0
endMisc = 0
endBase = endSkill + endLevel + endMisc

resistSkill = waynescore.willScore
resistLevel = 5
resistMisc = 0
resistBase = resistSkill + resistLevel + resistMisc

sneakSkill = waynescore.dexScore
sneakLevel = 2
sneakMisc = 0
sneakBase = sneakSkill + sneakLevel + sneakMisc

# Control Skills
landSkill = waynescore.refScore
landLevel = 2
landMisc = 0
landBase = landSkill + landLevel + landMisc

airSkill = waynescore.refScore
airLevel = 0
airMisc = 0
airBase = airSkill + airLevel + airMisc

seaSkill = waynescore.refScore
seaLevel = 0
seaMisc = 0
seaBase = seaSkill + seaLevel + seaMisc

rideSkill = waynescore.refScore
rideLevel = 0
rideMisc = 0
rideBase = rideSkill + rideLevel + rideMisc

# Education Skills
accSkill = waynescore.ntlScore
accLevel = 0
accMisc = 0
accBase = accSkill + accLevel + accMisc

animSkill = waynescore.ntlScore
animLevel = 0
animMisc = 0
animBase = animSkill + animLevel + animMisc

bureauSkill = waynescore.ntlScore
bureauLevel = 0
bureauMisc = 0
bureauBase = bureauSkill + bureauLevel + bureauMisc

busiSkill = waynescore.ntlScore
busiLevel = 0
busiMisc = 0
busiBase = busiSkill + busiLevel + busiMisc

compSkill = waynescore.ntlScore
compLevel = 3
compMisc = 0
compBase = compSkill + compLevel + compMisc

crimSkill = waynescore.ntlScore
crimLevel = 0
crimMisc = 0
crimBase = crimSkill + crimLevel + crimMisc

cryptoSkill = waynescore.ntlScore
cryptoLevel = 0
cryptoMisc = 0
cryptoBase = cryptoSkill + cryptoLevel + cryptoMisc

dedSkill = waynescore.ntlScore
dedLevel = 0
dedMisc = 0
dedBase = dedSkill + dedLevel + dedMisc

eduSkill = waynescore.ntlScore
eduLevel = 2
eduMisc = 0
eduBase = eduSkill + eduLevel + eduMisc

gambleSkill = waynescore.ntlScore
gambleLevel = 0
gambleMisc = 0
gambleBase = gambleSkill + gambleLevel + gambleMisc

libSkill = waynescore.ntlScore
libLevel = 0
libMisc = 0
libBase = libSkill + libLevel + libMisc

tacSkill = waynescore.ntlScore
tacLevel = 0
tacMisc = 0
tacBase = tacSkill + tacLevel + tacMisc

wildSkill = waynescore.ntlScore
wildLevel = 0
wildMisc = 0
wildBase = wildSkill + wildLevel + wildMisc

# Melee Fighting Skills
brawlSkill = waynescore.dexScore
brawlLevel = 2
brawlMisc = 0
brawlBase = brawlSkill + brawlLevel + brawlMisc

evadeSkill = waynescore.dexScore
evadeLevel = 4
evadeMisc = 0
evadeBase = evadeSkill + evadeLevel + evadeMisc

meleeSkill = waynescore.dexScore
meleeLevel = 2
meleeMisc = 0
meleeBase = meleeSkill + meleeLevel + meleeMisc

# Performance Skills
actSkill = waynescore.coolScore
actLevel = 0
actMisc = 0
actBase = actSkill + actLevel + actMisc

# Ranged Weapon Skills
archSkill = waynescore.refScore
archLevel = 0
archMisc = 0
archBase = archSkill + archLevel + archMisc

autoSkill = waynescore.refScore
autoLevel = 0
autoMisc = 0
autoBase = autoSkill + autoLevel + autoMisc

handSkill = waynescore.refScore
handLevel = 4
handMisc = 0
handBase = handSkill + handLevel + handMisc

heavySkill = waynescore.refScore
heavyLevel = 0
heavyMisc = 0
heavyBase = heavySkill + heavyLevel + heavyMisc

shoulderSkill = waynescore.refScore
shoulderLevel = 0
shoulderMisc = 0
shoulderBase = shoulderSkill + shoulderLevel + shoulderMisc

# Social Skills
bribeSkill = waynescore.coolScore
bribeLevel = 0
bribeMisc = 0
bribeBase = bribeSkill + bribeLevel + bribeMisc

convSkill = waynescore.empScore
convLevel = 2
convMisc = 0
convBase = convSkill + convLevel + convMisc

huperSkill = waynescore.empScore
huperLevel = 2
huperMisc = 0
huperBase = huperSkill + huperLevel + huperMisc

interSkill = waynescore.coolScore
interLevel = 0
interMisc = 0
interBase = interSkill + interLevel + interMisc

persSkill = waynescore.coolScore
persLevel = 2
persMisc = 0
persBase = persSkill + persLevel + persMisc

groomSkill = waynescore.coolScore
groomLevel = 4
groomMisc = 0
groomBase = groomSkill + groomLevel + groomMisc

streetSkill = waynescore.coolScore
streetLevel = 3
streetMisc = 0
streetBase = streetSkill + streetLevel + streetMisc

tradeSkill = waynescore.coolScore
tradeLevel = 0
tradeMisc = 0
tradeBase = tradeSkill + tradeLevel + tradeMisc

styleSkill = waynescore.coolScore
styleLevel = 2
styleMisc = 0
styleBase = styleSkill + styleLevel + styleMisc

# Tech Skills
airtechSkill = waynescore.techScore
airtechLevel = 0
airtechMisc = 0
airtechBase = airtechSkill + airtechLevel + airtechMisc

basictechSkill = waynescore.techScore
basictechLevel = 2
basictechMisc = 0
basictechBase = basictechSkill + basictechLevel + basictechMisc

cybertechSkill = waynescore.techScore
cybertechLevel = 6
cybertechMisc = 0
cybertechBase = cybertechSkill + cybertechLevel + cybertechMisc

demotechSkill = waynescore.techScore
demotechLevel = 0
demotechMisc = 0
demotechBase = demotechSkill + demotechLevel + demotechMisc

sectechSkill = waynescore.techScore
sectechLevel = 0
sectechMisc = 0
sectechBase = sectechSkill + sectechLevel + sectechMisc

firstaidSkill = waynescore.techScore
firstaidLevel = 2
firstaidMisc = 0
firstaidBase = firstaidSkill + firstaidLevel + firstaidMisc

forgeSkill = waynescore.techScore
forgeLevel = 0
forgeMisc = 0
forgeBase = forgeSkill + forgeLevel + forgeMisc

landveSkill = waynescore.techScore
landveLevel = 2
landveMisc = 0
landveBase = landveSkill + landveLevel + landveMisc

paintSkill = waynescore.techScore
paintLevel = 0
paintMisc = 0
paintBase = paintSkill + paintLevel + paintMisc

paraSkill = waynescore.techScore
paraLevel = 0
paraMisc = 0
paraBase = paraSkill + paraLevel + paraMisc

photoSkill = waynescore.techScore
photoLevel = 0
photoMisc = 0
photoBase = photoSkill + photoLevel + photoMisc

picklockSkill = waynescore.techScore
picklockLevel = 0
picklockMisc = 0
picklockBase = picklockSkill + picklockLevel + picklockMisc

pickpocketSkill = waynescore.techScore
pickpocketLevel = 0
pickpocketMisc = 0
pickpocketBase = pickpocketSkill + pickpocketLevel + pickpocketMisc

seaveSkill = waynescore.techScore
seaveLevel = 0
seaveMisc = 0
seaveBase = seaveSkill + seaveLevel + seaveMisc

weptechSkill = waynescore.techScore
weptechLevel = 2
weptechMisc = 0
weptechBase = weptechSkill + weptechLevel + weptechMisc

###################################################

# Multi-Option Skills
# (Skills that can be bought more than 1x
# and must be specialized each time)

## Language Skills
langSkillA = waynescore.ntlScore
langLevelA = 2
langMiscA = 0
langBaseA = langSkillA + langLevelA + langMiscA
langTypeA = "Streetslang"

langSkillB = waynescore.ntlScore
langLevelB = 4
langMiscB = 0
langBaseB = langSkillB + langLevelB + langMiscB
langTypeB = "English"

## Local Expert Skills
localSkillA = waynescore.ntlScore
localLevelA = 4
localMiscA = 0
localBaseA = localSkillA + localLevelA + localMiscA
localTypeA = "University District"

## Science Skills
sciSkillA = waynescore.ntlScore
sciLevelA = 0
sciMiscA = 0
sciBaseA = sciSkillA + sciLevelA + sciMiscA
sciTypeA = "null"

## Martial Arts Skills
martialSkillA = waynescore.dexScore
martialLevelA = 5
martialMiscA = 0
martialBaseA = martialSkillA + martialLevelA + martialMiscA
martialTypeA = "Judo"

## Instrument Skills
playSkillA = waynescore.techScore
playLevelA = 4
playMiscA = 0
playBaseA = playSkillA + playLevelA + playMiscA
playTypeA = "Guitar"

playSkillB = waynescore.techScore
playLevelB = 4
playMiscB = 0
playBaseB = playSkillB + playLevelB + playMiscB
playTypeB = "Vocals"

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
        f"Play Instrument ({playTypeB})": playBaseB,
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