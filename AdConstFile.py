# ------------------------------------------------------------------------------
# Copyright © 2017 Daniil Nepryahin
# contacts: <nervoidaz@yandex.ru>
# License: https://opensource.org/licenses/cpl1.0.php
# ------------------------------------------------------------------------------


# Addictional file with 'constants' that very useful

''' It's time to create some global constants
    So, you should know that there're some types of Character possible trips
    and some types of possible Enemy
    so trip can be easy, normal (medium), hard and very hard,
    and unique - forest trip
    Enemies can be easy, normal(medium), hard, unique (that will create by hand),
    and animals
    idea is: we have Random Function and we have set of possible Enemies
    so, let's create random Enemy. Of course, Enemy not random at all, there're
    some setups for them (classes like archer, warrior, thief, etc.)
    In area these classes will use clearly. Field Enemies I create as I see them
'''
# Data File name
constDataFileName = 'GameData.NEU'
# common traits tuple
constCommonTraits = ('Vitality', 'Strength', 'Luck', 'Agility', 'Accuracy',
                     'Attention', 'Charisma', 'Intelligence', 'Instinct')
# Special traits tuple
constSpecialTraits = ('Undead', 'Carrier', 'QuickHand', 'OnePunch', 'Physician',
                      'Trader')
# General param tuple
constGeneralParams = ('Name', 'Description', 'CHealth', 'MHealth', 'MinDamage',
                      'MaxDamage', 'MaxPotion', 'PotionSlots', 'PotionRestore',
                      'Gold', 'Level', 'Experience', 'HitChance', 'AttackSpeed',
                      'FindChance', 'KnowChance', 'FleeChance', 'BattleRestore')
# Weapons params
constWeaponParams = ('Name', 'Description', 'Price', 'MinDamage', 'MaxDamage',
                     'AttackSpeed')
# Armours params
constArmourParams = ('Name', 'Description', 'Price', 'HealthBoost', 'SpeedBoost')
# Random functions for trips
constEasyTrip = {'EasyEnemy': 80, 'AnimalEnemy': 15, 'MediumEnemy': 5 }
constMediumTrip = {'EasyEnemy': 15, 'AnimalEnemy': 10, 'MediumEnemy': 70,
                   'HardEnemy': 5}
constHardTrip = {'EasyEnemy': 5, 'AnimalEnemy': 5, 'MediumEnemy': 35,
                 'HardEnemy': 55}
constVeryHardTrip = {'MediumEnemy': 15, 'HardEnemy': 80, 'UniqueEnemy': 5}
constForestTrip = {'EasyEnemy': 10, 'AnimalEnemy': 90}
constArenaAnimal = {'AnimalEnemy': 100}
# random functions for bosses
constEasyBoss = {'EasyEnemy': 30, 'MediumEnemy': 70}
constMediumBoss = {'MediumEnemy': 20, 'HardEnemy': 80}
constHardBoss = {'HardEnemy': 40, 'UniqueEnemy': 60}
constVeryHardBoss = {'HardEnemy': 10, 'UniqueEnemy': 90}
# Names of places
constCityName = 'City'
constFortName = 'Fort'
constTowerName = 'Watch Tower'
constHofName = 'Druid Grove'
constAbandonedFortName = 'Abandoned Fort'
constDenName = 'Robber\'s Den'
constCoastalCaveName = 'Coastal Cave'
constDragonIslandName = 'It\'s secret for now ;)'
# length of trips. To place {From: HowLong}. from = const*Name
constToCityLength = {constFortName: 5, constTowerName: 10, constHofName:5,
                     constAbandonedFortName: 15, constDenName: 25}
constToFortLength = {constCityName: constToCityLength[constFortName],
                     constAbandonedFortName: 13}
constToTowerLength = {constCityName: constToCityLength[constTowerName],
                      constCoastalCaveName: 40}
constToHofLength = {constCityName: constToCityLength[constHofName]}
constToAbandonedFortLength = {constCityName: constToCityLength[constAbandonedFortName],
                              constFortName: constToFortLength[constAbandonedFortName]}
