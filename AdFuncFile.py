# Neuralturer game
# File with useful functional

class clCharacter:
    """ Character class
        There are:
        General Params:
        str Name - name of Character
        int Health, chMinDamage, chMaxDamage - health of Character and Damage
        int MaxPotion, PotionSlots[int HealthRestore, IncDamage] - max count that Character can carry
        and Count of each poison types
        int PotionRestore - how much potion can restore points
        int Gold - gold of Character
        int Level - Level of character
        int HitChance - chance to hit the enemy
        int AttackSpeed - if you have A*[Enemy]chAttackSpeed then you hit A times
        int FindChance - chance to find interesting in others places
        int KnowChance - chance to know something interesting from people
        int FleeChance - chance to flee from dead figth
        int BattleRestore - percent of chHelth restore after every battle

        Every new level player gets 1 point. At the first level player has 3 points
        You can increase next traits:
        int Vitality - each point increase chHealth by 5
        int Strength - each point increase chDamage by 2
        int Accuracy - each point increase chHitChance by 5
        int Luck - who has more chLuck that smashes enemy the first
        int Agility - each point increase chAttackSpeed by 5
        int Attention - each point increase chFindChance by 10
        int Charisma - each point increase chKnowChance by 10
        int Intelligence - each point increase chPotionRestore by 1
        int Instinct - each point increase chFleeChance by 10

        Every 10 levels player gets 1 point to spend it to special traits:
        int Undead - every point increase chHealth by 20
        int Carrier - every point increase chMaxPotions by 2
        int QuickHand - every point increase chSpeed by 20
        int OnePunch - every point increase chSpeed by 8
        int Physician - every point increase chBattleRestore by 16
        int Trader - character gets 1000 Golds
    """
    # define character params
    chGeneralParam = {'Name': '', 'Health': 50, 'MinDamage': 1,
                      'MaxDamage': 3, 'MaxPotion': 5, 'PotionSlots': [0, 0],
                      'PotionRestore': 1, 'Gold': 100, 'Level': 0,
                      'HitChance': 50, 'AttackSpeed': 5,
                      'FindChance': 0, 'KnowChance': 0,
                      'FleeChance': 0, 'BattleRestore': 20}
    chCommonTrait = {'Vitality': 0, 'Strength': 0, 'Luck': 0,
                     'Accuracy': 0, 'Attention': 0, 'Charisma': 0,
                     'Intelligence': 0, 'Instinct': 0, 'Agility': 0}
    chSpecialTrait = {'Undead': 0, 'Carrier': 0, 'QuickHand': 0,
                      'OnePunch': 0, 'Physician': 0, 'Trader': 0}



    def __init__(self, Name):
        self.chGeneralParam['Name'] = Name

    def ShowInfo(self, Param = 0):
        '''Param - how much info you need
           Param = 0 shows you only General params
           Param = 1 shows you only Character Traits
           Param = 2 show you only Character Special Traits
           Param = 3 show you every param
        '''
        if Param == 0 or Param == 3:
            print("Name:", self.chGeneralParam['Name'], " "*5,
                  "Level:", self.chGeneralParam['Level'], " "*5,
                  "Gold:", self.chGeneralParam['Gold'])
            print("Health:", self.chGeneralParam['Health'])
            print("Damage:", self.chGeneralParam['MinDamage'],
                  "-", self.chGeneralParam['MaxDamage'])
            print("Potions: Healing", str(self.chGeneralParam['PotionSlots'][0])+
                  "/"+str(self.chGeneralParam['MaxPotion'])+ "; Damage "+
                  str(self.chGeneralParam['PotionSlots'][1])+"/"+
                  str(self.chGeneralParam['MaxPotion']))
            print("Each potion gets +" + str(self.chGeneralParam['PotionRestore']))
            print("Attack speed:", self.chGeneralParam['AttackSpeed'],
                  " "*5, "Hit Chance:", self.chGeneralParam['HitChance'])
            print("Chance to know something interesting from people:",
                  self.chGeneralParam['KnowChance'])
            print("Chance to find something interesting in the area:",
                  self.chGeneralParam['FindChance'])
            print("Chance to flee from figth:", self.chGeneralParam['FleeChance'])
            print(str(self.chGeneralParam['BattleRestore'])+"%"+" will heal after every battle")
        if Param == 1 or Param == 3:
            print(self.chGeneralParam['Name'], "has next traits:")
            print("Vitality:", self.chCommonTrait['Vitality'])
            print("Strength:", self.chCommonTrait['Strength'])
            print("Accuracy:", self.chCommonTrait['Accuracy'])
            print("Luck:", self.chCommonTrait['Luck'])
            print("Agility:", self.chCommonTrait['Agility'])
            print("Attention:", self.chCommonTrait['Attention'])
            print("Charisma:", self.chCommonTrait['Charisma'])
            print("Intelligence:", self.chCommonTrait['Intelligence'])
            print("Instinct:", self.chCommonTrait['Instinct'])
        if Param == 2 or Param == 3:
            if (not self.chSpecialTrait['Undead'] and not self.chSpecialTrait['Carrier']
                and not self.chSpecialTrait['QuickHand'] and not self.chSpecialTrait['OnePunch']
                and not self.chSpecialTrait['Physician'] and not self.chSpecialTrait['Trader']):
                print(self.chGeneralParam['Name'], "has no special traits.")
            else:
                print(self.chGeneralParam['Name'], "has next special traits:")
            if self.chSpecialTrait['Undead'] != 0:
                print("Undead with", self.chSpecialTrait['Undead'], "power")
            if self.chSpecialTrait['Carrier'] != 0:
                print("Carrier with", self.chSpecialTrait['Carrier'], "power")
            if self.chSpecialTrait['QuickHand'] != 0:
                print("Quick Hand with", self.chSpecialTrait['QuickHand'], "power")
            if self.chSpecialTrait['OnePunch'] != 0:
                print("One Punch with", self.chSpecialTrait['OnePunch'], "power")
            if self.chSpecialTrait['Physician'] != 0:
                print("Physician with", self.chSpecialTrait['Physician'], "power")
            if self.chSpecialTrait['Trader'] != 0:
                print("Trader with", self.chSpecialTrait['Trader'], "power")

    def chIncreaseCommonTrait(self, CommonTraitKey):
        ''' Method increase choosen chCommonTrait
            by CommonTraitKey
        '''
        # just a lot of 'if'
        if CommonTraitKey in self.chCommonTrait.keys():
            print(CommonTraitKey, 'has been increased!')
            self.chCommonTrait[CommonTraitKey] += 1
            if CommonTraitKey == 'Vitality':
                self.chGeneralParam['Health'] += 5
            elif CommonTraitKey == 'Strength':
                self.chGeneralParam['MinDamage'] += 2
                self.chGeneralParam['MaxDamage'] += 2
            elif CommonTraitKey == 'Accuracy':
                self.chGeneralParam['HitChance'] += 5
            elif CommonTraitKey == 'Attention':
                self.chGeneralParam['FindChance'] += 10
            elif CommonTraitKey == 'Charisma':
                self.chGeneralParam['KnowChance'] += 10
            elif CommonTraitKey == 'Intelligence':
                self.chGeneralParam['PotionRestore'] += 1
            elif CommonTraitKey == 'Instinct':
                self.chGeneralParam['FleeChance'] += 10
        else:
            print("Imposible to improve", CommonTraitKey)

    def chIncreaseSpecialTrait(self, SpecialTraitKey):
        ''' Method increase choosen chSpecialTrait
            by SpecialTrait
        '''
        # if if if if if if ... if
        if SpecialTraitKey in self.chSpecialTrait.keys():
            print(SpecialTraitKey, 'has been improve!')
            self.chSpecialTrait[SpecialTraitKey] += 1
            if SpecialTraitKey == 'Undead':
                self.chGeneralParam['Health'] += 20
            elif SpecialTraitKey == 'Carrier':
                self.chGeneralParam['MaxPotion'] += 2
            elif SpecialTraitKey == 'QuickHand':
                self.chGeneralParam['AttackSpeed'] += 20
            elif SpecialTraitKey == 'OnePunch':
                self.chGeneralParam['MinDamage'] += 8
                self.chGeneralParam['MaxDamage'] += 8
            elif SpecialTraitKey == 'Physician':
                self.chGeneralParam['BattleRestore'] += 16
            elif SpecialTraitKey == 'Trader':
                self.chGeneralParam['Gold'] += 1000
        else:
            print("Imposible to improve", SpecialTraitKey)
