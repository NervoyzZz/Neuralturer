# Neuralturer game
# File with useful functional

# to make random choices
from random import randint, choice
# to save data to file
from pickle import dump, load
# to check file exists
import os.path
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
        int OnePunch - every point increase chSpeed by 8
        int Physician - every point increase chBattleRestore by 16
        int Trader - character gets 1000 Golds

        Methods:
        chShowInfo(Param); Param = 0, 1, 2, 3
            This method for Hero, so there isn't Description that will be used
            only for Enemy. Info about Enemy we will get with chGetGeneralParam
        chIncreaseCommonTrait(CommonTraitKey); Key is from chCommonTrait
        chIncreaseSpecialTrait(SpecialTraitKey); same
        chRemoveWeapon(Weapon); chRemoveArmour(Armour)
        chAddWeapon(NewWeapon); chAddArmour(NewArmour)
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
                self.__chGeneralParam['Gold'] += 1000
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

    def chAddWeapon(self, NewWeapon):
        ''' This method adds NewWeapon to Character
            First, we should remove weapon from character and next we can
            change Character's params and set Weapon to NewWeapon
        '''
        self.chRemoveWeapon(self.__chWeapon)
        self.__chWeapon = NewWeapon
        self.__chGeneralParam['MinDamage'] += NewWeapon['MinDamage']
        self.__chGeneralParam['MaxDamage'] += NewWeapon['MaxDamage']
        self.__chGeneralParam['AttackSpeed'] += NewWeapon['AttackSpeed']

    def chRemoveArmour(self, OldArmour):
        ''' This method removes OldArmour from Character
            change Character's params and set Armour to None
        '''
        self.__chGeneralParam['MHealth'] -= OldArmour['HealthBoost']
        self.__chGeneralParam['AttackSpeed'] -= OldArmour['SpeedBoost']
        self.__chArmour = clArmour()

    def chAddArmour(self, NewArmour):
        ''' This method adds NewArmour to Character
            First, we should remove weapon from character and next we can
            change Character's params and set Armour to NewArmour
        '''
        self.chRemoveArmour(self.__chArmour)
        self.__chArmour = NewArmour
        self.__chGeneralParam['MHealth'] += NewArmour['HealthBoost']
        self.__chGeneralParam['AttackSpeed'] += NewArmour['SpeedBoost']

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

    def chGetSpecialTrait(self, Key):
        ''' return SpecialTrait by Key '''
        if Key in self.__chSpecialTrait.keys():
            return self.__chSpecialTrait[Key]
        else:
            return -1

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
        constVeryHardTrip and constForestTrip. It also can be equal ArenaE,
        ArenaM, ArenaH for difficult of Arena. First, choose EnemyType,
        then create Enemy and return it.
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
        print(traits)
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
                print(traits)
                print(traitPoint)
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
    # first we need to change current Hero Experience
    exp = (Hero.chGetGeneralParam('Experience') -
           chHowMuchExpNeed(Hero.chGetGeneralParam('Level') + 1))
    Hero.chChangeGeneralParam('Level', 1)
    Hero.chSetGeneralParam('Experience', exp)
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

def NewGame():
    ''' Function to start new game. It's create character for hero, create File
        constDataFileName (see in AdConstFile).
        Return (clCharacter, Inventory), where
        Inventory = (list of Weapon, list of Armour)
    '''
    res = ()
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
    res = (Hero, (HeroWeapons, HeroArmours))
    f = open(constDataFileName, 'bw')
    dump(res, f)
    f.close()
    return res

def ContinueGame():
    ''' Function to continue game. It's read File constDataFileName and returns
        (clCharacter, (List of Weapon, List of Armour))
        It doesn't check file exists. It will be checked in function that will
        call ContinueGame
    '''
    f = open(constDataFileName, 'br')
    res = load(f)
    f.close()
    return res

def AboutGame():
    ''' Just info about the game. It will be shown if user choose About in MainMenu '''
    print('There will be Game Info')

def MainMenu():
    ''' Function that show Main Menu of the game. User can choose what he
        want to do (Start New Game, Continue, show info About the game
        and Exit from game)
    '''
    res = 0
    print('~~~~~____Neuralturer____~~~~~')
    print('Main Menu')
    print('Input digit corresponding option that you want')
    canContinue = 0
    if os.path.exists(constDataFileName):
        canContunue = 1
        print('1. Continue Game')
    print(str(1 + canContinue) + '. New Game')
    print(str(2 + canContinue) + '. About')
    print(str(3 + canContinue) + '. Exit')
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

def SaveGame(Character, Inventory):
    ''' Function that save Game Data to constDataFileName file.
        Be sure that Inventory is (List of Weapon, List of Armour)
    '''
    res = (Character, Inventory)
    f = open(constDataFileName, 'bw')
    dump(res, f)
    f.close()
    print('Successfully saved!')