constToDenLength = {constCityName: constToCityLength[constDenName]}
constToCoastalCaveLength = {constTowerName: constToTowerLength[constCoastalCaveName]}
# types of trips. To place {From: TripType}
constToCityTrip = {constFortName: constEasyTrip, constTowerName: constEasyTrip,
                   constHofName: constForestTrip, constAbandonedFortName: constMediumTrip,
                   constDenName: constMediumTrip}
constToFortTrip = {constCityName: constToCityTrip[constFortName],
                   constAbandonedFortName: constMediumTrip}
constToTowerTrip = {constCityName: constToCityTrip[constTowerName],
                    constCoastalCaveName: constVeryHardTrip}
constToHofTrip = {constCityName: constToCityTrip[constHofName]}
constToAbandonedFortTrip = {constCityName: constToCityTrip[constAbandonedFortName],
                            constFortName: constToFortTrip[constAbandonedFortName]}
constToDenTrip = {constCityName: constToCityTrip[constDenName]}
constToCoastalCaveTrip = {constTowerName: constToTowerTrip[constCoastalCaveName]}
# Places INFO {Name, TripLength, IsSafe, TripType, PossibleTrip, EnemyChance, BossType}
# place name, how far is place, is place safe? trip type, chance to meet enemy,
# boss type in place (if need); PossibleTrip = tuple of Possibble places with info
constCityPlace = {'Name': constCityName, 'TripLength': constToCityLength,
                  'IsSafe': True, 'TripType': constToCityTrip, 'EnemyChance': 100}
constFortPlace = {'Name': constFortName, 'TripLength': constToFortLength,
                  'IsSafe': True, 'TripType': constToFortTrip, 'EnemyChance': 100}
constTowerPlace = {'Name': constTowerName, 'TripLength': constToTowerLength,
                   'IsSafe': True, 'TripType': constToTowerTrip,'EnemyChance': 100}
constHofPlace = {'Name': constHofName, 'TripLength': constToHofLength,
                 'IsSafe': True, 'TripType': constToHofTrip,'EnemyChance': 100}
constAbandonedFortPlace = {'Name': constAbandonedFortName,
                           'TripLength': constToAbandonedFortLength, 'IsSafe': False,
                           'TripType': constToAbandonedFortTrip,
                           'EnemyChance': 65, 'BossType': constMediumBoss}
constDenPlace = {'Name': constDenName, 'TripLength': constToDenLength,
                 'IsSafe': False, 'TripType': constToDenTrip, 'EnemyChance': 50,
                 'BossType': constMediumBoss}
constCoastalCavePlace = {'Name': constCoastalCaveName,
                         'TripLength': constToCoastalCaveLength,
                         'IsSafe': False, 'TripType': constToCoastalCaveTrip,
                         'EnemyChance': 70, 'BossType': constVeryHardBoss}
# Possible trips FromPlace
# let's show Python future variables
constFromCityTrip = [[constFortPlace, 'Easy'], [constTowerPlace, 'Easy'],
                     [constHofPlace, 'Easy'], [constAbandonedFortPlace, 'Medium'],
                     [constDenPlace, 'Medium']]
constFromFortTrip = [[constCityPlace, 'Easy'],
                     [constAbandonedFortPlace, 'Medium']]
constFromTowerTrip = [[constCityPlace, 'Easy'],
                      [constCoastalCavePlace, 'Very hard']]
constFromHofTrip = [[constCityPlace, 'Easy']]
constFromAbandonedFortTrip = [[constCityPlace, 'Medium'],
                              [constFortPlace, 'Medium']]
constFromDenTrip = [[constCityPlace, 'Medium']]
constFromCoastalCaveTrip = [[constTowerPlace, 'Very hard']]
# append Places
constCityPlace['PossibleTrip'] = constFromCityTrip
constFortPlace['PossibleTrip'] = constFromFortTrip
constTowerPlace['PossibleTrip'] = constFromTowerTrip
constHofPlace['PossibleTrip'] = constFromHofTrip
constAbandonedFortPlace['PossibleTrip'] = constFromAbandonedFortTrip
constDenPlace['PossiblePlace'] = constFromDenTrip
constCoastalCavePlace['PossibleTrip'] = constFromCoastalCaveTrip
# Keys for Params
constDefaultParams = {'Place': constCityPlace}
# Weapons and Armours
constNoneWeapon = ({'Name': 'None', 'Description': '', 'Price': 0,
                    'Damage': (0, 0), 'AttackSpeed': 0}, )
