# ------------------------------------------------------------------------------
# Copyright © 2017 Daniil Nepryahin
# contacts: <nervoidaz@yandex.ru>
# License: https://opensource.org/licenses/cpl1.0.php
# ------------------------------------------------------------------------------


# File with useful functional

# to make random choices
from random import randint, choice
# to save data to file
from pickle import dump, load
# to check file exists
import os.path
# need for PlaceMenu function
from collections import OrderedDict
from AdConstFile import *


class clWeapon:
    """ Weapon class
        There is wpGeneralParam with keys:
        str Name
        str Description
        int MinDamage, MaxDamage
        int AttackSpeed
        methods:
        wpShowInfo()
    """

    __wpGeneralParam = 0
    def __init__(self, Name = 'None', Description = '', Price = 0, MinDamage = 0,
                 MaxDamage = 0, AttackSpeed = 0):
        self.__wpGeneralParam = dict()
        self.__wpGeneralParam['Name'] = Name
        self.__wpGeneralParam['Description'] = Description
        self.__wpGeneralParam['Price'] = Price
        self.__wpGeneralParam['MinDamage'] = MinDamage
        self.__wpGeneralParam['MaxDamage'] = MaxDamage
        self.__wpGeneralParam['AttackSpeed'] = AttackSpeed
    def __getitem__(self, key):
        return self.__wpGeneralParam[key]
    def __setitem__(self, key, val):
        self.__wpGeneralParam[key] = val
    def __eq__(self, other):
        res = 1
        for key in self.__wpGeneralParam.keys():
            res = res and self.__wpGeneralParam[key] == other.__wpGeneralParam[key]
        return res

    def wpShowInfo(self):
        ''' Just show info about Weapon '''
        print(self.__wpGeneralParam['Name'])
        print(self.__wpGeneralParam['Description'])
        print('Damage:', str(self.__wpGeneralParam['MinDamage']) + '-' +
              str(self.__wpGeneralParam['MaxDamage']))
        print('Attack speed:', self.__wpGeneralParam['AttackSpeed'])
        print('Price:', self.__wpGeneralParam['Price'])

class clArmour:
    """ Armour class
        There is arGeneralParam with keys:
        str Name
        str Descriotion
        int HealthBoost, SpeedBoost
        methods:
        arShowInfo()
    """
    __arGeneralParam = 0
    def __init__(self, Name = 'None', Description = '', Price = 0,
                 HealthBoost = 0, SpeedBoost = 0):
        self.__arGeneralParam = dict()
        self.__arGeneralParam['Name'] = Name
        self.__arGeneralParam['Description'] = Description
        self.__arGeneralParam['Price'] = Price
        self.__arGeneralParam['HealthBoost'] = HealthBoost
        self.__arGeneralParam['SpeedBoost'] = SpeedBoost
    def __getitem__(self, key):
        return self.__arGeneralParam[key]
    def __setitem__(self, key, val):
        self.__arGeneralParam[key] = val
    def __eq__(self, other):
        res = 1
        for key in self.__arGeneralParam.keys():
            res = res and self.__arGeneralParam[key] == other.__arGeneralParam[key]
        return res

    def arShowInfo(self):
        ''' Just show info about Weapon '''
        print(self.__arGeneralParam['Name'])
        print(self.__arGeneralParam['Description'])
        print('Health modifier:', self.__arGeneralParam['HealthBoost'])
        print('Speed modifier:', self.__arGeneralParam['SpeedBoost'])
        print('Price:', self.__arGeneralParam['Price'])

def chHowMuchExpNeed(CurLvL):
    ''' Show how much experience Character needs for new Level
        Just interesting formula.
        Exec it on the loop and see what it return. It's nice.
    '''
    if CurLvL <= 1:
        return 0
    else:
        if CurLvL//10 == 0:
            k = 5
        else:
            k = CurLvL//10*10
        return chHowMuchExpNeed(CurLvL-1) + k

def WhatWillHappen(DictOfEvents):
    ''' Count probability of Events in Keys of DictOfEvents with
        percents as Value
        If nothing will happen => return 0
        Samples (Just show that's it work and how, don't show
        all functions calling):
        >>> a = {'KeK':100}
        >>> b = {'LoL': 100, 'SES':200}
        >>> c = {'Yeah': 50, 'Wow':15}
        >>> d = {'int': 15, 'float': 45, 'dict': 40}
        >>> WhatWillHappen(a)
            'KeK'
        >>> WhatWillHappen(b)
            'LoL'
        >>> WhatWillHappen(c)
            0
        >>> WhatWillHappen(c)
            'Yeah'
        >>> WhatWillHappen(c)
            'Wow'
        >>> WhatWillHappen(d)
            'float'
        >>> WhatWillHappen(d)
            'dict'
        >>> WhatWillHappen(d)
            'int'
    '''
    randomNumber = randint(1, 10000)
    curPerc = 0
    for key in DictOfEvents.keys():
        if randomNumber <= (curPerc + DictOfEvents[key]) * 100:
            return key
        else:
            curPerc += DictOfEvents[key]
    return 0

