from random import *
class protagonist:
    def __init__ (self, perk):
        self.hp  = 100
        self.dmgLight = 5
        self.dmgHeavy = 10
        self.cripple = 0
        self.fracture = 0
        self.bleed  = 0
        self.artery = 0
        self.i4s = 0
        self.meleeDefenseMulti = 1
        self.rangeDefenseMulti = 1
        if perk == 1:
            self.meleeDefenseMulti = 1.1
            self.rangeDefenseMulti = 1.1
        elif perk == 2:
            self.meleeDefenseMulti = 0.9
            self.rangeDefenseMulti = 1.2
            self.dmgLight = 6
            self.dmgHeavy = 12
    def debuffProt(self, effectID):
          if effectID == 1:
              self.bleed = 30
              print("You're bleeding...")
          elif effectID == 2:
              self.artery = 20
              print("Your arteries hurt...")
          elif effectID == 3:
              self.cripple = 45
              print ("Your leg is broken. You can't roam far or flee.")
          elif effectID == 4:
              self.fracture = 45
              print("Your arm is broken. You can't use Shove.")
          elif effectID == 5:
              self.dmgLight = self.dmgLight + 1
              self.dmgHeavy = self.dmgHeavy + 2
              print("Honorable applied")
    
    def displayStats(self):
        print(f"Player - {player.hp}/100 HP")
        textBuffer = ""
        if self.fracture > 0:
            textBuffer = textBuffer + f"[FRACTURE {str(self.fracture)}]     "
        if self.cripple > 0:
            textBuffer = textBuffer + f"[CRIPPLE {str(self.cripple)}]     "
        if self.bleed > 0:
            textBuffer = textBuffer + f"[BLEED {str(self.bleed)}]      "
        if self.artery > 0:
            textBuffer = textBuffer + f"[ARTERY {str(self.artery)}]     "
        print(textBuffer)
    
    def damageProt(self, dmg):
        self.hp = self.hp - dmg
        print(f"You took {str(dmg)} damage.")
        if self.hp <= 0:
            self.isDead = True
    
    def turn(self):
        if self.cripple > 0:
            self.cripple = self.cripple - 1
            if self.cripple == 0:
                print("Your leg healed.")
        if self.fracture > 0:
            self.fracture = self.fracture - 1
            if self.fractureEffect == 0:
                print("Your arm healed.")
        if self.bleed > 0:
            self.bleed = self.bleed - 1
            self.hp = self.hp - 1
            if self.bleed == 0:
                print("You're no longer bleeding.")
        if self.artery > 0:
            self.artery = self.artery - 1
            self.hp = self.hp - 2
            self.bleed = 5
            if self.artery == 0:
                print("Your artery healed. You still have a slight bleed.")
        if self.hp <= 0:
            self.isDead = True

class hostileHuman:
    def __init__(self, hp, light, heavy, shove, parry, ranged):
        self.hp = hp
        self.lightDamage = light
        self.heavyDamage = heavy
        self.shove = shove
        self.parry = parry
        self.ranged = ranged
        self.maxHp = hp
        self.parry = False
    def displayStats(self):
        print(f"Enemy - HP {self.hp}/{self.maxHp}")
    def beginParry(self):
        self.parry = True
        print("The enemy is parrying.")
    def takeShove(self):
        self.parry = False
        self.stunned = True
    def takeDamage(self, amount):
        if self.parry == False:
            self.hp = self.hp - round(amount*self.resistmulti)
            print(f"The enemy took {round(amount*self.resistmulti)} damage.")
        elif self.parry:
            print("Enemy blocked the attack ")
            self.parry = False
def battle(name, hp, lightDamage, heavyDamage, canShove, canParry, isRanged):
    enemy = hostileHuman(HP, lightDamage, heavyDamage, canShove, canParry, isRanged)
    print(f"{name} blocks your way.")
    while enemy.hp > 0:
        player.displayStats()
        player.turn()
        turns = 4
        print(f"Your turn. Actions: {turns}")
        print("""Actions:
light - 1 turn simple attack
lightc - 3 turn L-L-L*1.5 combo rounded damage
heavy - inefficient, powerful, consumes 2 turns
shove - stun enemy to flee, ends turn
parry - ends turn, block attack chance to stun
flee - REQUIRES STUNNED ENEMY attempt to flee battle""")
        action = input("Your move: ")
        if action == "light":
            enemy.takeDamage(player.dmgLight)
            turns = turns - 1
        elif action == "lightc":
            enemy.takeDamage(player.dmgLight)
            enemy.takeDamage(player.dmgLight)
            enemy.takeDamage(round(player.dmgLight*1.5))
            turns = turns - 3
        elif action == "heavy":
            enemy.takeDamage(player.dmgHeavy)
            turns = turns - 2
        elif action == "parry":
            parry = True
            turns = 0
        elif action == "shove":
            shove = True
            turns = 0

print("Welcome to Winter's End")
print("""Status effects:
FRACTURE disables shoves.
CRIPPLE disables Castle and Tower locations and fleeing.
BLEED slowly saps your HP.
and ARTERY BLEEDING saps it even faster.""")
input("Enter to continue.")
print("""Choose your perk.
1 - ARTILLERIST has better ranged performance but is weak at melee.
2 - EXECUTIONER has powerful melee performance but suffers from issues with ranged enemies.
Leave Blank - SURVIVALIST doesn't have any special quirk. The recommended beginner class.""")

perkChoice = input("Input perk ID: ")
if perkChoice == "":
    perkChoice = "3"
player = protagonist(int(perkChoice))
player.debuffProt(4)
player.debuffProt(3)
player.debuffProt(2)
player.debuffProt(1)
player.damageProt(15)
player.displayStats()
night = 1
while player.isDead == False:
    print("hi")