constNoneArmour = ({'Name': 'None', 'Description': '', 'Price': 0,
                    'HealthBoost': 0, 'SpeedBoost': 0}, )
# It's better to generate weapon object when we generate Enemy, so there will be
# tuple of dictionaries. Also, Weapons and Armour will be tradable, so it's time
# to add Price to them
constDaggerWeapon = ({'Name': 'Rusty dagger', 'Description': """It's an
                      old rusty dagger, that has lived his best times.""",
                      'Price': 200, 'Damage': (1, 5), 'AttackSpeed': 30},

                     {'Name': 'Blunt dagger', 'Description': """It's a good dagger,
                      but it's blunt.""", 'Price': 520, 'Damage': (2, 6),
                      'AttackSpeed': 40},

                     {'Name': 'Dagger', 'Description': """It's a good dagger in
                      good condition.""", 'Price': 688, 'Damage': (2, 7),
                      'AttackSpeed': 40},

                     {'Name': 'Sharpened dagger', 'Description': """It's a good
                      dagger, that was well sharpened.""", 'Price': 1100,
                      'Damage': (3, 8), 'AttackSpeed': 50})

constSwordWeapon = ({'Name': 'Rusty sword', 'Description': """It's an old rusty
                      sword, that has lived his best times.""", 'Price': 757,
                      'Damage': (5, 10), 'AttackSpeed': 15},

                     {'Name': 'Blunt sword', 'Description': """It's a good sword,
                      but it's blunt.""", 'Price': 1098, 'Damage': (6, 12),
                      'AttackSpeed': 15},

                     {'Name': 'Sword', 'Description': """It's a good sword in
                      good condition.""", 'Price': 2426, 'Damage': (8, 13),
                      'AttackSpeed': 25},

                     {'Name': 'Sharpened sword', 'Description': """It's a good
                      sword, that was well sharpened.""", 'Price': 3954,
                      'Damage': (9, 15), 'AttackSpeed': 25})

constAxeWeapon = ({'Name': 'Rusty axe', 'Description': """It's an old rusty
                      axe, that has lived his best times. But it's still cool tool
                      to crack enemies' skulls.""", 'Price': 1342,
                      'Damage': (7, 11), 'AttackSpeed': 15},

                     {'Name': 'Blunt axe', 'Description': """It's a good axe,
                      but it's blunt. It doesn't chop, it cracks!""",
                      'Price': 1701, 'Damage': (7, 13), 'AttackSpeed': 15},

                     {'Name': 'Axe', 'Description': """It's a good axe in
                      good condition, be made in viking traditions.""",
                      'Price': 2546, 'Damage': (9, 15), 'AttackSpeed': 20},

                     {'Name': 'Sharpened Axe', 'Description': """What can be
                      better?""", 'Price': 3805, 'Damage': (10, 17),
                      'AttackSpeed': 20})

constSpearWeapon = ({'Name': 'Rusty spear', 'Description': """It's an old rusty
                      spear, that has lived his best times. But it's still cool
                      place for enemies' heads.""", 'Price': 1933,
                      'Damage': (8, 13), 'AttackSpeed': 15},

                     {'Name': 'Blunt spear', 'Description': """It's a good spear,
                      but it's blunt. Is it matter for spear?!""",
                      'Price': 2205, 'Damage': (8, 15), 'AttackSpeed': 15},

                     {'Name': 'Spear', 'Description': """It's a good spear in
                      good condition. Few people know that vikings had more spears
                      than axes.""", 'Price': 3577, 'Damage': (10, 15),
                      'AttackSpeed': 20},

                     {'Name': 'Balanced Spear', 'Description': """It's good
                      spear that was well balanced and sharpened.""",
                      'Price': 6914, 'Damage': (12, 18),
                      'AttackSpeed': 20})