class clCharacter:
    """ Character class
        There are:
        chGeneralParams:
        str Name - name of Character
        str Description - description of Character (Just for Enemy)
        int CHealth, MHealth - Current and Max Health of Character
        int MinDamage, MaxDamage - damage of Character
        int MaxPotion, PotionSlots[int HealthRestore, IncDamage] - max count that Character can carry
        and Count of each poison types
        int PotionRestore - how much potion can restore points
        int Gold - gold of Character
        int Level - Level of character
        int Experience - experience of Character
        clWeapon chWeapon - weapon that character uses
        clArmour chArmour - armour that character wears
        int HitChance - chance to hit the enemy
        int AttackSpeed - if you have A*[Enemy]chAttackSpeed then you hit A times
        int FindChance - chance to find interesting in others places
        int KnowChance - chance to know something interesting from people
        int FleeChance - chance to flee from dead figth
        int BattleRestore - percent of chHelth restore after every battle

        Every new level player gets 1 point. At the first level player has 3 points
        You can increase next chCommonTrait:
        int Vitality - each point increase chHealth by 5
        int Strength - each point increase chDamage by 2
        int Accuracy - each point increase chHitChance by 5
        int Luck - who has more chLuck that smashes enemy the first
        int Agility - each point increase chAttackSpeed by 10
        int Attention - each point increase chFindChance by 10
        int Charisma - each point increase chKnowChance by 10
        int Intelligence - each point increase chPotionRestore by 1
        int Instinct - each point increase chFleeChance by 10

        Every 10 levels player gets 1 point to spend it to chSpecialTrait:
        int Undead - every point increase chHealth by 20
        int Carrier - every point increase chMaxPotions by 2
        int QuickHand - every point increase chSpeed by 50
        int OnePunch - every point increase chDamage by 8
        int Physician - every point increase chBattleRestore by 16
        int Trader - character gets 10000 Golds

        Methods:
        chShowInfo(Param); Param = 0, 1, 2, 3
            This method for Hero, so there isn't Description that will be used
            only for Enemy. Info about Enemy we will get with chGetGeneralParam
        chIncreaseCommonTrait(CommonTraitKey); Key is from chCommonTrait
        chIncreaseSpecialTrait(SpecialTraitKey); same
        chSetCommonTrait(key, value); chSetSpecialTrait(key, value) => just set
        chRemoveWeapon(Weapon); chRemoveArmour(Armour)
        chAddWeapon(NewWeapon); chAddArmour(NewArmour)
        chGetWeapon(); chGetArmour() => returns current equipment
        chHealthRestore(modifier); modifier = 0 => Restore value of BattleRestore
             otherwise full restoration
        chChangeGeneralParam(Key, Value); Key from chGeneralParam
        chSetGeneralParam(Key, value);
        chGetGeneralParam(Key) => return Value of GeneralParam[Key] or -1 in
            case of error
        chGetCommonTrait(Key); chGetSpecialTrait(Key) => same
        chDoHit() => return Damage that Character delivers in that time
        chDrinkPotion(Type) => type = 0 for Damage; = 1 for Healing
        IT DOESN'T RETURN DAMAGE BACK AFTER HIT! Just drink and no more deals
        chDisappearPotion() => set Damage back to normal
        !!!How to use: Drink -> Hit -> Disappear!!!
        One more IMPORTANT INFO: be sure that Character has potions, methods don't
        check it. You can use chGetGeneralParam('PotionSlots')[i] i = 0 or 1
    """
    # define class fields
    __chGeneralParam = 0
    __chCommonTrait = 0
    __chSpecialTrait = 0
    def __init__(self, Name = '', Description = '', Health = 50, MinDamage = 1,
                 MaxDamage = 3, MaxPotion = 5, PotionSlots = [0, 0],
                 PotionRestore = 1, Gold = 100, Level = 0, Experience = 0,
                 Weapon = clWeapon(), Armour = clArmour(), HitChance = 50,
                 AttackSpeed = 100, FindChance = 0, KnowChance = 0, FleeChance = 0,
                 BattleRestore = 20, Vitality = 0, Strength = 0, Luck = 0,
                 Agility = 0, Accuracy = 0, Attention = 0, Charisma = 0,
                 Intelligence = 0, Instinct = 0, Undead = 0, Carrier = 0,
                 QuickHand = 0, OnePunch = 0, Physician = 0, Trader = 0):
        self.__chGeneralParam = dict()
        self.__chGeneralParam['Name'] = Name
        self.__chGeneralParam['Description'] = Description
        # when we create Character current and max health are equal
        self.__chGeneralParam['CHealth'] = Health
        self.__chGeneralParam['MHealth'] = Health
        self.__chGeneralParam['MinDamage'] = MinDamage
        self.__chGeneralParam['MaxDamage'] = MaxDamage
        self.__chGeneralParam['MaxPotion'] = MaxPotion
        self.__chGeneralParam['PotionSlots'] = PotionSlots
        self.__chGeneralParam['PotionRestore'] = PotionRestore
        self.__chGeneralParam['Gold'] = Gold
        self.__chGeneralParam['Level'] = Level
        self.__chGeneralParam['Experience'] = Experience
        self.__chGeneralParam['HitChance'] = HitChance
        self.__chGeneralParam['AttackSpeed'] = AttackSpeed
        self.__chGeneralParam['FindChance'] = FindChance
        self.__chGeneralParam['KnowChance'] = KnowChance
        self.__chGeneralParam['FleeChance'] = FleeChance
        self.__chGeneralParam['BattleRestore'] = BattleRestore
        self.__chWeapon = Weapon
        self.__chArmour = Armour

        self.__chCommonTrait = dict()
        self.__chCommonTrait['Vitality'] = Vitality
        self.__chCommonTrait['Strength'] = Strength
        self.__chCommonTrait['Luck'] = Luck
        self.__chCommonTrait['Agility'] = Agility
        self.__chCommonTrait['Accuracy'] = Accuracy
        self.__chCommonTrait['Attention'] = Attention
        self.__chCommonTrait['Charisma'] = Charisma
        self.__chCommonTrait['Intelligence'] = Intelligence
        self.__chCommonTrait['Instinct'] = Instinct

        self.__chSpecialTrait = dict()
        self.__chSpecialTrait['Undead'] = Undead
        self.__chSpecialTrait['Carrier'] = Carrier
        self.__chSpecialTrait['QuickHand'] = QuickHand
        self.__chSpecialTrait['OnePunch'] = OnePunch
        self.__chSpecialTrait['Physician'] = Physician
        self.__chSpecialTrait['Trader'] = Trader

    def chShowInfo(self, Param = 0):
        ''' Param - how much info you need
            Param = 0 shows you only General params
            Param = 1 shows you only Character Traits
            Param = 2 show you only Character Special Traits
            Param = 3 show you every param
        '''
        if Param == 0 or Param == 3:
            print("Name:", self.__chGeneralParam['Name'], " "*5,
                  "Level:", self.__chGeneralParam['Level'], " "*5,
                  "Exp:", str(self.__chGeneralParam['Experience']) + '/' +
                  str(chHowMuchExpNeed(self.__chGeneralParam['Level'] + 1)), " "*5,
                  "Gold:", self.__chGeneralParam['Gold'])
            print("Health:", str(self.__chGeneralParam['CHealth']) + '/' + str(
                  self.__chGeneralParam['MHealth']))
            print("Damage:", self.__chGeneralParam['MinDamage'],
                  "-", self.__chGeneralParam['MaxDamage'])
            print("Weapon:", self.__chWeapon['Name'])
            print("Armour:", self.__chArmour['Name'])
            print("Potions: Healing", str(self.__chGeneralParam['PotionSlots'][0])+
                  "/"+str(self.__chGeneralParam['MaxPotion'])+ "; Damage "+
                  str(self.__chGeneralParam['PotionSlots'][1])+"/"+
                  str(self.__chGeneralParam['MaxPotion']))
            print("Each potion gives +" + str(self.__chGeneralParam['PotionRestore']))
            print("Attack speed:", self.__chGeneralParam['AttackSpeed'],
                  " "*5, "Hit Chance:", self.__chGeneralParam['HitChance'])
            print("Chance to know something interesting from people:",
                  self.__chGeneralParam['KnowChance'])
            print("Chance to find something interesting in the area:",
                  self.__chGeneralParam['FindChance'])
            print("Chance to flee from figth:", self.__chGeneralParam['FleeChance'])
            print(str(self.__chGeneralParam['BattleRestore'])+"%"+" will heal after every battle")
        if Param == 1 or Param == 3:
            print(self.__chGeneralParam['Name'], "has next traits:")
            print("Vitality:", self.__chCommonTrait['Vitality'])
            print("Strength:", self.__chCommonTrait['Strength'])
            print("Accuracy:", self.__chCommonTrait['Accuracy'])
            print("Luck:", self.__chCommonTrait['Luck'])
            print("Agility:", self.__chCommonTrait['Agility'])
            print("Attention:", self.__chCommonTrait['Attention'])
            print("Charisma:", self.__chCommonTrait['Charisma'])
            print("Intelligence:", self.__chCommonTrait['Intelligence'])
            print("Instinct:", self.__chCommonTrait['Instinct'])
        if Param == 2 or Param == 3:
            if (not self.__chSpecialTrait['Undead'] and not self.__chSpecialTrait['Carrier']
                and not self.__chSpecialTrait['QuickHand'] and not self.__chSpecialTrait['OnePunch']
                and not self.__chSpecialTrait['Physician'] and not self.__chSpecialTrait['Trader']):
                print(self.__chGeneralParam['Name'], "has no special traits.")
            else:
                print(self.__chGeneralParam['Name'], "has next special traits:")
            if self.__chSpecialTrait['Undead'] != 0:
                print("Undead with", self.__chSpecialTrait['Undead'], "power")
            if self.__chSpecialTrait['Carrier'] != 0:
                print("Carrier with", self.__chSpecialTrait['Carrier'], "power")
            if self.__chSpecialTrait['QuickHand'] != 0:
                print("Quick Hand with", self.__chSpecialTrait['QuickHand'], "power")
            if self.__chSpecialTrait['OnePunch'] != 0:
                print("One Punch with", self.__chSpecialTrait['OnePunch'], "power")
            if self.__chSpecialTrait['Physician'] != 0:
                print("Physician with", self.__chSpecialTrait['Physician'], "power")
            if self.__chSpecialTrait['Trader'] != 0:
                print("Trader with", self.__chSpecialTrait['Trader'], "power")

    def chIncreaseCommonTrait(self, CommonTraitKey):
        ''' Method increase choosen chCommonTrait
            by CommonTraitKey
        '''
        # just a lot of 'if'
        if CommonTraitKey in self.__chCommonTrait.keys():
            self.__chCommonTrait[CommonTraitKey] += 1
            if CommonTraitKey == 'Vitality':
                self.__chGeneralParam['MHealth'] += 5
            elif CommonTraitKey == 'Strength':
                self.__chGeneralParam['MinDamage'] += 2
                self.__chGeneralParam['MaxDamage'] += 2
            elif CommonTraitKey == 'Agility':
                self.__chGeneralParam['AttackSpeed'] += 10
            elif CommonTraitKey == 'Accuracy':
                self.__chGeneralParam['HitChance'] += 5
            elif CommonTraitKey == 'Attention':
                self.__chGeneralParam['FindChance'] += 10
            elif CommonTraitKey == 'Charisma':
                self.__chGeneralParam['KnowChance'] += 10
            elif CommonTraitKey == 'Intelligence':
                self.__chGeneralParam['PotionRestore'] += 1
            elif CommonTraitKey == 'Instinct':
                self.__chGeneralParam['FleeChance'] += 10
        else:
            print("Imposible to improve", CommonTraitKey)

    def chIncreaseSpecialTrait(self, SpecialTraitKey):
        ''' Method increase choosen chSpecialTrait
            by SpecialTraitKey
        '''
        # if if if if if if ... if
        if SpecialTraitKey in self.__chSpecialTrait.keys():
            self.__chSpecialTrait[SpecialTraitKey] += 1
            if SpecialTraitKey == 'Undead':
                self.__chGeneralParam['MHealth'] += 20
            elif SpecialTraitKey == 'Carrier':
                self.__chGeneralParam['MaxPotion'] += 2
            elif SpecialTraitKey == 'QuickHand':
                self.__chGeneralParam['AttackSpeed'] += 50
            elif SpecialTraitKey == 'OnePunch':
                self.__chGeneralParam['MinDamage'] += 8
                self.__chGeneralParam['MaxDamage'] += 8
            elif SpecialTraitKey == 'Physician':
                self.__chGeneralParam['BattleRestore'] += 16
            elif SpecialTraitKey == 'Trader':
                self.__chGeneralParam['Gold'] += 10000
        else:
            print("Imposible to improve", SpecialTraitKey)

    def chRemoveWeapon(self, OldWeapon):
        ''' This method removes OldWeapon from Character
            change Character's params and set Weapon to None
        '''
        self.__chGeneralParam['MinDamage'] -= OldWeapon['MinDamage']
        self.__chGeneralParam['MaxDamage'] -= OldWeapon['MaxDamage']
        self.__chGeneralParam['AttackSpeed'] -= OldWeapon['AttackSpeed']
        self.__chWeapon = clWeapon()

    def chAddWeapon(self, NewWeapon, SetFlag = 0):
        ''' This method adds NewWeapon to Character
            First, we should remove weapon from character and next we can
            change Character's params and set Weapon to NewWeapon
        '''
        self.chRemoveWeapon(self.__chWeapon)
        self.__chWeapon = NewWeapon
        if not SetFlag:
            self.__chGeneralParam['MinDamage'] += NewWeapon['MinDamage']
            self.__chGeneralParam['MaxDamage'] += NewWeapon['MaxDamage']
            self.__chGeneralParam['AttackSpeed'] += NewWeapon['AttackSpeed']

    def chGetWeapon(self):
        ''' This method return Character current Weapon '''
        return self.__chWeapon

    def chRemoveArmour(self, OldArmour):
        ''' This method removes OldArmour from Character
            change Character's params and set Armour to None
        '''
        self.__chGeneralParam['MHealth'] -= OldArmour['HealthBoost']
        self.__chGeneralParam['AttackSpeed'] -= OldArmour['SpeedBoost']
        self.__chArmour = clArmour()

    def chAddArmour(self, NewArmour, SetFlag = 0):
        ''' This method adds NewArmour to Character
            First, we should remove weapon from character and next we can
            change Character's params and set Armour to NewArmour
        '''
        self.chRemoveArmour(self.__chArmour)
        self.__chArmour = NewArmour
        if not SetFlag:
            self.__chGeneralParam['MHealth'] += NewArmour['HealthBoost']
            self.__chGeneralParam['AttackSpeed'] += NewArmour['SpeedBoost']

    def chGetArmour(self):
        ''' This method return Character current Armour '''
        return self.__chArmour

    def chHealthRestore(self, modifier = 0):
        ''' Restore character health.
            If modifier = 0, then restore value of BattleRestore
            else full restoration
        '''
        if not modifier:
            self.__chGeneralParam['CHealth'] += int(self.__chGeneralParam['BattleRestore'] *
                                                    self.__chGeneralParam['MHealth'] / 100)
            if self.__chGeneralParam['CHealth'] > self.__chGeneralParam['MHealth']:
                self.__chGeneralParam['CHealth'] = self.__chGeneralParam['MHealth']
        else:
            self.__chGeneralParam['CHealth'] = self.__chGeneralParam['MHealth']

    def chChangeGeneralParam(self, Key, value = 1):
        ''' Change chGeneralParam[Key] with value '''
        if Key in self.__chGeneralParam.keys():
            self.__chGeneralParam[Key] += value
        else:
            print('Enable to change', Key)

    def chSetGeneralParam(self, Key, value = 0):
        ''' Set chGeneralParam[Key] to value '''
        if Key in self.__chGeneralParam.keys():
            self.__chGeneralParam[Key] = value
        else:
            print('Enable to set', Key)


    def chGetGeneralParam(self, Key):
        ''' return GeneralParam by Key '''
        if Key in self.__chGeneralParam.keys():
            return self.__chGeneralParam[Key]
        else:
            return -1

    def chGetCommonTrait(self, Key):
        ''' return CommonTrait by Key '''
        if Key in self.__chCommonTrait.keys():
            return self.__chCommonTrait[Key]
        else:
            return -1

    def chSetCommonTrait(self, Key, value = 0):
        ''' Set chCommonTrait[Key] to value '''
        if Key in self.__chCommonTrait.keys():
            self.__chCommonTrait[Key] = value
        else:
            print('Enable to set', Key)

    def chGetSpecialTrait(self, Key):
        ''' return SpecialTrait by Key '''
        if Key in self.__chSpecialTrait.keys():
            return self.__chSpecialTrait[Key]
        else:
            return -1

    def chSetSpecialTrait(self, Key, value = 0):
        ''' Set chSpecialTrait[Key] to value '''
        if Key in self.__chSpecialTrait.keys():
            self.__chSpecialTrait[Key] = value
        else:
            print('Enable to set', Key)

    def chDoHit(self):
        ''' Let's smash our enemies!
            return delivered Damage. It can be 0, if Character missed
        '''
        res = 0
        # let's check, can we hit or not
           # return 1 if Character can hit
        if WhatWillHappen({1: self.__chGeneralParam['HitChance']}):
            res = randint(self.__chGeneralParam['MinDamage'],
                          self.__chGeneralParam['MaxDamage'])
        return res

    def chDrinkPotion(self, PotionType):
        ''' It's time to drink potions!
            PotionType = 0 for Healing and 1 for Damaging
            We just drink potion and increase params of hero
            !Don't forget to set Damage back after drinking!
            !This method don't check count of Potions, so be sure that you have
            more than 0 Potions!
        '''
        if PotionType:
            self.__chGeneralParam['MinDamage'] += self.__chGeneralParam['PotionRestore']
            self.__chGeneralParam['MaxDamage'] += self.__chGeneralParam['PotionRestore']
            self.__chGeneralParam['PotionSlots'][1] -= 1
        else:
            self.__chGeneralParam['CHealth'] += self.__chGeneralParam['PotionRestore']
            self.__chGeneralParam['PotionSlots'][0] -= 1
    def chDisappearPotion(self):
        ''' potion effect is disappeared. As you can guess, it works for
            Damage PotionRestore
        '''
        self.__chGeneralParam['MinDamage'] -= self.__chGeneralParam['PotionRestore']
        self.__chGeneralParam['MaxDamage'] -= self.__chGeneralParam['PotionRestore']


