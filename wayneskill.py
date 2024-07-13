# Import modules.
import waynescore

#####################################
#  Cyberpunk RED CharSkill Def v0d  #
# by nowherekydd # Updated 7/13/24  #
#         Github here later         #
#####################################

# Template
#Skill = waynescore.Score
#Level = 2
#Misc = 0
#Base = Skill + Level + Misc

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

# Print for debug.
print("Awareness Skills")
print(f"Concentration: {concBase}")
print(f"Conceal/Reveal Object: {conrevBase}")
print(f"Lip Reading: {lipBase}")
print(f"Perception: {percBase}")
print(f"Tracking: {trackBase}")
print("----------------------")
print("Body Skills")
print(f"Athletics: {athBase}")
print(f"Contortionist: {contBase}")
print(f"Dance: {danceBase}")
print(f"Endurance: {endBase}")
print(f"Resist Torture/Drugs: {resistBase}")
print(f"Stealth: {sneakBase}")
print("----------------------")
print("Control Skills")
print(f"Drive Land: {landBase}")
print(f"Pilot Air: {airBase}")
print(f"Pilot Sea: {seaBase}")
print(f"Riding: {rideBase}")
print("----------------------")
print("Education Skills")
print(f"Accounting: {accBase}")
print(f"Animal Handling: {animBase}")
print(f"Bureaucracy: {bureauBase}")
print(f"Business: {busiBase}")
print(f"Composition: {compBase}")
print(f"Criminology: {crimBase}")
print(f"Cryptography: {cryptoBase}")
print(f"Deduction: {dedBase}")
print(f"Education: {eduBase}")
print(f"Gambling: {gambleBase}")
print(f"Library Search: {libBase}")
print(f"Tactics: {tacBase}")
print(f"Wilderness Survival: {wildBase}")
print("----------------------")
print("Melee Fighting Skills")
print(f"Brawling: {brawlBase}")
print(f"Evasion: {evadeBase}")
print(f"Melee Weapons: {meleeBase}")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~ Multi-Option Skills ~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f"Language ({langTypeA}): {langBaseA}")
print(f"Language ({langTypeB}): {langBaseB}")
print(f"Local Expert ({localTypeA}): {langBaseA}")
print("Science: null")
print(f"Martial Arts ({martialTypeA}): {martialBaseA}")