constGreatSwordWeapon = ({'Name': 'Rusty great sword', 'Description': """It's an old rusty
                          great sword. It's as big as his history.""", 'Price': 2004,
                          'Damage': (10, 17), 'AttackSpeed': 10},

                         {'Name': 'Blunt great sword', 'Description': """It's a good great
                          sword. This weapon has no flaw, except his blunt edges.""",
                          'Price': 2152, 'Damage': (13, 20), 'AttackSpeed': 10},

                         {'Name': 'Zweihänder', 'Description': """Legendary great sword made
                          for elegant and deadly movements.""", 'Price': 6288,
                          'Damage': (15, 20), 'AttackSpeed': 15},

                         {'Name': 'Sharpened zweihänder', 'Description': """Legendary great
                          sword was improved, well balanced, well sharpened. It was made for
                          true connoisseur of martial arts.""", 'Price': 12538,
                          'Damage': (17, 25), 'AttackSpeed': 15})

constHammerWeapon = ({'Name': 'Old hammer', 'Description': """It's an old rusty
                      large heavy hammer for forging metals, crushing stones and skulls.""",
                      'Price': 2456, 'Damage': (15, 20), 'AttackSpeed': 5},

                     {'Name': "Blacksmith's special hammer", 'Description': """It's an large
                      heavy hammer for forging metals, crushing stones and skulls. It's
                      special blacksmith's tool that not everyone can afford.""",
                      'Price': 3140, 'Damage': (15, 25), 'AttackSpeed': 5},

                     {'Name': 'Zwerg hammer', 'Description': """This hammer has survived
                      to the present day. It belonged to ancient Zwerg race. They was short
                      and very strong human-like creatures with long beards.""",
                      'Price': 12785, 'Damage': (20, 25), 'AttackSpeed': 10},

                     {'Name': 'Improved Zwerg hammer', 'Description': """This hammer belonged
                      to ancient Zwerg race. Best modern blacksmiths hard working on this
                      deadly weapon and now it's the best decision to kill everything that
                      can move.""", 'Price': 18091, 'Damage': (20, 30), 'AttackSpeed': 10})

constBowWeapon = ({'Name': 'Old bow', 'Description': """This bow was sold by old hunter. It
                   still can shoot, but it's so old as our world!""", 'Price': 1879,
                   'Damage': (10, 15), 'AttackSpeed': 10},

                  {'Name': 'Long bow', 'Description': """Common bow, good choice to hunt some
                   bad guys""", 'Price': 1959, 'Damage': (12, 17), 'AttackSpeed': 10},

                  {'Name': 'Short bow', 'Description': """Common short bow for adventurer who
                   prefer attack speed to damage.""", 'Price': 2279, 'Damage': (10, 17),
                   'AttackSpeed': 15},

                  {'Name': 'Elvegr bow', 'Description': """The tale of this great beautiful
                   carved bow is that it was made by Elvegr race master. This bow is the top
                   of skill. It allows shoot fast and deal a lot damage. What can be better
                   for accurate marksman?""", 'Price': 6381, 'Damage': (17, 20),
                   'AttackSpeed': 15})

constAnyWeapon = (constDaggerWeapon, constSwordWeapon, constAxeWeapon, constSpearWeapon,
                  constGreatSwordWeapon, constHammerWeapon, constBowWeapon)

# armour time!
constClothesArmour = ({'Name': 'Ragged clothes', 'Description': """Old ragged stinky clothes.""",
                       'Price': 50, 'HealthBoost': 0, 'SpeedBoost': 0},

                      {'Name': 'Common clothes', 'Description': """Common clothet that can be
                       found in every house.""", 'Price': 939, 'HealthBoost': 0, 'SpeedBoost': 15},

                      {'Name': 'Hunter clothes', 'Description': """Good quality clothes.
                       good choice to go hunting.""", 'Price': 2350, 'HealthBoost': 0,
                       'SpeedBoost': 30},

                      {'Name': 'Thiefs clothes', 'Description': """Perfect weightless clothes
                       that doesn't constrain movement. Want be faster than shadow?""",
                       'Price': 6264, 'HealthBoost': 0, 'SpeedBoost': 55},

                      {'Name': 'Vampire robe', 'Description': """Cold black robe that smells
                       like death. Some days ago a Vampire has this clothes. Vampires are
                       long-lived creature that moves fast, bites hard.""", 'Price': 9979,
                       'HealthBoost': 0, 'SpeedBoost': 70})