def CityMarket(Hero, Inventory):
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
    PotionRange = ({'Name': 'Heal Potion', 'Description':"""This potion can
                    restore your health""", 'Price': 20},
                    {'Name': 'Damage Potion', 'Description': """This potion
                     can increase your strength for short time""", 'Price': 20})
    PlayerChoice = '0'
    while PlayerChoice != '4':
        print('_____MARKET_____')
        print('1. Visit weaponsmith')
        print('2. Visit armoursmith')
        print('3. Visit alchemist')
        print('4. Leave')
        print()
        PlayerChoice = input('You decided: [> ')
        if PlayerChoice == '1':
            # list of available weapons
            for i in range(0, len(WeaponRange)):
                print(str(i) + '.', WeaponRange[i]['Name'], ' '*3, 'Damage:',
                      WeaponRange[i]['Damage'][0], '-', WeaponRange[i]['Damage'][1],
                      ' '*3, 'Speed:', WeaponRange[i]['AttackSpeed'], ' '*3, 'Price:',
                      WeaponRange[i]['Price'])
            print('8. Leave')
            pch = input('You decided: [> ')
            if pch in '123456780':
                if pch == '8':
                    PlayerChoice = 0
                else:
                    pch = int(pch)
                    # you can buy if you have enough golds
                    if Hero.chGetGeneralParam('Gold') >= WeaponRange[pch]['Price']:
                        Hero.chSetGeneralParam('Gold',
                            Hero.chGetGeneralParam('Gold') - WeaponRange[pch]['Price'])
                        weapon = clWeapon(WeaponRange[pch]['Name'],
                                          WeaponRange[pch]['Description'],
                                          WeaponRange[pch]['Price'],
                                          WeaponRange[pch]['Damage'][0],
                                          WeaponRange[pch]['Damage'][1],
                                          WeaponRange[pch]['AttackSpeed'])
                        # you get it
                        Hero.chAddWeapon(weapon)
                        Inventory[0].append(weapon)
                        WeaponRange.remove(WeaponRange[pch])
                    else:
                        print('Not enough GOLD!')
            else:
                print('Imposible to choose', pch)
        elif PlayerChoice == '2':
            # same with armour
            for i in range(0, len(ArmourRange)):
                print(str(i) + '.', ArmourRange[i]['Name'], ' '*3, 'Health boost:',
                      ArmourRange[i]['HealthBoost'], ' '*3, 'Speed boost:',
                      ArmourRange[i]['SpeedBoost'], ' '*3,  'Price:', WeaponRange[i]['Price'])
            print('3. Leave')
            pch = input('You decided: [> ')
            if pch in '1230':
                if pch == '3':
                    PlayerChoice = 0
                else:
                    pch = int(pch)
                    if Hero.chGetGeneralParam('Gold') >= ArmourRange[pch]['Price']:
                        Hero.chSetGeneralParam('Gold',
                            Hero.chGetGeneralParam('Gold') - ArmourRange[pch]['Price'])
                        armour = clArmour(ArmourRange[pch]['Name'],
                                          ArmourRange[pch]['Description'],
                                          ArmourRange[pch]['Price'],
                                          ArmourRange[pch]['HealthBoost'],
                                          ArmourRange[pch]['SpeedBoost'])
                        Hero.chAddArmour(armour)
                        Inventory[1].append(armour)
                        ArmourRange.remove(ArmourRange[pch])
                    else:
                        print('Not enough GOLD!')
            else:
                print('Imposible to choose', pch)
        elif PlayerChoice == '3':
            # Potions
            for i in range(0, len(PotionRange)):
                print(str(i) + '.', PotionRange[i]['Name'], ' '*5,
                      'Price:', PotionRange[i]['Price'])
            print('2. Leave')
            pch = input('You decided: [> ')
            if pch in '120':
                if pch == '2':
                    PlayerChoice = 0
                else:
                    pch = int(pch)
                    if Hero.chGetGeneralParam('Gold') >= PotionRange[pch]['Price']:
                        if Hero.chGetGeneralParam('PotionSlots')[pch] < Hero.chGetGeneralParam('MaxPotion'):
                            Hero.chSetGeneralParam('Gold',
                                Hero.chGetGeneralParam('Gold') - PotionRange[pch]['Price'])
                            hpot = Hero.chGetGeneralParam('PotionSlots')[0]
                            dpot = Hero.chGetGeneralParam('PotionSlots')[1]
                            pot = ([hpot + 1, dpot] if pch == 0 else [hpot, dpot + 1])
                            Hero.chSetGeneralParam('PotionSlots', pot)
                        else:
                            print('No free space!')
                    else:
                        print('Not enough GOLD!')
            else:
                print('Imposible to choose', pch)

def HeroInfoOption(Hero, Inventory):
    ''' This function can show Hero information as chShowInfo and show Inventory.
        Player can equip item from Inventory
    '''
    PlayerChoice = '0'
    while PlayerChoice != '5':
        print('_____Player Info_____')
        print('1. General info')
        print('2. Full info')
        print('3. Weapons')
        print('4. Armours')
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
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                print(str(i) + '.', Inventory[0][i]['Name'])
                print(' '.join(Inventory[0][i]['Description'].split()))
            print('What you want to equip? (-1 for nothing)')
            pch = input('You decided: [> ')
            if pch.isdigit():
                if pch == '-1':
                    PlayerChoice = '0'
                elif int(pch) >= len(Inventory[0]):
                    print('Incorrect input!')
                else:
                    Hero.chAddWeapon(Inventory[0][int(pch)])
            else:
                print('Impossible to choose', pch)
        elif PlayerChoice == '4':
            print('You have next armours.')
            for i in range(0, len(Inventory[1])):
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                print(Inventory[1][i]['Name'])
                print(' '.join(Inventory[1][i]['Description'].split()))
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('What you want to equip? (-1 for nothing)')
            pch = input('You decided: [> ')
            if pch.isdigit():
                if pch == '-1':
                    PlayerChoice = '0'
                elif int(pch) >= len(Inventory[1]):
                    print('Incorrect input!')
                else:
                    Hero.chAddArmour(Inventory[1][int(pch)])
            else:
                print('Impossible to choose', pch)
