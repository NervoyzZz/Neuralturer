# Neuralturer game
# File with useful functional

class clCharacter:
    """ Character class
        There are:
        General Params:
        str chName - name of Character
        int chHealth, chDamage[int min, int max] - helth of Character and Damage
        int chMaxPotion, chPotionSlots[int HealthRestore, IncDamage] - max count that Character can carry
        and Count of each poison types 
        int chPotionRestore - how much potion can restore points
        int chGold - gold of Character
        int chLevel - Level of character
        int chHitChance - chance to hit the enemy
        int chAttackSpeed - if you have A*[Enemy]chAttackSpeed then you hit A times
        int chFindChance - chance to find interesting in others places
        int chKnowChance - chance to know something interesting from people
        int chFleeChance - chance to flee from dead figth
        int chBattleRestore - percent of chHelth restore after every battle

        Every new level player gets 1 point. At the first level player has 3 points
        You can increase next traits:
        int chVitality - each point increase chHealth by 5
        int chStrength - each point increase chDamage by 2
        int chAccuracy - each point increase chHitChance by 5
        int chLuck - who has more chLuck that smashes enemy the first
        int chAgility - each point increase chAttackSpeed by 5
        int chAttention - each point increase chFindChance by 10
        int chCharisma - each point increase chKnowChance by 10
        int chIntelligence - each point increase chPotionRestore by 1
        int chInstinct - each point increase chFleeChance by 10

        Every 10 levels player gets 1 point to spend it to special traits:
        int chUndead - every point increase chHealth by 20
        int chCarrier - every point increase chMaxPotions by 2
        int chQuickHand - every point increase chSpeed by 20
        int chOnePunch - every point increase chSpeed by 8
        int chPhysician - every point increase chBattleRestore by 16
        int chTrader - character gets 1000 Golds    
    """
    # define character params
    chName = ''
    chHealth = 50
    chDamage = [1, 3]
    chMaxPotion = 5
    chPotionSlots = [0, 0]
    chPotionRestore = 1
    chGold = 100
    chLevel = 0
    chHitChance = 50
    chAttackSpeed = 5
    chFindChance = 0
    chKnowChance = 0
    chFleeChance = 0
    chBattleRestore = 20    
    chVitality = 0
    chStrength = 0
    chAccuracy = 0
    chLuck = 0
    chAgility = 0
    chAttention = 0
    chCharisma = 0
    chIntelligence = 0
    chInstinct = 0
    
    chUndead = 0
    chCarrier = 0
    chQuickHand = 0
    chOnePunch = 0
    chPhysician = 0
    chTrader = 0

    def __init__(self, Name):
        self.chName = Name

    def ShowInfo(self, Param = 0):
        '''Param - how much info you need
           Param = 0 shows you only General params
           Param = 1 shows you only Character Traits
           Param = 2 show you only Character Special Traits
           Param = 3 show you every param       
        '''
        if Param == 0 or Param == 3:
            print("Name:", self.chName, " "*5, "Level:", self.chLevel, " "*5, "Gold:", self.chGold)
            print("Health:", self.chHealth)
            print("Damage:", self.chDamage[0], "-", self.chDamage[1])
            print("Potions: Healing", str(self.chPotionSlots[0])+"/"+str(self.chMaxPotion)+"; Damage "+str(self.chPotionSlots[1])+"/"+str(self.chMaxPotion))
            print("Each potion gets +" + str(self.chPotionRestore))
            print("Attack speed:", self.chAttackSpeed, " "*5, "Hit Chance:", self.chHitChance)
            print("Chance to know something interesting from people:", self.chKnowChance)
            print("Chance to find something interesting in the area:", self.chFindChance)
            print("Chance to flee from figth:", self.chFleeChance)
            print(str(self.chBattleRestore)+"%"+" will heal after every battle")
        if Param == 1 or Param == 3:
            print(self.chName, "has next traits:")
            print("Vitality:", self.chVitality)
            print("Strength:", self.chStrength)
            print("Accuracy:", self.chAccuracy)
            print("Luck:", self.chLuck)
            print("Agility:", self.chAgility)
            print("Attention:", self.chAttention)
            print("Charisma:", self.chCharisma)
            print("Intelligence:", self.chIntelligence)
            print("Instinct:", self.chInstinct)
        if Param == 2 or Param == 3:
            if not self.chUndead and not self.chCarrier and not self.chQuickHand and not self.chOnePunch and not self.chPhysician and not self.chTrader:
                print(self.chName, "has no special traits.")
            else:
                print(self.chName, "has next special traits:")
            if self.chUndead != 0:
                print("Undead with", self.chUndead, "power")
            if self.chCarrier != 0:
                print("Carrier with", self.chCarrier, "power")
            if self.chQuickHand != 0:
                print("Quick Hand with", self.chQuickHand, "power")
            if self.chOnePunch != 0:
                print("One Punch with", self.chOnePunch, "power")
            if self.chPhysician != 0:
                print("Physician with", self.chPhysician, "power")
            if self.chTrader != 0:
                print("Trader with", self.chTrader, "power")