constLightArmour = ({'Name': 'Hide armour', 'Description': """Light armour, that doesn't offer
                     much protection, but you will fell better with it.""", 'Price': 1095,
                     'HealthBoost': 10, 'SpeedBoost': 0},

                    {'Name': 'Studded armour', 'Description': """Light armour, that can offer
                     little protection.""", 'Price': 2662, 'HealthBoost': 20, 'SpeedBoost': 0},

                    {'Name': 'Scaled armour', 'Description': """Light armour, that can offer
                     little protection and cool look.""", 'Price': 6249, 'HealthBoost': 35,
                     'SpeedBoost': 0},

                    {'Name': 'Leather armour', 'Description': """Good armour. It's light,
                     and it offer good protection.""", 'Price': 11506, 'HealthBoost': 49,
                     'SpeedBoost': 0},

                    {'Name': 'Fur armour', 'Description': """Brutal light armour that presents
                     you as strong man that can punish his foes.""", 'Price': 11973,
                     'HealthBoost': 50, 'SpeedBoost': 0})

constHeavyArmour = ({'Name': 'Iron armour', 'Description': """Cheap heavy armour. It's really
                     heavy but it offers nice protection.""", 'Price': 14587, 'HealthBoost': 70,
                     'SpeedBoost': -20},

                    {'Name': 'Steel armour', 'Description': """Good heavy armour. It's really
                     heavy but it offers good protection""", 'Price': 15994, 'HealthBoost': 90,
                     'SpeedBoost': -40},

                    {'Name': 'Mail armour', 'Description': """Shirt that made with thousands
                     iron rings. It's heavy and it offers real protection.""", 'Price': 21785,
                     'HealthBoost': 85, 'SpeedBoost': -25},

                    {'Name': 'Lamellar armour', 'Description': """Heavy armour that made with
                     two layers. First is leather armor, second is made with a lot of steel
                     plates. This armour provides a great protection.""", 'Price': 34682,
                     'HealthBoost': 120, 'SpeedBoost': -50},

                    {'Name': 'Plate armour', 'Description': """Piece of metal. Who can pierce
                     it? Yeah, but it's weight - brrrr.""", 'Price': 75726, 'HealthBoost': 170,
                     'SpeedBoost': -80})

constBerserkerWeapon = ({'Name': 'Dual axes', 'Description': """Good sharpened axes. Professional can use them 
                         with wind speed""", 'Price': 0, 'Damage': (15, 22), 'AttackSpeed': 40}, )
constBerserkerArmour = ({'Name': 'Bear pelt', 'Description': """Fresh pelt from bear. Stinky, warm and bloody.
                         only true berserker can wear it.""", 'Price': 0, 'HealthBoost': 50,
                         'SpeedBoost': 50}, )

constAnyArmour = (constClothesArmour, constLightArmour, constHeavyArmour)

# Hero starting items
constHeroStartWeapon = {'Name': 'Family heirloom sword fragment', 'Description':
                        """It's your family heirloom, this sword fragment is very
                        important for you. You're ready to die for it.""",
                        'Price': 0, 'Damage': (1, 3), 'AttackSpeed': 30}

constHeroStartArmour = {'Name': 'Road robe', 'Description': """Old road robe. You walk a long
                        way with this clothes on.""", 'Price': 0, 'HealthBoost': 0,
                        'SpeedBoost': 0}