def EnemyGenerationByTrip(TripType, HeroLvl = 25):
    ''' Function that return Enemy. Enemy is choosen by TripType (look at
        AdConstFile). It can be constEasyTrip, constMediumTrip, constHardTrip,
        constVeryHardTrip, constForestTrip, constArenaAnimal. It also can be
        equal ArenaE, ArenaM, ArenaH for difficult of Arena. First, choose
        EnemyType, then create Enemy and return it.
    '''
    # So let's choose EnemyType:
    resEnemy = -1
    EnemyInfo = -1
    if TripType not in ('ArenaE', 'ArenaM', 'ArenaH'):
        EnemyType = WhatWillHappen(TripType)
        if EnemyType == 'EasyEnemy':
            EnemyInfo = choice(constEasyEnemy)
        elif EnemyType == 'MediumEnemy':
            EnemyInfo = choice(constMediumEnemy)
        elif EnemyType == 'AnimalEnemy':
            EnemyInfo = choice(constAnimalEnemy)
        elif EnemyType == 'HardEnemy':
            EnemyInfo = choice(constHardEnemy)
        elif EnemyType == 'UniqueEnemy':
            EnemyInfo = choice(constUniqueEnemy)
        else:
            print("Error! Enable to choice Enemy.")
            return resEnemy
    else:
        EnemyType = constArenaDueler
        EnemyInfo = choice(EnemyType)
        mLvl = 0
        xLvl = 0
        # auto leveling
        if TripType == 'ArenaE':
            mLvl = (1 if HeroLvl - 5 <= 1 else HeroLvl - 5)
            xLvl = HeroLvl
        elif TripType == 'ArenaM':
            mLvl = HeroLvl
            xLvl = (50 if HeroLvl + 5 >= 50 else HeroLvl + 5)
        elif TripType == 'ArenaH':
            mLvl = (50 if HeroLvl + 5 >= 50 else HeroLvl + 5)
            xLvl = 50
        DueLvl = (mLvl, xLvl)
        EnemyInfo['Levels'] = DueLvl
    # fill enemy params
    resEnemy = clCharacter(EnemyInfo['Name'], EnemyInfo['Description'],
                           EnemyInfo['Health'], EnemyInfo['Damage'][0],
                           EnemyInfo['Damage'][1])
    lvl = randint(EnemyInfo['Levels'][0], EnemyInfo['Levels'][1])
    resEnemy.chSetGeneralParam('Level', lvl)
    gld = randint(EnemyInfo['Gold'][0], EnemyInfo['Gold'][1])
    resEnemy.chSetGeneralParam('Gold', gld)
    weapInfo = choice(choice(EnemyInfo['Weapon']))
    EnWeap = clWeapon(weapInfo['Name'], weapInfo['Description'],
                      weapInfo['Price'], weapInfo['Damage'][0],
                      weapInfo['Damage'][1], weapInfo['AttackSpeed'])
    resEnemy.chAddWeapon(EnWeap)
    armInfo = choice(choice(EnemyInfo['Armour']))
    EnArm = clArmour(armInfo['Name'], armInfo['Description'], armInfo['Price'],
                     armInfo['HealthBoost'], armInfo['SpeedBoost'])
    resEnemy.chAddArmour(EnArm)
    # let's train our Enemy
    traitPoint = lvl + 2
    spTraitPoint = lvl // 10
    traits = ['Vitality', 'Strength', 'Accuracy', 'Luck', 'Agility', 'Intelligence',
              'Instinct']
    spTraits = ['Undead', 'Carrier', 'QuickHand', 'OnePunch', 'Trader']
    # remove useless traits for arena
    if TripType in ('ArenaE', 'ArenaM', 'ArenaH'):
        traits.remove('Luck')
        traits.remove('Instinct')
        spTraits.remove('Trader')
    traitsProb = {}
    for keys in EnemyInfo['CommonTrait'].keys():
        traitsProb[keys] = EnemyInfo['CommonTrait'][keys]
    # so now we have more points than we can spend, so choose useless traits
    if TripType in ('ArenaE', 'ArenaM', 'ArenaH') and traitPoint > 50:
        for i in range(0, traitPoint - 50):
            resEnemy.chIncreaseCommonTrait(choice(('Luck', 'Instinct')))
            traitPoint -= 1
    while traitPoint > 0:
        impTr = WhatWillHappen(traitsProb)
        if impTr in traits:
            resEnemy.chIncreaseCommonTrait(impTr)
            traitPoint -= 1
            if resEnemy.chGetCommonTrait(impTr) == 10:
                traits.remove(impTr)
                # it's max size of common trait, so let's recount probability
                # when we spend all our points for arena we will try to recount
                # probability, that is an error. So:
                if traitPoint != 0:
                    probofTrait = traitsProb[impTr]
                    for k in range(1, probofTrait + 1):
                        traitsProb[impTr] -= 1
                        traitsProb[choice(traits)] += 1
    while spTraitPoint > 0:
        resEnemy.chIncreaseSpecialTrait(choice(spTraits))
        spTraitPoint -= 1
    # and give to Enemy some Potions
    if EnemyInfo in constAnimalEnemy:
        # animal can't use potions
        hlPtn = 0
        dmgPtn = 0
    else:
        hlPtn = randint(0, resEnemy.chGetGeneralParam('MaxPotion') + 1)
        dmgPtn = randint(0, resEnemy.chGetGeneralParam('MaxPotion') + 1)
    resEnemy.chSetGeneralParam('PotionSlots', [hlPtn, dmgPtn])
    # and we should set health of enemy to MAX
    resEnemy.chSetGeneralParam('CHealth', resEnemy.chGetGeneralParam('MHealth'))
    return resEnemy

