# Neuralturer game
# File with useful functional

'''
Character class
There are
str chName
int chHealth, chDamage[int min, int max]
int chMaxPoison, chPoisonSlots[int HealthRestore, IncDamage]
int chPoisonRestore
int chGold
int chLevel
int chHitChance - chance to hit the enemy
int chAttackSpeed - if you have A*[Enemy]chAttackSpeed then you hit A times
int chFindChance - chance to find interesting in others places
int chKnowChance - chance to know something interesting from people
int chFleeChance - chance to flee from dead figth
int chBattleRestore - percent of chHelth restore after every battle

Every new level player gets 1 point. At the first level player has 3 points
You can increase nex traits
int chVitality - each point increase chHealth by 5
int chStrength - each point increase chDamage by 2
int chAccuracy - each point increase chHitChance by 5
int chLuck - who has more chLuck that smashes enemy the first
int chAgility - each point increase chAttackSpeed by 5
int chAttention - each point increase chFindChance by 10
int chCharisma - each point increase chKnowChance by 10
int chIntelligence - each point increase chPoisonRestore by 1
int chInstinct - each point increase chFleeChance by 10

Every 10 levels player can choose one of next special traits
int chUndead - every point increase chHealth by 20
int chCarrier - every point increase chMaxPoison 2
int chQuickHand - every point increase chSpeed by 20
int chOnePunch - every point increase chSpeed by 8
int chPhysician - every point increase chBattleRestore by 16
int chTrader - character gets 1000 Golds
'''
class clCharacter:
    chName = ''
    chHealth = 50
    chDamage = [1, 3]
    chMaxPoison = 5
    chPoisonSlots = [0, 0]
    chPoisonRestore = 1
    chGold = 100
    chLevel = 0
    chHitChance = 50
    chAttackSpeed = 5
    chFindChance = 0
    chKnowChance = 0
    chFleeChance = 0
    chBattleRestore = 16    
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