# Enemies. They have name, Description, Health, Damage[], Levels[], Gold[],
#  Weapon[][], Armour[][], CommonTrait like {Key: percent} for random generation
constAnimalEnemy = ({'Name': 'Young wolf', 'Description': """You see just common
                     young wolf, that looks hungry and ungry""", 'Health': 30,
                     'Damage': (2, 7), 'Levels': (1, 5), 'Gold': (0,0),
                     'Weapon': (constNoneWeapon, ), 'Armour': (constNoneArmour, ),
                     'CommonTrait': {'Vitality': 0, 'Strength': 0,
                     'Accuracy': 0, 'Luck': 0, 'Agility': 100,
                     'Intelligence': 0, 'Instinct': 0}},

                     {'Name': 'Wolf', 'Description': """You see just common wolf,
                      that looks hungry and ungry""", 'Health': 35,
                      'Damage': (2, 7), 'Levels': (3, 7), 'Gold': (0,0),
                      'Weapon': (constNoneWeapon, ), 'Armour': (constNoneArmour, ),
                      'CommonTrait': {'Vitality': 0, 'Strength': 0,
                      'Accuracy': 0, 'Luck': 0, 'Agility': 100,
                      'Intelligence': 0, 'Instinct': 0}},

                     {'Name': 'Furious wolf', 'Description': """You see strong
                      wolf in fury""", 'Health': 40, 'Damage': (4, 9),
                      'Levels': (6, 10), 'Gold': (0,0),
                      'Weapon': (constNoneWeapon, ), 'Armour': (constNoneArmour, ),
                      'CommonTrait': {'Vitality': 0, 'Strength': 40,
                      'Accuracy': 0, 'Luck': 0, 'Agility': 60,
                      'Intelligence': 0, 'Instinct': 0}},

                     {'Name': 'Young boar', 'Description': """You see just
                      common young boar, that looks hungry""", 'Health': 25,
                      'Damage': (2, 5), 'Levels': (1, 5), 'Gold': (0,0),
                      'Weapon': (constNoneWeapon, ), 'Armour': (constNoneArmour, ),
                      'CommonTrait': {'Vitality': 100, 'Strength': 0,
                      'Accuracy': 0, 'Luck': 0, 'Agility': 0,
                      'Intelligence': 0, 'Instinct': 0}},

                     {'Name': 'Boar', 'Description': """You see just common boar,
                      that looks hungry""", 'Health': 35, 'Damage': (3, 6),
                      'Levels': (3, 7), 'Gold': (0,0), 'Weapon': (constNoneWeapon, ),
                      'Armour': (constNoneArmour, ), 'CommonTrait': {'Vitality': 100,
                      'Strength': 0, 'Accuracy': 0, 'Luck': 0, 'Agility': 0,
                      'Intelligence': 0, 'Instinct': 0}},

                     {'Name': 'Huge boar', 'Description': """You see enormous
                      boar, that looks hungry""", 'Health': 50, 'Damage': (5, 9),
                      'Levels': (6, 10), 'Gold': (0,0),
                      'Weapon': (constNoneWeapon, ),'Armour': (constNoneArmour, ),
                      'CommonTrait': {'Vitality': 50, 'Strength': 0,
                      'Accuracy': 0, 'Luck': 0, 'Agility': 50,
                      'Intelligence': 0, 'Instinct': 0}},

                     {'Name': 'Young bear', 'Description': """You see just
                      common young bear, that looks hungry and ungry""",
                      'Health': 35, 'Damage': (3, 9), 'Levels': (1, 5),
                      'Gold': (0,0), 'Weapon': (constNoneWeapon, ),
                      'Armour': (constNoneArmour, ), 'CommonTrait': {'Vitality': 0,
                      'Strength': 100, 'Accuracy': 0, 'Luck': 0, 'Agility': 0,
                      'Intelligence': 0, 'Instinct': 0}},

                     {'Name': 'Bear', 'Description': """You see just common bear,
                      that looks hungry and ungry""", 'Health': 45,
                      'Damage': (4, 10), 'Levels': (3, 7), 'Gold': (0,0),
                      'Weapon': (constNoneWeapon, ), 'Armour': (constNoneArmour, ),
                      'CommonTrait': {'Vitality': 0, 'Strength': 100,
                      'Accuracy': 0, 'Luck': 0, 'Agility': 0, 'Intelligence': 0,
                      'Instinct': 0}},

                     {'Name': 'Bear in range', 'Description':"""You see old bear
                      in range, that looks very dangerous""", 'Health': 55,
                      'Damage': (5, 12), 'Levels': (6, 10), 'Gold': (0,0),
                      'Weapon': (constNoneWeapon, ), 'Armour': (constNoneArmour, ),
                      'CommonTrait': {'Vitality': 0, 'Strength': 40,
                      'Accuracy': 0, 'Luck': 0, 'Agility': 60, 'Intelligence': 0,
                      'Instinct': 0}})