def HeroNewLevel(Hero):
    ''' Function that makes all durty work to increase Hero lvl '''
    print('NEW LEVEL!')
    # first we need to change current Hero Experience
    exp = (Hero.chGetGeneralParam('Experience') -
           chHowMuchExpNeed(Hero.chGetGeneralParam('Level') + 1))
    Hero.chChangeGeneralParam('Level', 1)
    Hero.chSetGeneralParam('Experience', exp)
    # idea is: if hero has full health then after lvl up he will be with full health
    # if hero was healthy then he will be healthy, but if he was bitten then he
    # can't be healthy after lvl up.
    FullHealthFlag = (1 if Hero.chGetGeneralParam('CHealth') == Hero.chGetGeneralParam('MHealth')
                      else 0)
    # on 1st lvl Hero gets 3 points
    points = (3 if Hero.chGetGeneralParam('Level') == 1 else 1)
    # every 10 lvl Hero gets 1 point to increase Special Trait
    spoints = (1 if Hero.chGetGeneralParam('Level') // 10 > 0 and
               Hero.chGetGeneralParam('Level') % 10 == 0 else 0)
    while points > 0:
        print('You have', points, 'Trait Points')
        print('Your traits:')
        for key in constCommonTraits:
            print(key, Hero.chGetCommonTrait(key))
        print("What would you like to increase?")
        trait = input('[> ').lower().capitalize()
        if trait in constCommonTraits:
            if Hero.chGetCommonTrait(trait) == 10:
                print('Max level of', trait)
            else:
                Hero.chIncreaseCommonTrait(trait)
                points -= 1
        else:
            print('There is no', trait + '. Try again!')
    while spoints > 0:
        print('You have', spoints, 'Special Trait Points')
        print("It's time to decide what you want to improve.")
        print('1. You want to be a healthfuly man with a good health')
        print('2. You want to be a strong man, who can carry more weight')
        print('3. You are enviouse of the wind, so you want to be faster')
        print('4. You prefer a power, so you want to deliver more damage')
        print('5. Life is what we need, so you want to learn about restoration')
        print('6. Everithing in the world can be bought, so you want to have G O L D')
        strait = input('You decide [> ')
        if strait == '1':
            Hero.chIncreaseSpecialTrait('Undead')
            spoints -= 1
        elif strait == '2':
            Hero.chIncreaseSpecialTrait('Carrier')
            spoints -= 1
        elif strait == '3':
            Hero.chIncreaseSpecialTrait('QuickHand')
            spoints -= 1
        elif strait == '4':
            Hero.chIncreaseSpecialTrait('OnePunch')
            spoints -= 1
        elif strait == '5':
            Hero.chIncreaseSpecialTrait('Physician')
            spoints -= 1
        elif strait == '6':
            Hero.chIncreaseSpecialTrait('Trader')
            spoints -= 1
        else:
            print('There is no option to choose', strait + '''. Be careful, use only digits!''')
    if FullHealthFlag:
        Hero.chSetGeneralParam('CHealth', Hero.chGetGeneralParam('MHealth'))

def NewGame():
    ''' Function to start new game. It's create character for hero, create File
        constDataFileName (see in AdConstFile).
        Return (clCharacter, Inventory), where
        Inventory = (list of Weapon, list of Armour)
    '''
    Params = {'Place': constCityPlace}
    Hero = clCharacter()
    HeroWeapons = []
    HeroArmours = []
    startWeapon = clWeapon(constHeroStartWeapon['Name'], constHeroStartWeapon['Description'],
                           constHeroStartWeapon['Price'], constHeroStartWeapon['Damage'][0],
                           constHeroStartWeapon['Damage'][1], constHeroStartWeapon['AttackSpeed'])
    startArmour = clArmour(constHeroStartArmour['Name'], constHeroStartArmour['Description'],
                           constHeroStartArmour['Price'], constHeroStartArmour['HealthBoost'],
                           constHeroStartArmour['SpeedBoost'])
    HeroWeapons.append(startWeapon)
    HeroArmours.append(startArmour)
    Hero.chAddWeapon(startWeapon)
    Hero.chAddArmour(startArmour)
    print('Here will be a Hero history')
    print("Now, it's time to remember who are you. What's your name?")
    name = input('[> ')
    Hero.chChangeGeneralParam('Name', name)
    HeroNewLevel(Hero)
    Hero.chSetGeneralParam('CHealth', Hero.chGetGeneralParam('MHealth'))
    Hero.chSetGeneralParam('PotionSlots', [1, 1])
    res = (Hero, (HeroWeapons, HeroArmours), Params)
    SaveGame(res[0], res[1], res[2], 0)
    return res

def ContinueGame():
    ''' Function to continue game. It's read File constDataFileName and returns
        (clCharacter, (List of Weapon, List of Armour))
        It doesn't check file exists. It will be checked in function that will
        call ContinueGame
    '''
    f = open(constDataFileName, 'br')
    Hero, Inv, Par = load(f)
    f.close()
    resH = clCharacter()
    resI = [[],[]]
    resP = {}
    for keys in constGeneralParams:
        resH.chSetGeneralParam(keys, Hero[0][keys])
    for keys in constCommonTraits:
        resH.chSetCommonTrait(keys, Hero[3][keys])
    for keys in constSpecialTraits:
        resH.chSetSpecialTrait(keys, Hero[4][keys])
    for keys in constDefaultParams.keys():
        if keys in Par.keys():
            resP[keys] = Par[keys]
        else:
            resP[keys] = constDefaultParams[keys]
    wep = clWeapon()
    arm = clArmour()
    for keys in constWeaponParams:
        wep[keys] = Hero[1][keys]
    for keys in constArmourParams:
        arm[keys] = Hero[2][keys]
    resH.chAddWeapon(wep, 1)
    resH.chAddArmour(arm, 1)
    for weps in Inv[0]:
        w = clWeapon()
        for keys in constWeaponParams:
            w[keys] = weps[keys]
        resI[0].append(w)
    for arms in Inv[1]:
        a = clArmour()
        for keys in constArmourParams:
            a[keys] = arms[keys]
        resI[1].append(a)
    return (resH, resI, resP)

def AboutGame():
    ''' Just info about the game. It will be shown if user choose About in MainMenu '''
    print('There will be Game Info')

def MainMenu():
    ''' Function that show Main Menu of the game. User can choose what he
        want to do (Start New Game, Continue, show info About the game
        and Exit from game)
    '''
    res = 0
    print()
    print('~'*7 + '_'*7 + 'Neuralturer' + '_'*7 + '~'*7)
    print()
    print('_'*10 + 'Main Menu' + '_'*10)
    print('Input digit that corresponding option that you want to choose')
    print()
    canContinue = 0
    if os.path.exists(constDataFileName):
        canContinue = 1
        print('1. Continue Game')
    print(str(1 + canContinue) + '. New Game')
    print(str(2 + canContinue) + '. About')
    print(str(3 + canContinue) + '. Exit')
    print()
    userChoice = input('[> ')
    if canContinue and userChoice == '1':
        res = ContinueGame()
    elif userChoice == str(1 + canContinue):
        res = NewGame()
    elif userChoice == str(2 + canContinue):
        AboutGame()
        res = MainMenu()
    elif userChoice == str(3 + canContinue):
        exit()
    else:
        print("There's no option", userChoice + '! Try again')
        res = MainMenu()
    return res

def SaveGame(Character, Inventory, Params, ShowInfoFlag = 1):
    ''' Function that save Game Data to constDataFileName file.
        Be sure that Inventory is (List of Weapon, List of Armour)
        Params is dictionary with Params and their values
    '''
    hgp = {}                        # Hero GeneralParam
    hw = {}                         # Hero Weapon
    ha = {}                         # Hero Armour
    hct = {}                        # Hero CommonTrait
    hst = {}                        # Hero SpecialTrait
    wep = Character.chGetWeapon()   # Hero current Weapon
    arm = Character.chGetArmour()   # Hero current Armour
    invw = []                       # Weapons from Inventory
    inva = []                       # Armours from Inventory
    for keys in constGeneralParams:
        hgp[keys] = Character.chGetGeneralParam(keys)
    for keys in constCommonTraits:
        hct[keys] = Character.chGetCommonTrait(keys)
    for keys in constSpecialTraits:
        hst[keys] = Character.chGetSpecialTrait(keys)
    for keys in constWeaponParams:
        hw[keys] = wep[keys]
    for keys in constArmourParams:
        ha[keys] = arm[keys]
    for weps in Inventory[0]:
        w = {}
        for keys in constWeaponParams:
            w[keys] = weps[keys]
        invw.append(w)
    for arms in Inventory[1]:
        a = {}
        for keys in constArmourParams:
            a[keys] = arms[keys]
        inva.append(a)
    res = ((hgp, hw, ha, hct, hst), (invw, inva), Params)
    f = open(constDataFileName, 'bw')
    dump(res, f)
    f.close()
    if ShowInfoFlag:
        print('Successfully saved!')

