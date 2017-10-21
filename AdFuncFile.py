# Neuralturer game
# File with useful functional

from random import randint

class clWeapon:
    """ Weapon class
        There is wpGeneralParam with keys:
        str Name
        int MinDamage, MaxDamage
        int AttackSpeed
        methods:
        wpShowInfo()
    """

    __wpGeneralParam = 0
    def __init__(self, Name = 'None', MinDamage = 0, MaxDamage = 0, AttackSpeed = 0):
        self.__wpGeneralParam = dict()
        self.__wpGeneralParam['Name'] = Name
        self.__wpGeneralParam['MinDamage'] = MinDamage
        self.__wpGeneralParam['MaxDamage'] = MaxDamage
        self.__wpGeneralParam['AttackSpeed'] = AttackSpeed
    def __getitem__(self, key):
        return self.__wpGeneralParam[key]

    def wpShowInfo(self):
        ''' Just show info about Weapon
        '''
        for Key in self.__wpGeneralParam.keys():
            print(Key + ':', self.__wpGeneralParam[Key])

class clArmour:
    """ Armour class
        There is arGeneralParam with keys:
        str Name
        int HealthBoost, SpeedBoost
        methods:
        arShowInfo()
    """
    __arGeneralParam = 0
    def __init__(self, Name = 'None', HealthBoost = 0, SpeedBoost = 0):
        self.__arGeneralParam = dict()
        self.__arGeneralParam['Name'] = Name
        self.__arGeneralParam['HealthBoost'] = HealthBoost
        self.__arGeneralParam['SpeedBoost'] = SpeedBoost
    def __getitem__(self, key):
        return self.__arGeneralParam[key]

    def arShowInfo(self):
        ''' Just show info about Weapon
        '''
        for Key in self.__arGeneralParam.keys():
            print(Key + ':', self.__arGeneralParam[Key])

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

def CountProbability(percent):
    ''' Count probability of starting event
        if event can start => return 1 else return 0
    '''
    randomNumber = randint(1, 10000)
    if randomNumber <= percent * 100:
        return 1
    else:
        return 0

class clCharacter:
    """ Character class
        There are:
        chGeneralParams:
        str Name - name of Character
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
        int Agility - each point increase chAttackSpeed by 5
        int Attention - each point increase chFindChance by 10
        int Charisma - each point increase chKnowChance by 10
        int Intelligence - each point increase chPotionRestore by 1
        int Instinct - each point increase chFleeChance by 10

        Every 10 levels player gets 1 point to spend it to chSpecialTrait:
        int Undead - every point increase chHealth by 20
        int Carrier - every point increase chMaxPotions by 2
        int QuickHand - every point increase chSpeed by 20
        int OnePunch - every point increase chSpeed by 8
        int Physician - every point increase chBattleRestore by 16
        int Trader - character gets 1000 Golds

        Methods:
        chShowInfo(Param); Param = 0, 1, 2, 3
        chIncreaseCommonTrait(CommonTraitKey); Key is from chCommonTrait
        chIncreaseSpecialTrait(SpecialTraitKey); same
        chRemoveWeapon(Weapon); chRemoveArmour(Armour)
        chAddWeapon(NewWeapon); chAddArmour(NewArmour)
        chHealthRestore(modifier); modifier = 0 => Restore value of BattleRestore
             otherwise full restoration
        chChangeGeneralParam(Key, Value); Key from chGeneralParam
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
    __chWeapon = clWeapon()
    __chArmour = clArmour()
    __chCommonTrait = 0
    __chSpecialTrait = 0
    def __init__(self, Name = '', Health = 50, MinDamage = 1, MaxDamage = 3,
                 MaxPotion = 5, PotionSlots = [0, 0], PotionRestore = 1,
                 Gold = 100, Level = 0, Experience = 0, Weapon = clWeapon(), Armour = clArmour(),
                 HitChance = 50, AttackSpeed = 5, FindChance = 0, KnowChance = 0,
                 FleeChance = 0, BattleRestore = 20, Vitality = 0, Strength = 0,
                 Luck = 0, Agility = 0, Accuracy = 0, Attention = 0, Charisma = 0,
                 Intelligence = 0, Instinct = 0, Undead = 0, Carrier = 0,
                 QuickHand = 0, OnePunch = 0, Physician = 0, Trader = 0):
        self.__chGeneralParam = dict()
        self.__chGeneralParam['Name'] = Name
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
        '''Param - how much info you need
           Param = 0 shows you only General params
           Param = 1 shows you only Character Traits
           Param = 2 show you only Character Special Traits
           Param = 3 show you every param
        '''
        if Param == 0 or Param == 3:
            print("Name:", self.__chGeneralParam['Name'], " "*5,
                  "Level:", self.__chGeneralParam['Level'], " "*5,
                  "Exp:", str(self.__chGeneralParam['Experience']) + '/' +
                  str(chHowMuchExpNeed(self.__chGeneralParam['Level'])), " "*5,
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
            print(CommonTraitKey, 'has been increased!')
            if CommonTraitKey == 'Vitality':
                self.__chGeneralParam['MHealth'] += 5
            elif CommonTraitKey == 'Strength':
                self.__chGeneralParam['MinDamage'] += 2
                self.__chGeneralParam['MaxDamage'] += 2
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
            by SpecialTrait
        '''
        # if if if if if if ... if
        if SpecialTraitKey in self.__chSpecialTrait.keys():
            self.__chSpecialTrait[SpecialTraitKey] += 1
            print(SpecialTraitKey, 'has been improve!')
            if SpecialTraitKey == 'Undead':
                self.__chGeneralParam['MHealth'] += 20
            elif SpecialTraitKey == 'Carrier':
                self.__chGeneralParam['MaxPotion'] += 2
            elif SpecialTraitKey == 'QuickHand':
                self.__chGeneralParam['AttackSpeed'] += 20
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

    def chHealthRestore(self, modifier=0):
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
        ''' Change chGeneralParam[Key] with value
        '''
        if Key in self.__chGeneralParam.keys():
            self.__chGeneralParam[Key] += value
        else:
            print('Enable to change', Key)

    def chGetGeneralParam(self, Key):
        ''' return GeneralParam by Key
        '''
        if Key in self.__chGeneralParam.keys():
            return self.__chGeneralParam[Key]
        else:
            return -1

    def chGetCommonTrait(self, Key):
        ''' return CommonTrait by Key
        '''
        if Key in self.__chCommonTrait.keys():
            return self.__chCommonTrait[Key]
        else:
            return -1

    def chGetSpecialTrait(self, Key):
        ''' return SpecialTrait by Key
        '''
        if Key in self.__chSpecialTrait.keys():
            return self.__chSpecialTrait[Key]
        else:
            return -1

    def chDoHit(self):
        ''' Let's smash our enemies!
            return delivered Damage. It can be 0, if Character misses
        '''
        res = 0
        # let's check, can we hit or not
        if CountProbability(self.__chGeneralParam['HitChance']):
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
        ''' potion effect is disappeared. As you can guess, it works for Damage PotionRestore
        '''
        self.__chGeneralParam['MinDamage'] -= self.__chGeneralParam['PotionRestore']
        self.__chGeneralParam['MaxDamage'] -= self.__chGeneralParam['PotionRestore']