constEasyEnemy = ({'Name': 'Young thief', 'Description': """You see a thief. He isn't a
                   professional, but he wants your gold.""", 'Health': 50, 'Damage': (1, 3),
                   'Levels': (1, 5), 'Gold': (0, 50), 'Weapon': (constDaggerWeapon, ),
                   'Armour': (constClothesArmour, ), 'CommonTrait': {'Vitality': 0, 'Strength': 0,
                   'Accuracy': 0, 'Luck': 50, 'Agility': 50, 'Intelligence': 0, 'Instinct': 0}},

                  {'Name': 'Thief', 'Description': """You see a thief. Common thief that wants
                   your gold.""", 'Health': 50, 'Damage': (1, 3), 'Levels': (6, 10),
                   'Gold': (0, 100), 'Weapon': (constDaggerWeapon, ),
                   'Armour': (constClothesArmour, ), 'CommonTrait': {'Vitality': 0,
                   'Strength': 0, 'Accuracy': 0, 'Luck': 50, 'Agility': 50, 'Intelligence': 0,
                   'Instinct': 0}},

                  {'Name': 'Master thief', 'Description': """You see a thief. He is well
                   prepeared, and he wants your gold.""", 'Health': 50, 'Damage': (1, 3),
                   'Levels': (11, 15), 'Gold': (50, 250), 'Weapon': (constDaggerWeapon, ),
                   'Armour': (constLightArmour, ), 'CommonTrait': {'Vitality': 0, 'Strength': 0,
                   'Accuracy': 25, 'Luck': 50, 'Agility': 25, 'Intelligence': 0, 'Instinct': 0}},

                  {'Name': 'Robber', 'Description': """You see a robber. He is serious.
                   Where are your golds?""", 'Health': 50, 'Damage': (1, 3), 'Levels': (1, 15),
                   'Gold': (0, 300), 'Weapon': (constSwordWeapon, ), 'Armour': (constLightArmour, ),
                   'CommonTrait': {'Vitality': 30, 'Strength': 20, 'Accuracy': 0, 'Luck': 0,
                   'Agility': 50, 'Intelligence': 0, 'Instinct': 0}},

                  {'Name': 'Bandit', 'Description': """You see a bandit. Just a common bandit.
                   Are you ready?""", 'Health': 50, 'Damage': (1, 3), 'Levels': (1, 15),
                   'Gold': (50, 300), 'Weapon': (constGreatSwordWeapon, constAxeWeapon,
                   constHammerWeapon), 'Armour': (constLightArmour, ),
                   'CommonTrait': {'Vitality': 40, 'Strength': 40, 'Accuracy': 20, 'Luck': 0,
                   'Agility': 0, 'Intelligence': 0, 'Instinct': 0}},

                  {'Name': 'Young hunter', 'Description': """You see a hunter. He is going to
                   hunt you. Wait, what?""", 'Health': 50, 'Damage': (1, 3), 'Levels': (1, 8),
                   'Gold': (0, 50), 'Weapon': (constBowWeapon, ), 'Armour': (constClothesArmour, ),
                   'CommonTrait': {'Vitality': 0, 'Strength': 0, 'Accuracy': 50, 'Luck': 0,
                   'Agility': 50, 'Intelligence': 0, 'Instinct': 0}},

                  {'Name': 'Hunter', 'Description': """You see a hunter. He is going to
                   hunt you. Wait, what?""", 'Health': 50, 'Damage': (1, 3), 'Levels': (7, 15),
                   'Gold': (0, 50), 'Weapon': (constBowWeapon, ), 'Armour': (constLightArmour, ),
                   'CommonTrait': {'Vitality': 0, 'Strength': 0, 'Accuracy': 40, 'Luck': 20,
                   'Agility': 40, 'Intelligence': 0, 'Instinct': 0}},

                  {'Name': 'Skeleton', 'Description': """You see a skeleton. Common skeleton,
                   but it's going to kill you. Yeah, it's armed and goes right to you.""",
                   'Health': 30, 'Damage': (1, 3), 'Levels': (1, 15), 'Gold': (0, 0),
                   'Weapon': constAnyWeapon, 'Armour': (constNoneArmour, ),
                   'CommonTrait': {'Vitality': 50, 'Strength': 25, 'Accuracy': 25, 'Luck': 0,
                   'Agility': 0, 'Intelligence': 0, 'Instinct': 0}})