def CityMarket(Hero, Inventory, Params):
    ''' Function that imitate market in main city. On market player can buy
        weapons, armour and potions. Merchants have one weapon and armour for
        each type.
    '''
    # what you can buy
    WeaponRange = [choice(constDaggerWeapon), choice(constSwordWeapon),
                   choice(constAxeWeapon), choice(constSpearWeapon),
                   choice(constGreatSwordWeapon), choice(constHammerWeapon),
                   choice(constBowWeapon)]
    ArmourRange = [choice(constClothesArmour), choice(constLightArmour),
                   choice(constHeavyArmour)]
    # Price of a bottle of Potion
    PotPrice = 20
    PlayerChoice = '0'
    weapstr = '70123456'
    armstr = '3012'
    # idea is: if hero has full health then after wearing new armour up he will
    # be with full health
    # if hero was healthy then he will be healthy, but if he was bitten then he
    # can't be healthy after wearing new armour.
    FullHealthFlag = (1 if Hero.chGetGeneralParam('CHealth') == Hero.chGetGeneralParam('MHealth')
                      else 0)
    while PlayerChoice != '4':
        # How much Potion Hero need to buy for full stack
        HM4FullHeal = (Hero.chGetGeneralParam('MaxPotion') -
                       Hero.chGetGeneralParam('PotionSlots')[0])
        HM4FullDamage = (Hero.chGetGeneralParam('MaxPotion') -
                         Hero.chGetGeneralParam('PotionSlots')[1])
        PotionRange = ({'Name': 'Heal Potion', 'Price': PotPrice},
                       {'Name': 'Heal Potion (full)', 'Price': PotPrice * HM4FullHeal},
                       {'Name': 'Damage Potion', 'Price': PotPrice},
                       {'Name': 'Damage Potion (full)', 'Price': PotPrice * HM4FullDamage})
        print('_____MARKET_____')
        print('1. Visit weaponsmith')
        print('2. Visit armoursmith')
        print('3. Visit alchemist')
        print('4. Leave')
        print()
        PlayerChoice = input('You decided: [> ')
        if PlayerChoice == '1':
            print()
            print('You have', Hero.chGetGeneralParam('Gold'), 'golds')
            print('~'*15)
            # list of available weapons
            for i in range(0, len(WeaponRange)):
                print(str(i) + '.', WeaponRange[i]['Name'], ' '*3, 'Damage:',
                      WeaponRange[i]['Damage'][0], '-', WeaponRange[i]['Damage'][1],
                      ' '*3, 'Speed:', WeaponRange[i]['AttackSpeed'], ' '*3, 'Price:',
                      WeaponRange[i]['Price'])
            print('8. Leave')
            print()
            pch = input('You decided: [> ')
            if pch in weapstr and pch != '':
                if pch == '8':
                    PlayerChoice = 0
                else:
                    pch = int(pch)
                    # you can buy if you have enough golds
                    if Hero.chGetGeneralParam('Gold') >= WeaponRange[pch]['Price']:

                        weapon = clWeapon(WeaponRange[pch]['Name'],
                                          WeaponRange[pch]['Description'],
                                          WeaponRange[pch]['Price'],
                                          WeaponRange[pch]['Damage'][0],
                                          WeaponRange[pch]['Damage'][1],
                                          WeaponRange[pch]['AttackSpeed'])
                        if weapon in Inventory[0]:
                            print('You have that one!')
                        else:
                            Hero.chSetGeneralParam('Gold',
                                Hero.chGetGeneralParam('Gold') - WeaponRange[pch]['Price'])
                            # you get it
                            Hero.chAddWeapon(weapon)
                            Inventory[0].append(weapon)
                            WeaponRange.remove(WeaponRange[pch])
                            weapstr = weapstr[0: -1]
                            print('You got it!')
                            print('And now you have', Hero.chGetGeneralParam('Gold'), 'golds')
                            SaveGame(Hero, Inventory, Params, 0)
                    else:
                        print('Not enough GOLD!')
                        print('You have only', Hero.chGetGeneralParam('Gold'), 'golds')
            else:
                print('Imposible to choose', pch)
            print()
        elif PlayerChoice == '2':
            print()
            print('You have', Hero.chGetGeneralParam('Gold'), 'golds')
            print('~'*15)
            # same with armour
            for i in range(0, len(ArmourRange)):
                print(str(i) + '.', ArmourRange[i]['Name'], ' '*3, 'Health boost:',
                      ArmourRange[i]['HealthBoost'], ' '*3, 'Speed boost:',
                      ArmourRange[i]['SpeedBoost'], ' '*3,  'Price:', ArmourRange[i]['Price'])
            print('3. Leave')
            print()
            pch = input('You decided: [> ')
            if pch in armstr and pch != '':
                if pch == '3':
                    PlayerChoice = 0
                else:
                    pch = int(pch)
                    if Hero.chGetGeneralParam('Gold') >= ArmourRange[pch]['Price']:
                        armour = clArmour(ArmourRange[pch]['Name'],
                                          ArmourRange[pch]['Description'],
                                          ArmourRange[pch]['Price'],
                                          ArmourRange[pch]['HealthBoost'],
                                          ArmourRange[pch]['SpeedBoost'])
                        if armour in Inventory[1]:
                            print('You have that one!')
                        else:
                            Hero.chSetGeneralParam('Gold',
                                Hero.chGetGeneralParam('Gold') - ArmourRange[pch]['Price'])
                            Hero.chAddArmour(armour)
                            Inventory[1].append(armour)
                            ArmourRange.remove(ArmourRange[pch])
                            armstr = armstr[0: -1]
                            print('You got it!')
                            print('And now you have', Hero.chGetGeneralParam('Gold'), 'golds')
                            if FullHealthFlag:
                                Hero.chSetGeneralParam('CHealth', Hero.chGetGeneralParam('MHealth'))
                            SaveGame(Hero, Inventory, Params, 0)
                    else:
                        print('Not enough GOLD!')
                        print('You have only', Hero.chGetGeneralParam('Gold'), 'golds')
            else:
                print('Imposible to choose', pch)
            print()
        elif PlayerChoice == '3':
            print()
            print('You have', Hero.chGetGeneralParam('Gold'), 'golds')
            print('~'*15)
            # Potions
            for i in range(0, len(PotionRange)):
                print(str(i) + '.', PotionRange[i]['Name'], ' '*5,
                      PotionRange[i]['Price'])
            print('4. Leave')
            print()
            pch = input('You decided: [> ')
            if pch in '01234' and pch != '':
                if pch == '4':
                    PlayerChoice = 0
                else:
                    pch = int(pch)
                    if Hero.chGetGeneralParam('Gold') >= PotionRange[pch]['Price']:
                        k = (0 if pch in (0, 1) else 1)
                        if Hero.chGetGeneralParam('PotionSlots')[k] < Hero.chGetGeneralParam('MaxPotion'):
                            Hero.chSetGeneralParam('Gold',
                                Hero.chGetGeneralParam('Gold') - PotionRange[pch]['Price'])
                            hpot = Hero.chGetGeneralParam('PotionSlots')[0]
                            dpot = Hero.chGetGeneralParam('PotionSlots')[1]
                            if pch % 2 == 0:
                                 pot = ([hpot + 1, dpot] if pch == 0 else [hpot, dpot + 1])
                            else:
                                pot = ([hpot + HM4FullHeal, dpot] if pch == 1 else [hpot, dpot + HM4FullDamage])
                            Hero.chSetGeneralParam('PotionSlots', pot)
                            print('You got it!')
                            print('And now you have', Hero.chGetGeneralParam('Gold'), 'golds')
                            SaveGame(Hero, Inventory, Params, 0)
                        else:
                            print('No free space!')
                    else:
                        print('Not enough GOLD!')
                        print('You have only', Hero.chGetGeneralParam('Gold'), 'golds')
            else:
                print('Imposible to choose', pch)
            print()

def HeroInfoOption(Hero, Inventory, Params):
    ''' This function can show Hero information as chShowInfo and show Inventory.
        Player can equip item from Inventory
    '''
    PlayerChoice = '0'
    # idea is: if hero has full health then after wearing new armour up he will
    # be with full health
    # if hero was healthy then he will be healthy, but if he was bitten then he
    # can't be healthy after wearing new armour.
    FullHealthFlag = (1 if Hero.chGetGeneralParam('CHealth') == Hero.chGetGeneralParam('MHealth')
                      else 0)
    while PlayerChoice != '5':
        print('_____Hero Information_____')
        print('1. General info')
        print('2. Full info')
        print('3. Weapons in inventory')
        print('4. Armours in inventory')
        print('5. Back')
        print()
        PlayerChoice = input('You decided: [> ')
        if PlayerChoice == '1':
            Hero.chShowInfo()
        elif PlayerChoice == '2':
            Hero.chShowInfo(3)
        elif PlayerChoice == '3':
            print('You have next weapons.')
            for i in range(0, len(Inventory[0])):
                print('~'*40)
                print(str(i) + '.', Inventory[0][i]['Name'], ' '*5, 'Damage:',
                      Inventory[0][i]['MinDamage'], '-', Inventory[0][i]['MaxDamage'],
                      ' '*5, 'Attack speed:', Inventory[0][i]['AttackSpeed'])
                print(' '.join(Inventory[0][i]['Description'].split()))
            print('~'*40)
            print()
            print('What do you want to equip? (00 for nothing)')
            pch = input('You decided: [> ')
            if pch.isdigit():
                if pch == '00':
                    PlayerChoice = '0'
                elif int(pch) >= len(Inventory[0]):
                    print('Incorrect input!')
                else:
                    Hero.chAddWeapon(Inventory[0][int(pch)])
                    print('You equiped it!')
            else:
                print('Impossible to choose', pch)
        elif PlayerChoice == '4':
            print('You have next armours.')
            for i in range(0, len(Inventory[1])):
                print('~'*40)
                print(str(i) + '.', Inventory[1][i]['Name'], ' '*5, 'Health boost:',
                      Inventory[1][i]['HealthBoost'], ' '*5, 'Speed boost:',
                      Inventory[1][i]['SpeedBoost'])
                print(' '.join(Inventory[1][i]['Description'].split()))
            print('~'*40)
            print()
            print('What do you want to equip? (00 for nothing)')
            pch = input('You decided: [> ')
            if pch.isdigit():
                if pch == '00':
                    PlayerChoice = '0'
                elif int(pch) >= len(Inventory[1]):
                    print('Incorrect input!')
                else:
                    Hero.chAddArmour(Inventory[1][int(pch)])
                    print('You equiped it!')
                    if FullHealthFlag:
                        Hero.chSetGeneralParam('CHealth', Hero.chGetGeneralParam('MHealth'))
            else:
                print('Impossible to choose', pch)
        print()