constMediumEnemy = ({'Name': 'Thug', 'Description': """You see a thug. He is going to cut your
                     head off.""", 'Health': 50, 'Damage': (1, 3), 'Levels': (16, 30),
                     'Gold': (100, 500), 'Weapon': (constSwordWeapon, ),
                     'Armour': (constHeavyArmour, ), 'CommonTrait': {'Vitality': 35,
                     'Strength': 35, 'Accuracy': 30, 'Luck': 0, 'Agility': 0,
                     'Intelligence': 0, 'Instinct': 0}},

                     {'Name': 'Highwayman', 'Description': """You see a highwayman. He's high,
                      he's on your way and he's man.""", 'Health': 50, 'Damage': (1, 3),
                      'Levels': (16, 30), 'Gold': (100, 500), 'Weapon': (constDaggerWeapon, ),
                      'Armour': (constLightArmour, ), 'CommonTrait': {'Vitality': 35,
                      'Strength': 0, 'Accuracy': 0, 'Luck': 30, 'Agility': 35,
                      'Intelligence': 0, 'Instinct': 0}},

                     {'Name': 'Goon', 'Description': """You see a goon. He's goin to have some
                      fun.""", 'Health': 50, 'Damage': (1, 3), 'Levels': (16, 30),
                      'Gold': (100, 500), 'Weapon': (constGreatSwordWeapon, constHammerWeapon),
                      'Armour': (constHeavyArmour, ), 'CommonTrait': {'Vitality': 30,
                      'Strength': 30, 'Accuracy': 15, 'Luck': 0, 'Agility': 25,
                      'Intelligence': 0, 'Instinct': 0}},

                     {'Name': 'Ghost', 'Description': """You see a ghost. Just common undead
                      creature that is going to check your vitality.""", 'Health': 100,
                      'Damage': (3, 7), 'Levels': (16, 30), 'Gold': (0, 0),
                      'Weapon': (constNoneWeapon, ), 'Armour': (constNoneArmour, ),
                      'CommonTrait': {'Vitality': 0, 'Strength': 0, 'Accuracy': 60, 'Luck': 15,
                      'Agility': 25, 'Intelligence': 0, 'Instinct': 0}})

constHardEnemy = ({'Name': 'Troll', 'Description': """You see a enormous troll. He is going to have a breakfast. 
                     You\'re so tasty!""", 'Health': 200, 'Damage': (10, 25), 'Levels': (30, 50),
                     'Gold': (0, 0), 'Weapon': (constNoneWeapon, ),
                     'Armour': (constNoneArmour, ), 'CommonTrait': {'Vitality': 30,
                     'Strength': 35, 'Accuracy': 25, 'Luck': 0, 'Agility': 0,
                     'Intelligence': 0, 'Instinct': 10}}, )

constUniqueEnemy = ({'Name': 'Berserker in range', 'Description': """You see a berserker in range. He\'s crashing 
                     everything on his way. You\'re next!""", 'Health': 50, 'Damage': (1, 3), 'Levels': (50, 50),
                     'Gold': (0, 0), 'Weapon': (constBerserkerWeapon, ),
                     'Armour': (constBerserkerArmour, ), 'CommonTrait': {'Vitality': 20,
                     'Strength': 25, 'Accuracy': 20, 'Luck': 5, 'Agility': 20,
                     'Intelligence': 0, 'Instinct': 0}}, )

constArenaDueler = ({'Name': 'Dueler', 'Description': "", 'Health': 50,
                     'Damage': (1, 3), 'Gold': (0, 0),
                     'Weapon': (constDaggerWeapon, constBowWeapon),
                     'Armour': (constClothesArmour, constLightArmour ),
                     'CommonTrait': {'Vitality': 0, 'Strength': 0, 'Accuracy': 50,
                     'Agility': 50, 'Intelligence': 0}},

                    {'Name': 'Dueler', 'Description': "", 'Health': 50,
                     'Damage': (1, 3), 'Gold': (0, 0),
                     'Weapon': (constSwordWeapon, constAxeWeapon, constSpearWeapon),
                     'Armour': constAnyArmour,
                     'CommonTrait': {'Vitality': 50, 'Strength': 50, 'Accuracy': 0,
                     'Agility': 0, 'Intelligence': 0}},

                    {'Name': 'Dueler', 'Description': "", 'Health': 50,
                     'Damage': (1, 3), 'Gold': (0, 0),
                     'Weapon': (constGreatSwordWeapon, constHammerWeapon),
                     'Armour': constAnyArmour,
                     'CommonTrait': {'Vitality': 0, 'Strength': 50, 'Accuracy': 0,
                     'Agility': 50, 'Intelligence': 0}})