def TownPhysician(Hero, Inventory, Params):
    ''' Option Visit Physician in some places.
        In constCityName you can pay for full health restoring and for BattleRestoring
        In one place, there will be only free full restoration
    '''
    PlayerChoice = '-1'
    if Params['Place']['Name'] == constHofName:
        fulprice = 0
        poulticeprice = 0
    elif Params['Place']['IsSafe']:
        fulprice = 100
        poulticeprice = 35
    else:
        fulprice = 200
        poulticeprice = 70
    while PlayerChoice != '3':
        print('_____PHYSICIAN_____')
        # there will be if for unique place where it's free to full restoration
        print('1. Ask for full healing (' + str(fulprice), 'golds)')
        print('2. Ask for healing poultice (max restore',
              str(Hero.chGetGeneralParam('BattleRestore') *
              Hero.chGetGeneralParam('MHealth') // 100), ') ('+str(poulticeprice), 'golds)')
        print('3. Leave')
        print()
        print('You have', Hero.chGetGeneralParam('Gold'), 'golds')
        print('And now your health:', str(Hero.chGetGeneralParam('CHealth')) + '/' +
              str(Hero.chGetGeneralParam('MHealth')))
        PlayerChoice = input('You decided: [> ')
        if PlayerChoice == '1':
            if Hero.chGetGeneralParam('CHealth') == Hero.chGetGeneralParam('MHealth'):
                print('You are in full health!')
            else:
                if Hero.chGetGeneralParam('Gold') >= fulprice:
                    Hero.chHealthRestore(1)
                    Hero.chChangeGeneralParam('Gold', -fulprice)
                    print('Now you have', Hero.chGetGeneralParam('Gold'), 'golds')
                    print('And your health:', str(Hero.chGetGeneralParam('CHealth')) + '/' +
                          str(Hero.chGetGeneralParam('MHealth')))
                    SaveGame(Hero, Inventory, Params, 0)
                else:
                    print('Not enough GOLD!')
                    print('You have only', Hero.chGetGeneralParam('Gold'), 'golds')
        elif PlayerChoice == '2':
            if Hero.chGetGeneralParam('CHealth') == Hero.chGetGeneralParam('MHealth'):
                print('You are in full health!')
            else:
                if Hero.chGetGeneralParam('Gold') >= poulticeprice:
                    Hero.chHealthRestore()
                    Hero.chChangeGeneralParam('Gold', -poulticeprice)
                    print('Now you have', Hero.chGetGeneralParam('Gold'), 'golds')
                    print('And your health:', str(Hero.chGetGeneralParam('CHealth')) + '/' +
                          str(Hero.chGetGeneralParam('MHealth')))
                    SaveGame(Hero, Inventory, Params, 0)
                else:
                    print('Not enough GOLD!')
                    print('You have only', Hero.chGetGeneralParam('Gold'), 'golds')
        elif PlayerChoice != '3':
            print('Impossible to choose', PlayerChoice)
            print('Try again!')
        print()

def HeroEnemyBattle(Hero, Enemy, type):
    ''' function that makes Hero fights with Enemy.
        type can be 'Arena' and 'Field'. It influence on some parameters of battle
        function returns (WinFlag, FleeFlag). WinFlag = 1 if Hero Win
        FleeFlag = 0 if Nobody fleed, 1 if Flee Hero and 2 if Flee Enemy.
        Function just hits Hero and Enemy and uses their Potions. It doesn't
        reward participants. You should do it with your own hands.
    '''
    # define result variables
    WinFlag = -1
    FleeFlag = 0
    # flag for some differences between arena and field
    ArenaFlag = (1 if type == 'Arena' else 0)
    # who is attacker and who is defender
    if ArenaFlag:
        a = choice((0, 1))
        if a:
            attacker, defender = Hero, Enemy
        else:
            attacker, defender = Enemy, Hero
    elif type == 'Field':
        # who is more lucky
        if Hero.chGetCommonTrait('Luck') > Enemy.chGetCommonTrait('Luck'):
            attacker, defender = Hero, Enemy
        elif Hero.chGetCommonTrait('Luck') < Enemy.chGetCommonTrait('Luck'):
            attacker, defender = Enemy, Hero
        # if equal that random
        else:
            a = choice((0, 1))
            if a:
                attacker, defender = Hero, Enemy
            else:
                attacker, defender = Enemy, Hero
    # now, count of hits for both fighters
    atHits = (1 if attacker.chGetGeneralParam('AttackSpeed') < defender.chGetGeneralParam('AttackSpeed')
              else round(attacker.chGetGeneralParam('AttackSpeed') / defender.chGetGeneralParam('AttackSpeed')))
    defHits = (1 if defender.chGetGeneralParam('AttackSpeed') < attacker.chGetGeneralParam('AttackSpeed')
              else round(defender.chGetGeneralParam('AttackSpeed') / attacker.chGetGeneralParam('AttackSpeed')))
    # before battle info about opponents
    print('~'*20)
    print(Hero.chGetGeneralParam('Name'), ' '*3, 'Health:',
          str(Hero.chGetGeneralParam('CHealth')) + '/' + str(Hero.chGetGeneralParam('MHealth')),
          ' '*5, Enemy.chGetGeneralParam('Name'), ' '*3, 'Health:',
          str(Enemy.chGetGeneralParam('CHealth')) + '/' + str(Enemy.chGetGeneralParam('MHealth')))
    print('~'*20)
    # there battle will begin
    while (attacker.chGetGeneralParam('CHealth') > 0 and
           defender.chGetGeneralParam('CHealth') > 0 and
        FleeFlag == 0):
        # attacker hit. In the end of loop attacker is changed
        # print battle log only in Arena mode
        if ArenaFlag:
            print('~'*20)
            print(attacker.chGetGeneralParam('Name'), 'prepare to smash!')
        for i in range(0, atHits):
            # if it isn't Arena then attacker has FleeChance
            if type != 'Arena':
                if (attacker.chGetGeneralParam('CHealth') < defender.chGetGeneralParam('CHealth') // 2 and
                    WhatWillHappen({1: attacker.chGetGeneralParam('FleeChance')})):
                    if FleeFlag == 0:
                        FleeFlag = (1 if attacker == Hero else 2)
                        print(attacker.chGetGeneralParam('Name') + ' decided to flee.')
            # now let's drink some potions
            DamagePotionFlag = 0
            if (defender.chGetGeneralParam('CHealth') < defender.chGetGeneralParam('MHealth') and
                attacker.chGetGeneralParam('PotionSlots')[1] > 0):
                DamagePotionFlag = 1
                attacker.chDrinkPotion(1)
                if ArenaFlag:
                    print('Drink Damage Potion')
            if (attacker.chGetGeneralParam('CHealth') < attacker.chGetGeneralParam('MHealth') and
                attacker.chGetGeneralParam('PotionSlots')[0] > 0):
                attacker.chDrinkPotion(0)
                if ArenaFlag:
                    print('Drink Heal Potion')
            # attacker hits
            hit = attacker.chDoHit()
            defender.chChangeGeneralParam('CHealth', -hit)
            if defender.chGetGeneralParam('CHealth') < 0:
                defender.chSetGeneralParam('CHealth', 0)
            if ArenaFlag:
                print('Delivered', hit, 'damage!')
            if DamagePotionFlag:
                attacker.chDisappearPotion()
                DamagePotionFlag = 0
                if ArenaFlag:
                    print('Strength leaves', attacker.chGetGeneralParam('Name'))
        # print opponents health after hits
        if ArenaFlag:
            print('~'*20)
            print(Hero.chGetGeneralParam('Name'), ' '*3, 'Health:',
                  str(Hero.chGetGeneralParam('CHealth')) + '/' + str(Hero.chGetGeneralParam('MHealth')),
                  ' '*5, Enemy.chGetGeneralParam('Name'), ' '*3, 'Health:',
                  str(Enemy.chGetGeneralParam('CHealth')) + '/' + str(Enemy.chGetGeneralParam('MHealth')))
            print('~'*20)
        # change roles
        attacker, defender = defender, attacker
        atHits, defHits = defHits, atHits
    # battle ends
    if FleeFlag == 1:
        WinFlag = 0
    elif FleeFlag == 2:
        WinFlag = 1
    else:
        if Hero.chGetGeneralParam('CHealth') == 0:
            WinFlag = 0
        else:
            WinFlag = 1
    return (WinFlag, FleeFlag)

def CityArena(Hero, Inventory, Params):
    ''' function that makes it possible to participate in competition on the Arena
        Player makes choice, take bet and then his Hero fights. If Hero wins,
        then he gets bet*2, experience from bitten Enemy, NewLevel, if he has enough
        experience. And at the end, Hero full restore his health.
    '''
    PlayerChoice = '-1'
    while PlayerChoice != '0':
        PlayerBet = 0
        ContinueFlag = 0
        print('_____ARENA_____')
        print('1. Fight with animal (bets under 50 golds)')
        print('2. Easy fight (bets under 100 golds)')
        print('3. Medium fight (bets in [100; 500] golds)')
        print('4. Hard fight (bets above 500 golds)')
        # mb in future there will be Random Fight
        print('0. Leave')
        print()
        print('You have', Hero.chGetGeneralParam('Gold'), 'golds')
        # Easy fight
        PlayerChoice = input('You decided: [> ')
        if PlayerChoice == '1':
            # take a bet
            while ContinueFlag == 0:
                print('Input your bet. Must be in [1; 50]')
                print('Input 00 to go back!')
                PlayerBet = input('[> ')
                if PlayerBet == '00':
                    ContinueFlag = -1
                elif PlayerBet.isdigit():
                    if int(PlayerBet) <= 50 and int(PlayerBet) >= 1:
                        if int(PlayerBet) <= Hero.chGetGeneralParam('Gold'):
                            PlayerBet = int(PlayerBet)
                            Hero.chChangeGeneralParam('Gold', -PlayerBet)
                            print('Bet confirmed')
                            ContinueFlag = 1
                        else:
                            print('Not enough GOLD')
                    else:
                        print('Incorrect input!')
                else:
                    print('Use only digits!')
            # enemy generation
            if ContinueFlag == 1:
                Enemy = EnemyGenerationByTrip(constArenaAnimal)
        elif PlayerChoice == '2':
            # take a bet
            while ContinueFlag == 0:
                print('Input your bet. Must be in [1; 100]')
                print('Input 00 to go back!')
                PlayerBet = input('[> ')
                if PlayerBet == '00':
                    ContinueFlag = -1
                elif PlayerBet.isdigit():
                    if int(PlayerBet) <= 100 and int(PlayerBet) >= 1:
                        if int(PlayerBet) <= Hero.chGetGeneralParam('Gold'):
                            PlayerBet = int(PlayerBet)
                            Hero.chChangeGeneralParam('Gold', -PlayerBet)
                            print('Bet confirmed')
                            ContinueFlag = 1
                        else:
                            print('Not enough GOLD')
                    else:
                        print('Incorrect input!')
                else:
                    print('Use only digits!')
            # enemy generation
            if ContinueFlag == 1:
                Enemy = EnemyGenerationByTrip('ArenaE', Hero.chGetGeneralParam('Level'))
        elif PlayerChoice == '3':
            # take a bet
            while ContinueFlag == 0:
                print('Input your bet. Must be in [100; 500]')
                print('Input 00 to go back!')
                PlayerBet = input('[> ')
                if PlayerBet == '00':
                    ContinueFlag = -1
                elif PlayerBet.isdigit():
                    if int(PlayerBet) <= 500 and int(PlayerBet) >= 100:
                        if int(PlayerBet) <= Hero.chGetGeneralParam('Gold'):
                            PlayerBet = int(PlayerBet)
                            Hero.chChangeGeneralParam('Gold', -PlayerBet)
                            print('Bet confirmed')
                            ContinueFlag = 1
                        else:
                            print('Not enough GOLD')
                    else:
                        print('Incorrect input!')
                else:
                    print('Use only digits!')
            # enemy generation
            if ContinueFlag == 1:
                Enemy = EnemyGenerationByTrip('ArenaM', Hero.chGetGeneralParam('Level'))
        elif PlayerChoice == '4':
            # take a bet
            while ContinueFlag == 0:
                print('Input your bet. Must be 500 and more')
                print('Input 00 to go back!')
                PlayerBet = input('[> ')
                if PlayerBet == '00':
                    ContinueFlag = -1
                elif PlayerBet.isdigit():
                    if int(PlayerBet) >= 500:
                        if int(PlayerBet) <= Hero.chGetGeneralParam('Gold'):
                            PlayerBet = int(PlayerBet)
                            Hero.chChangeGeneralParam('Gold', -PlayerBet)
                            print('Bet confirmed')
                            ContinueFlag = 1
                        else:
                            print('Not enough GOLD')
                    else:
                        print('Incorrect input!')
                else:
                    print('Use only digits!')
            # enemy generation
            if ContinueFlag == 1:
                Enemy = EnemyGenerationByTrip('ArenaH', Hero.chGetGeneralParam('Level'))
        elif PlayerChoice != '0':
            print('Impossible to choose', PlayerChoice)
        # after all, let's show our battle
        if ContinueFlag == 1:
            WF, FF = HeroEnemyBattle(Hero, Enemy, 'Arena')
            # Hero wins
            if WF == 1:
                print(Hero.chGetGeneralParam('Name'), 'won!')
                # reward
                Hero.chChangeGeneralParam('Gold', PlayerBet * 2)
                # experience
                Hero.chChangeGeneralParam('Experience',
                    Enemy.chGetGeneralParam('Level') // 10 + 1)
                if Hero.chGetGeneralParam('Experience') >= chHowMuchExpNeed(
                        Hero.chGetGeneralParam('Level') + 1):
                    HeroNewLevel(Hero)
            else:
                print(Enemy.chGetGeneralParam('Name'), 'won!')
            # full restoration
            Hero.chHealthRestore(1)
            SaveGame(Hero, Inventory, Params, 0)
        print()

def TripFromToPlace(Hero, Inventory, Params, FromPlace, ToPlace):
    ''' Function of Character adventure. Hero go from FromPlace to ToPlace,
        fight with enemies, can return, when he arrives, he can clean place,
        and than visit it and do his deals. If Place IsSafe, there is no need
        to clear it
    '''
    # how much enemies Hero meets
    enemy_count = 0
    # continue trip or not
    continue_flag = True
    # hero award
    hero_award = 0
    # where will be Hero after trip
    Place = FromPlace
    Params['Place'] = Place
    # trip length from FromPlace to ToPlace
    i = 0
    while i < (ToPlace['TripLength'][FromPlace['Name']]) and continue_flag:
        # can meet Enemy?
        if WhatWillHappen({1: ToPlace['EnemyChance']}):
            enemy_count += 1
            Enemy = EnemyGenerationByTrip(ToPlace['TripType'][FromPlace['Name']])
            print(' '.join(Enemy.chGetGeneralParam('Description').split()))
            # Fight
            WinFlag, FleeFlag =  HeroEnemyBattle(Hero, Enemy, 'Field')
            Hero.chHealthRestore()
            # Hero Wins
            if WinFlag == 1 or FleeFlag == 1:
                if FleeFlag == 0:
                    print(Hero.chGetGeneralParam('Name'), 'won!')
                    print(Enemy.chGetGeneralParam('Name'), 'is defeated!')
                    hero_award = Hero.chGetGeneralParam('FindChance') * Enemy.chGetGeneralParam('Gold') / 100
                    hero_award = round(hero_award)
                    print('Found', hero_award, 'golds')
                    # drop:
                    enemy_weapon = Enemy.chGetWeapon()
                    if enemy_weapon['Name'] != 'None':
                        if WhatWillHappen({1: Hero.chGetGeneralParam('FindChance')/4}):
                            print('You found', enemy_weapon['Name'])
                            if enemy_weapon not in Inventory[0]:
                                Inventory[0].append(enemy_weapon)
                    enemy_armour = Enemy.chGetArmour()
                    if enemy_armour['Name'] != 'None':
                        if WhatWillHappen({1: Hero.chGetGeneralParam('FindChance')/4}):
                            print('You found', enemy_armour['Name'])
                            if enemy_armour not in Inventory[1]:
                                Inventory[1].append(enemy_armour)
                    # experience
                    Hero.chChangeGeneralParam('Experience',
                                              Enemy.chGetGeneralParam('Level') // 10 + 1)
                    if Hero.chGetGeneralParam('Experience') >= chHowMuchExpNeed(
                                    Hero.chGetGeneralParam('Level') + 1):
                        HeroNewLevel(Hero)
                elif FleeFlag == 2:
                    print(Hero.chGetGeneralParam('Name'), 'won!')
                    print(Enemy.chGetGeneralParam('Name'), 'retreated!')
                    # experience
                    Hero.chChangeGeneralParam('Experience',
                                              Enemy.chGetGeneralParam('Level') // 10 + 1)
                    if Hero.chGetGeneralParam('Experience') >= chHowMuchExpNeed(
                                    Hero.chGetGeneralParam('Level') + 1):
                        HeroNewLevel(Hero)
                elif FleeFlag == 1:
                    print(Hero.chGetGeneralParam('Name'), 'retreated!')
                # continue trip?
                cor_input = False
                print(Hero.chGetGeneralParam('Name'), ' ' * 3, 'Health:',
                      str(Hero.chGetGeneralParam('CHealth')) + '/' + str(Hero.chGetGeneralParam('MHealth')))
                while not cor_input:
                    print('1. Continue')
                    print('2. Go back')
                    user_choice = input('[> ')
                    if user_choice in ('1', '2'):
                        cor_input = True
                        # go back
                        if user_choice == '2':
                            continue_flag = False
                    else:
                        print('Incorrect input! Try again.')
            # lose
            else:
                print(Hero.chGetGeneralParam('Name'), 'lost!')
                continue_flag = False
                enemy_findchance = Enemy.chGetGeneralParam('FindChance') + Enemy.chGetGeneralParam('Level')
                if enemy_findchance > 90:
                    enemy_findchance = 90
                # take hero's money
                hero_award = -enemy_findchance * Hero.chGetGeneralParam('Gold') / 100
                hero_award = round(hero_award)
                # loses to go to safe zone
                if FromPlace['IsSafe']:
                    hero_award -= ToPlace['TripLength'][FromPlace['Name']] * 2
                else:
                    Place = constCityPlace
                    hero_award -= 200
                print('You was taken by good men. They bring you to', Place['Name'] + '.')
            if Hero.chGetGeneralParam('Gold') + hero_award < 0:
                print('Lost whole gold.')
                Hero.chSetGeneralParam('Gold', 0)
            else:
                if hero_award < 0:
                    print("Lost", abs(hero_award), "golds.")
                Hero.chChangeGeneralParam('Gold', hero_award)
        i += 1
        Params['Place'] = Place
        SaveGame(Hero, Inventory, Params, 0)
    if i == ToPlace['TripLength'][FromPlace['Name']] and continue_flag:
        # Hero arrived
        print('You successfully arrived!')
        if ToPlace['IsSafe']:
            Place = ToPlace
        else:
            # Hero can clear place or go home
            cor_input = False
            while not cor_input:
                print('Now you at', ToPlace['Name'])
                print('1. Clear the place (No one can help you)')
                print('2. Go back (You can go back and stay alive)')
                user_choice = input('[> ')
                if user_choice in ('1', '2'):
                    cor_input = True
                    # clear
                    if user_choice == '1':
                        Place = ToPlace
                        j = enemy_count
                        alive_flag = True
                        while j <= ToPlace['TripLength'][FromPlace['Name']] and alive_flag:
                            if j == ToPlace['TripLength'][FromPlace['Name']]:
                                print('It\'s BOSS time!')
                                Enemy = EnemyGenerationByTrip(ToPlace['BossType'])
                            else:
                                Enemy = EnemyGenerationByTrip(ToPlace['TripType'][FromPlace['Name']])
                            j += 1
                            print(' '.join(Enemy.chGetGeneralParam('Description').split()))
                            # Fight
                            WinFlag, FleeFlag = HeroEnemyBattle(Hero, Enemy, 'Field')
                            if WinFlag == 1:
                                if FleeFlag == 0:
                                    print(Hero.chGetGeneralParam('Name'), 'won!')
                                    print(Enemy.chGetGeneralParam('Name'), 'is defeated!')
                                    hero_award = Hero.chGetGeneralParam('FindChance') * \
                                                 Enemy.chGetGeneralParam('Gold') / 100
                                    hero_award = round(hero_award)
                                    print('Found', hero_award, 'golds')
                                    Hero.chChangeGeneralParam('Gold', hero_award)
                                    # boss drop. Yes, only boss, but chance is greater.
                                    if j > ToPlace['TripLength'][FromPlace['Name']]:
                                        enemy_weapon = Enemy.chGetWeapon()
                                        if enemy_weapon['Name'] != 'None':
                                            if WhatWillHappen({1: Hero.chGetGeneralParam('FindChance') / 2}):
                                                print('You found', enemy_weapon['Name'])
                                                if enemy_weapon not in Inventory[0]:
                                                    Inventory[0].append(enemy_weapon)
                                        enemy_armour = Enemy.chGetArmour()
                                        if enemy_armour['Name'] != 'None':
                                            if WhatWillHappen({1: Hero.chGetGeneralParam('FindChance') / 2}):
                                                print('You found', enemy_armour['Name'])
                                                if enemy_armour not in Inventory[1]:
                                                    Inventory[1].append(enemy_armour)
                                elif FleeFlag == 2:
                                    print(Hero.chGetGeneralParam('Name'), 'won!')
                                    print(Enemy.chGetGeneralParam('Name'), 'retreated!')
                                # experience
                                Hero.chChangeGeneralParam('Experience',
                                                          Enemy.chGetGeneralParam('Level') // 10 + 1)
                                if Hero.chGetGeneralParam('Experience') >= chHowMuchExpNeed(
                                                    Hero.chGetGeneralParam('Level') + 1):
                                    HeroNewLevel(Hero)
                                print(Hero.chGetGeneralParam('Name'), ' ' * 3, 'Health:',
                                      str(Hero.chGetGeneralParam('CHealth')) + '/' + str(
                                          Hero.chGetGeneralParam('MHealth')))
                            else:
                                print(Hero.chGetGeneralParam('Name'), 'lost!')
                                alive_flag = False
                                if FleeFlag == 1:
                                    print(Hero.chGetGeneralParam('Name'), 'retreated!')
                                    Place = FromPlace
                                    print('You run to', Place['Name'])
                                else:
                                    if j <= ToPlace['TripLength'][FromPlace['Name']]:
                                        Enemy = EnemyGenerationByTrip(ToPlace['BossType'])
                                    enemy_findchance = Enemy.chGetGeneralParam('FindChance') + \
                                                       Enemy.chGetGeneralParam('Level')
                                    if enemy_findchance > 100:
                                        enemy_findchance = 100
                                    hero_award = -enemy_findchance * Hero.chGetGeneralParam('Gold') / 100
                                    hero_award = round(hero_award)
                                    print('Lost', abs(hero_award), 'golds.')
                                    if Hero.chGetGeneralParam('Gold') + hero_award < 0:
                                        Hero.chSetGeneralParam('Gold', 0)
                                    else:
                                        Hero.chChangeGeneralParam('Gold', hero_award)
                                    # loses weapon and armour
                                    if WhatWillHappen({1: enemy_findchance}):
                                        if Hero.chGetWeapon()['Name'] != constHeroStartWeapon['Name']:
                                            Inventory[0].remove(Hero.chGetWeapon())
                                            Hero.chRemoveWeapon(Hero.chGetWeapon())
                                            print('Lost weapon.')
                                        else:
                                            print('They don\'t want to have your trash.')
                                    if WhatWillHappen({1: enemy_findchance}):
                                        Inventory[1].remove(Hero.chGetArmour())
                                        Hero.chRemoveArmour(Hero.chGetArmour())
                                        print('Lost armour.')
                                    Place = constCityPlace
                                    print('You was found by good men. They bring you to', Place['Name'] + '.')
                                    Params['Place'] = Place
                                SaveGame(Hero, Inventory, Params, 0)
                    Hero.chHealthRestore()
                else:
                    print('Incorrect input! Try again.')
    Params['Place'] = Place
    SaveGame(Hero, Inventory, Params, 0)
    return Hero, Inventory, Params

def AdventureOption(Hero, Inventory, Params):
    ''' That's is function that makes it possible to travel'''
    Place = Params['Place']
    PlayerChoice = '-1'
    while PlayerChoice != '0':
        for i in range(len(Place['PossibleTrip'])):
            print(str(i+1)+'.', Place['PossibleTrip'][i][0]['Name'],
                  '('+Place['PossibleTrip'][i][1]+')')
        print('0. Back')
        print()
        PlayerChoice = input('You decided: [> ')
        if PlayerChoice.isdigit() and PlayerChoice != '0':
            if int(PlayerChoice) <= len(Place['PossibleTrip']):
                Hero, Inventory, Params = TripFromToPlace(Hero, Inventory, Params, Place,
                                                          Place['PossibleTrip'][int(PlayerChoice)-1][0])
                PlayerChoice = '0'
            else:
                print('Incorrect input!')
        elif not PlayerChoice.isdigit():
            print('Use only digits!')
    return Hero, Inventory, Params


def PlaceMenu(Hero, Inventory, Params):
    ''' Function that show Menu of the Place (City and others). User can choose
        what he want to do. Other place has it's own list of option. But there is
        layout
    '''
    Place = Params['Place']
    PlaceName = Place['Name']
    # list of all option
    # some options are always available
    # that's my order of option:
    GeneralPlaceOptions = OrderedDict([('Inspect', 1), ('Adventure', 1), ('Market', 0),
                                       ('Tavern', 0), ('Arena', 0), ('Physician', 1),
                                       ('Character', 1), ('Save', 1), ('Menu', 1)])
    GeneralPlaceFunctions = {'Market': CityMarket, 'Arena': CityArena,
                             'Physician': TownPhysician, 'Character': HeroInfoOption,
                             'Save': SaveGame, 'Menu': MainMenu, 'Adventure': AdventureOption}
    CurPlaceOptions = OrderedDict()
    if PlaceName == constCityName:
        GeneralPlaceOptions['Market'] = 1
        GeneralPlaceOptions['Arena'] = 1
        GeneralPlaceOptions['Tavern'] = 1
    i = 1
    for key in GeneralPlaceOptions.keys():
        if GeneralPlaceOptions[key] == 1:
            CurPlaceOptions[i] = key
            i += 1
    print('~~~~~____' + PlaceName + '____~~~~~')
    for key in CurPlaceOptions.keys():
        print(str(key) + '.', CurPlaceOptions[key])
    print()
    userChoice = input('You decided to [> ')
    if userChoice == 'Give me GODMODE!':
        exec(input('[>>> '))
        PlaceMenu(Hero, Inventory, Params)
    elif userChoice.isdigit():
        if int(userChoice) in CurPlaceOptions.keys():
            if CurPlaceOptions[int(userChoice)] in ('Save', 'Market', 'Character', 'Arena', 'Physician'):
                GeneralPlaceFunctions[CurPlaceOptions[int(userChoice)]](Hero, Inventory, Params)
                PlaceMenu(Hero, Inventory, Params)
            elif CurPlaceOptions[int(userChoice)] in ('Menu'):
                Hero, Inventory, Params = GeneralPlaceFunctions[CurPlaceOptions[int(userChoice)]]()
                PlaceMenu(Hero, Inventory, Params)
            elif  CurPlaceOptions[int(userChoice)] in('Adventure'):
                Hero, Inventory, Params = \
                    GeneralPlaceFunctions[CurPlaceOptions[int(userChoice)]](Hero, Inventory, Params)
                PlaceMenu(Hero, Inventory, Params)
            else:
                print('Not available yet :(')
                PlaceMenu(Hero, Inventory, Params)
        else:
            print('Impossible to choose', userChoice)
            PlaceMenu(Hero, Inventory, Params)
    else:
        print('Use only digits!')
        PlaceMenu(Hero, Inventory, Params)
